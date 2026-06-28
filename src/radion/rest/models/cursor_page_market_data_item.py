from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CursorPageMarketDataItem")


@_attrs_define
class CursorPageMarketDataItem:
    """
    Attributes:
        condition_id (str):
        last_price (str):
        open_interest (str):
        total_volume (str):
        trade_count (int):
        updated_block (int):
        last_trade_ts (None | str | Unset):
    """

    condition_id: str
    last_price: str
    open_interest: str
    total_volume: str
    trade_count: int
    updated_block: int
    last_trade_ts: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition_id = self.condition_id

        last_price = self.last_price

        open_interest = self.open_interest

        total_volume = self.total_volume

        trade_count = self.trade_count

        updated_block = self.updated_block

        last_trade_ts: None | str | Unset
        if isinstance(self.last_trade_ts, Unset):
            last_trade_ts = UNSET
        else:
            last_trade_ts = self.last_trade_ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditionId": condition_id,
                "lastPrice": last_price,
                "openInterest": open_interest,
                "totalVolume": total_volume,
                "tradeCount": trade_count,
                "updatedBlock": updated_block,
            }
        )
        if last_trade_ts is not UNSET:
            field_dict["lastTradeTs"] = last_trade_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        condition_id = d.pop("conditionId")

        last_price = d.pop("lastPrice")

        open_interest = d.pop("openInterest")

        total_volume = d.pop("totalVolume")

        trade_count = d.pop("tradeCount")

        updated_block = d.pop("updatedBlock")

        def _parse_last_trade_ts(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_trade_ts = _parse_last_trade_ts(d.pop("lastTradeTs", UNSET))

        cursor_page_market_data_item = cls(
            condition_id=condition_id,
            last_price=last_price,
            open_interest=open_interest,
            total_volume=total_volume,
            trade_count=trade_count,
            updated_block=updated_block,
            last_trade_ts=last_trade_ts,
        )

        cursor_page_market_data_item.additional_properties = d
        return cursor_page_market_data_item

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
