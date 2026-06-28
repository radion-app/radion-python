from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.outcome import Outcome


T = TypeVar("T", bound="MarketBySlug")


@_attrs_define
class MarketBySlug:
    """
    Attributes:
        id (str):
        outcomes (list[Outcome]):
        status (str):
        description (None | str | Unset):
        end_date (int | None | Unset):
        question (None | str | Unset):
        slug (None | str | Unset):
        start_date (int | None | Unset):
    """

    id: str
    outcomes: list[Outcome]
    status: str
    description: None | str | Unset = UNSET
    end_date: int | None | Unset = UNSET
    question: None | str | Unset = UNSET
    slug: None | str | Unset = UNSET
    start_date: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        outcomes = []
        for outcomes_item_data in self.outcomes:
            outcomes_item = outcomes_item_data.to_dict()
            outcomes.append(outcomes_item)

        status = self.status

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

        question: None | str | Unset
        if isinstance(self.question, Unset):
            question = UNSET
        else:
            question = self.question

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "outcomes": outcomes,
                "status": status,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if question is not UNSET:
            field_dict["question"] = question
        if slug is not UNSET:
            field_dict["slug"] = slug
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.outcome import Outcome

        d = dict(src_dict)
        id = d.pop("id")

        outcomes = []
        _outcomes = d.pop("outcomes")
        for outcomes_item_data in _outcomes:
            outcomes_item = Outcome.from_dict(outcomes_item_data)

            outcomes.append(outcomes_item)

        status = d.pop("status")

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

        def _parse_question(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        question = _parse_question(d.pop("question", UNSET))

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

        market_by_slug = cls(
            id=id,
            outcomes=outcomes,
            status=status,
            description=description,
            end_date=end_date,
            question=question,
            slug=slug,
            start_date=start_date,
        )

        market_by_slug.additional_properties = d
        return market_by_slug

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
