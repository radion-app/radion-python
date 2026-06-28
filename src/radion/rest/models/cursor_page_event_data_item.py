from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CursorPageEventDataItem")


@_attrs_define
class CursorPageEventDataItem:
    """
    Attributes:
        id (str):
        market_count (int):
        category (None | str | Unset):
        closed (bool | None | Unset):
        description (None | str | Unset):
        end_date (int | None | Unset):
        liquidity (float | None | Unset):
        open_interest (float | None | Unset):
        slug (None | str | Unset):
        start_date (int | None | Unset):
        title (None | str | Unset):
        volume (float | None | Unset):
    """

    id: str
    market_count: int
    category: None | str | Unset = UNSET
    closed: bool | None | Unset = UNSET
    description: None | str | Unset = UNSET
    end_date: int | None | Unset = UNSET
    liquidity: float | None | Unset = UNSET
    open_interest: float | None | Unset = UNSET
    slug: None | str | Unset = UNSET
    start_date: int | None | Unset = UNSET
    title: None | str | Unset = UNSET
    volume: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        market_count = self.market_count

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        closed: bool | None | Unset
        if isinstance(self.closed, Unset):
            closed = UNSET
        else:
            closed = self.closed

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        end_date: int | None | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        liquidity: float | None | Unset
        if isinstance(self.liquidity, Unset):
            liquidity = UNSET
        else:
            liquidity = self.liquidity

        open_interest: float | None | Unset
        if isinstance(self.open_interest, Unset):
            open_interest = UNSET
        else:
            open_interest = self.open_interest

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        start_date: int | None | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        volume: float | None | Unset
        if isinstance(self.volume, Unset):
            volume = UNSET
        else:
            volume = self.volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "marketCount": market_count,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if closed is not UNSET:
            field_dict["closed"] = closed
        if description is not UNSET:
            field_dict["description"] = description
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if liquidity is not UNSET:
            field_dict["liquidity"] = liquidity
        if open_interest is not UNSET:
            field_dict["openInterest"] = open_interest
        if slug is not UNSET:
            field_dict["slug"] = slug
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if title is not UNSET:
            field_dict["title"] = title
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        market_count = d.pop("marketCount")

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_closed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        closed = _parse_closed(d.pop("closed", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_end_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        def _parse_liquidity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        liquidity = _parse_liquidity(d.pop("liquidity", UNSET))

        def _parse_open_interest(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        open_interest = _parse_open_interest(d.pop("openInterest", UNSET))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_start_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_volume(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        volume = _parse_volume(d.pop("volume", UNSET))

        cursor_page_event_data_item = cls(
            id=id,
            market_count=market_count,
            category=category,
            closed=closed,
            description=description,
            end_date=end_date,
            liquidity=liquidity,
            open_interest=open_interest,
            slug=slug,
            start_date=start_date,
            title=title,
            volume=volume,
        )

        cursor_page_event_data_item.additional_properties = d
        return cursor_page_event_data_item

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
