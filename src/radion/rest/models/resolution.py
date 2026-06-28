from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Resolution")


@_attrs_define
class Resolution:
    """
    Attributes:
        condition_id (str):
        payout_numerators (list[int]):
        resolution_source (int):
        resolved_ts (str):
    """

    condition_id: str
    payout_numerators: list[int]
    resolution_source: int
    resolved_ts: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition_id = self.condition_id

        payout_numerators = self.payout_numerators

        resolution_source = self.resolution_source

        resolved_ts = self.resolved_ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditionId": condition_id,
                "payoutNumerators": payout_numerators,
                "resolutionSource": resolution_source,
                "resolvedTs": resolved_ts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        condition_id = d.pop("conditionId")

        payout_numerators = cast(list[int], d.pop("payoutNumerators"))

        resolution_source = d.pop("resolutionSource")

        resolved_ts = d.pop("resolvedTs")

        resolution = cls(
            condition_id=condition_id,
            payout_numerators=payout_numerators,
            resolution_source=resolution_source,
            resolved_ts=resolved_ts,
        )

        resolution.additional_properties = d
        return resolution

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
