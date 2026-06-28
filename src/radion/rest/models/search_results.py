from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.market import Market
    from ..models.trader_pnl import TraderPnl


T = TypeVar("T", bound="SearchResults")


@_attrs_define
class SearchResults:
    """
    Attributes:
        markets (list[Market]):
        traders (list[TraderPnl]):
    """

    markets: list[Market]
    traders: list[TraderPnl]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        markets = []
        for markets_item_data in self.markets:
            markets_item = markets_item_data.to_dict()
            markets.append(markets_item)

        traders = []
        for traders_item_data in self.traders:
            traders_item = traders_item_data.to_dict()
            traders.append(traders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "markets": markets,
                "traders": traders,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market import Market
        from ..models.trader_pnl import TraderPnl

        d = dict(src_dict)
        markets = []
        _markets = d.pop("markets")
        for markets_item_data in _markets:
            markets_item = Market.from_dict(markets_item_data)

            markets.append(markets_item)

        traders = []
        _traders = d.pop("traders")
        for traders_item_data in _traders:
            traders_item = TraderPnl.from_dict(traders_item_data)

            traders.append(traders_item)

        search_results = cls(
            markets=markets,
            traders=traders,
        )

        search_results.additional_properties = d
        return search_results

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
