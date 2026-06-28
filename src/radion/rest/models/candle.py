from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Candle")


@_attrs_define
class Candle:
    """
    Attributes:
        c (str):
        h (str):
        l (str):
        o (str):
        t (int):
        v (str):
    """

    c: str
    h: str
    l: str
    o: str
    t: int
    v: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        c = self.c

        h = self.h

        l = self.l

        o = self.o

        t = self.t

        v = self.v

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "c": c,
                "h": h,
                "l": l,
                "o": o,
                "t": t,
                "v": v,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        c = d.pop("c")

        h = d.pop("h")

        l = d.pop("l")

        o = d.pop("o")

        t = d.pop("t")

        v = d.pop("v")

        candle = cls(
            c=c,
            h=h,
            l=l,
            o=o,
            t=t,
            v=v,
        )

        candle.additional_properties = d
        return candle

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
