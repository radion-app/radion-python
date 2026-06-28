from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CursorPagePositionDataItem")


@_attrs_define
class CursorPagePositionDataItem:
    """
    Attributes:
        amount (str):
        block_number (int):
        condition_id (str):
        kind (int):
        log_index (int):
        stakeholder (str):
        ts (str):
        tx_hash (str):
        collateral_token (None | str | Unset):
        parent_collection_id (None | str | Unset):
        position_id (None | str | Unset):
    """

    amount: str
    block_number: int
    condition_id: str
    kind: int
    log_index: int
    stakeholder: str
    ts: str
    tx_hash: str
    collateral_token: None | str | Unset = UNSET
    parent_collection_id: None | str | Unset = UNSET
    position_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        block_number = self.block_number

        condition_id = self.condition_id

        kind = self.kind

        log_index = self.log_index

        stakeholder = self.stakeholder

        ts = self.ts

        tx_hash = self.tx_hash

        collateral_token: None | str | Unset
        if isinstance(self.collateral_token, Unset):
            collateral_token = UNSET
        else:
            collateral_token = self.collateral_token

        parent_collection_id: None | str | Unset
        if isinstance(self.parent_collection_id, Unset):
            parent_collection_id = UNSET
        else:
            parent_collection_id = self.parent_collection_id

        position_id: None | str | Unset
        if isinstance(self.position_id, Unset):
            position_id = UNSET
        else:
            position_id = self.position_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "blockNumber": block_number,
                "conditionId": condition_id,
                "kind": kind,
                "logIndex": log_index,
                "stakeholder": stakeholder,
                "ts": ts,
                "txHash": tx_hash,
            }
        )
        if collateral_token is not UNSET:
            field_dict["collateralToken"] = collateral_token
        if parent_collection_id is not UNSET:
            field_dict["parentCollectionId"] = parent_collection_id
        if position_id is not UNSET:
            field_dict["positionId"] = position_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        block_number = d.pop("blockNumber")

        condition_id = d.pop("conditionId")

        kind = d.pop("kind")

        log_index = d.pop("logIndex")

        stakeholder = d.pop("stakeholder")

        ts = d.pop("ts")

        tx_hash = d.pop("txHash")

        def _parse_collateral_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collateral_token = _parse_collateral_token(d.pop("collateralToken", UNSET))

        def _parse_parent_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_collection_id = _parse_parent_collection_id(
            d.pop("parentCollectionId", UNSET)
        )

        def _parse_position_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        position_id = _parse_position_id(d.pop("positionId", UNSET))

        cursor_page_position_data_item = cls(
            amount=amount,
            block_number=block_number,
            condition_id=condition_id,
            kind=kind,
            log_index=log_index,
            stakeholder=stakeholder,
            ts=ts,
            tx_hash=tx_hash,
            collateral_token=collateral_token,
            parent_collection_id=parent_collection_id,
            position_id=position_id,
        )

        cursor_page_position_data_item.additional_properties = d
        return cursor_page_position_data_item

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
