"""Typed event payloads for every Radion realtime channel.

Each channel emits a ``data`` object discriminated by a snake_case ``type``
field (the ``prices`` channel is the exception -- a flat tick with no ``type``).
The ``TypedDict``\\ s below enumerate every ``data.type`` value a channel can
carry and type the fields documented for that channel's payload.

Provenance: field schemas mirror the published channel docs
(``/websockets/channels/*``), which document one representative payload per
channel plus the full discriminator set. Fields that are not universal across a
channel's events are optional (``total=False``), and additional fields the
protocol carries are preserved on the underlying ``dict``. Regenerate from the
backend protocol schema to tighten per-event field sets.
"""

from __future__ import annotations

from typing import Literal, TypedDict

# --- trades ----------------------------------------------------------------

TradeEventType = Literal[
    "order_filled_v1",
    "order_filled_v2",
    "orders_matched_v1",
    "orders_matched_v2",
]


class TradesPayload(TypedDict, total=False):
    """Confirmed fill / order-match payload from the exchange contracts."""

    type: TradeEventType
    orderHash: str
    maker: str
    taker: str
    side: int  # 0 = buy, 1 = sell. v2 fills and matches only.
    tokenId: str
    makerAmountFilled: str
    takerAmountFilled: str
    fee: str
    builder: str
    metadata: str


# --- oracle ----------------------------------------------------------------

OracleEventType = Literal[
    "uma_adapter_question_initialized",
    "uma_adapter_question_resolved",
    "uma_adapter_question_emergency_resolved",
    "uma_adapter_question_flagged",
    "uma_adapter_question_paused",
    "uma_adapter_question_unpaused",
    "uma_adapter_question_reset",
    "uma_adapter_ancillary_data_updated",
    "uma_optimistic_question_initialized",
    "uma_optimistic_question_resolved",
    "uma_optimistic_question_paused",
    "uma_optimistic_question_unpaused",
    "uma_optimistic_question_settled",
    "uma_optimistic_resolution_data_requested",
    "uma_optimistic_question_updated",
    "uma_optimistic_question_flagged_for_admin_resolution",
]


class OraclePayload(TypedDict, total=False):
    """UMA oracle lifecycle payload."""

    type: OracleEventType
    questionID: str
    settledPrice: str  # int256 as a signed decimal string (e.g. "-1").
    payouts: list[str]


# --- lifecycle -------------------------------------------------------------

LifecycleEventType = Literal[
    "market_prepared",
    "neg_risk_question_prepared",
    "outcome_reported",
    "event_prepared",
    "condition_resolved",
    "condition_preparation",
    "condition_resolution",
    "token_registered",
]


class LifecyclePayload(TypedDict, total=False):
    """Market / condition lifecycle payload."""

    type: LifecycleEventType
    conditionId: str
    oracle: str
    questionId: str
    outcomeSlotCount: str


# --- activity --------------------------------------------------------------

ActivityEventType = Literal[
    "redemption",
    "binary_redemption",
    "neg_risk_redemption",
    "positions_redeemed",
    "collateral_position_split",
    "collateral_positions_merged",
    "collateral_positions_converted",
    "neg_risk_positions_converted",
    "ctf_position_split",
    "ctf_positions_merge",
    "ctf_payout_redemption",
]


class ActivityPayload(TypedDict, total=False):
    """Redemption / split / merge / conversion payload."""

    type: ActivityEventType
    initiator: str
    conditionId: str
    amounts: list[str]
    payout: str


# --- collateral ------------------------------------------------------------

CollateralEventType = Literal["transfer", "approval", "wrapped", "unwrapped"]

# Functional syntax: the wire payload uses ``from``, a Python keyword.
CollateralPayload = TypedDict(
    "CollateralPayload",
    {
        "type": CollateralEventType,
        "from": str,
        "to": str,
        "amount": str,
    },
    total=False,
)
"""ERC-20 collateral payload."""


# --- combos ----------------------------------------------------------------

CombosEventType = Literal[
    "event_prepared",
    "result_reported",
    "position_redeemed",
    "module_positions_merged",
    "module_positions_split",
    "horizontal_merge",
    "horizontal_split",
    "position_converted",
    "condition_resolved",
    "resolution_paused",
    "resolution_unpaused",
    "resolver_paused",
    "resolver_unpaused",
    "bridge_position_minted",
    "bridge_positions_burned",
    "legacy_collateral_settled",
    "migration_condition_registered",
    "migration_resolved",
    "position_migrated",
    "combinatorial_condition_prepared",
    "compressed",
    "converted_to_yes_basket",
    "extracted",
    "injected",
    "merged_from_yes_basket",
    "merged_on_condition",
    "split_on_condition",
    "combinatorial_wrapped",
    "combinatorial_unwrapped",
    "transfer_single",
    "transfer_batch",
]


# Functional syntax: the wire payload uses ``from``, a Python keyword.
CombosPayload = TypedDict(
    "CombosPayload",
    {
        "type": CombosEventType,
        "operator": str,
        "from": str,
        "to": str,
        "id": str,
        "amount": str,
    },
    total=False,
)
"""Module / bridge / combinatorial / ERC-1155 payload."""


# --- prices ----------------------------------------------------------------


class PricesPayload(TypedDict):
    """Last-traded price tick. Flat shape -- no ``type`` discriminator."""

    token_id: str
    price: float  # last-traded price, USDC per share.
    timestamp_ms: int  # when the tick was produced (Unix ms).


# --- aggregates ------------------------------------------------------------

#: Any typed channel payload. Emitted by the ``global`` firehose.
AnyConfirmedPayload = (
    TradesPayload
    | OraclePayload
    | LifecyclePayload
    | ActivityPayload
    | CollateralPayload
    | CombosPayload
)

#: Any payload deliverable on an event frame, including price ticks.
AnyChannelPayload = AnyConfirmedPayload | PricesPayload
