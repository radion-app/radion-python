from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TraderPnl")


@_attrs_define
class TraderPnl:
    """
    Attributes:
        address (str):
        realized_pnl (str):
        trade_count (int):
        unrealized_pnl (str):
        updated_block (int):
        volume (str):
        win_count (int):
    """

    address: str
    realized_pnl: str
    trade_count: int
    unrealized_pnl: str
    updated_block: int
    volume: str
    win_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        realized_pnl = self.realized_pnl

        trade_count = self.trade_count

        unrealized_pnl = self.unrealized_pnl

        updated_block = self.updated_block

        volume = self.volume

        win_count = self.win_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "realizedPnl": realized_pnl,
                "tradeCount": trade_count,
                "unrealizedPnl": unrealized_pnl,
                "updatedBlock": updated_block,
                "volume": volume,
                "winCount": win_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        realized_pnl = d.pop("realizedPnl")

        trade_count = d.pop("tradeCount")

        unrealized_pnl = d.pop("unrealizedPnl")

        updated_block = d.pop("updatedBlock")

        volume = d.pop("volume")

        win_count = d.pop("winCount")

        trader_pnl = cls(
            address=address,
            realized_pnl=realized_pnl,
            trade_count=trade_count,
            unrealized_pnl=unrealized_pnl,
            updated_block=updated_block,
            volume=volume,
            win_count=win_count,
        )

        trader_pnl.additional_properties = d
        return trader_pnl

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
