from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CursorPageTradeDataItem")


@_attrs_define
class CursorPageTradeDataItem:
    """
    Attributes:
        block_number (int):
        chain_id (int):
        condition_id (str):
        fee (str):
        log_index (int):
        maker (str):
        outcome_index (int):
        position_id (str):
        price (str):
        side (int):
        size (str):
        taker (str):
        ts (str):
        tx_hash (str):
        usd (str):
        builder_code (None | str | Unset):
    """

    block_number: int
    chain_id: int
    condition_id: str
    fee: str
    log_index: int
    maker: str
    outcome_index: int
    position_id: str
    price: str
    side: int
    size: str
    taker: str
    ts: str
    tx_hash: str
    usd: str
    builder_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_number = self.block_number

        chain_id = self.chain_id

        condition_id = self.condition_id

        fee = self.fee

        log_index = self.log_index

        maker = self.maker

        outcome_index = self.outcome_index

        position_id = self.position_id

        price = self.price

        side = self.side

        size = self.size

        taker = self.taker

        ts = self.ts

        tx_hash = self.tx_hash

        usd = self.usd

        builder_code: None | str | Unset
        if isinstance(self.builder_code, Unset):
            builder_code = UNSET
        else:
            builder_code = self.builder_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blockNumber": block_number,
                "chainId": chain_id,
                "conditionId": condition_id,
                "fee": fee,
                "logIndex": log_index,
                "maker": maker,
                "outcomeIndex": outcome_index,
                "positionId": position_id,
                "price": price,
                "side": side,
                "size": size,
                "taker": taker,
                "ts": ts,
                "txHash": tx_hash,
                "usd": usd,
            }
        )
        if builder_code is not UNSET:
            field_dict["builderCode"] = builder_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block_number = d.pop("blockNumber")

        chain_id = d.pop("chainId")

        condition_id = d.pop("conditionId")

        fee = d.pop("fee")

        log_index = d.pop("logIndex")

        maker = d.pop("maker")

        outcome_index = d.pop("outcomeIndex")

        position_id = d.pop("positionId")

        price = d.pop("price")

        side = d.pop("side")

        size = d.pop("size")

        taker = d.pop("taker")

        ts = d.pop("ts")

        tx_hash = d.pop("txHash")

        usd = d.pop("usd")

        def _parse_builder_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        builder_code = _parse_builder_code(d.pop("builderCode", UNSET))

        cursor_page_trade_data_item = cls(
            block_number=block_number,
            chain_id=chain_id,
            condition_id=condition_id,
            fee=fee,
            log_index=log_index,
            maker=maker,
            outcome_index=outcome_index,
            position_id=position_id,
            price=price,
            side=side,
            size=size,
            taker=taker,
            ts=ts,
            tx_hash=tx_hash,
            usd=usd,
            builder_code=builder_code,
        )

        cursor_page_trade_data_item.additional_properties = d
        return cursor_page_trade_data_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
