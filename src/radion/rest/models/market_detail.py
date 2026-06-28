from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.market import Market
    from ..models.resolution import Resolution


T = TypeVar("T", bound="MarketDetail")


@_attrs_define
class MarketDetail:
    """
    Attributes:
        market (Market):
        resolution (None | Resolution | Unset):
    """

    market: Market
    resolution: None | Resolution | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resolution import Resolution

        market = self.market.to_dict()

        resolution: dict[str, Any] | None | Unset
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        elif isinstance(self.resolution, Resolution):
            resolution = self.resolution.to_dict()
        else:
            resolution = self.resolution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "market": market,
            }
        )
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market import Market
        from ..models.resolution import Resolution

        d = dict(src_dict)
        market = Market.from_dict(d.pop("market"))

        def _parse_resolution(data: object) -> None | Resolution | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resolution_type_1 = Resolution.from_dict(data)

                return resolution_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Resolution | Unset, data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        market_detail = cls(
            market=market,
            resolution=resolution,
        )

        market_detail.additional_properties = d
        return market_detail

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
