from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_key_plan import ApiKeyPlan
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_summary import KeySummary
    from ..models.monthly_usage import MonthlyUsage


T = TypeVar("T", bound="ListKeysResponse")


@_attrs_define
class ListKeysResponse:
    """
    Attributes:
        data (list[KeySummary]):
        monthly_usage (MonthlyUsage):
        plan (ApiKeyPlan):
        trial_ends_at (datetime.datetime | None | Unset):
    """

    data: list[KeySummary]
    monthly_usage: MonthlyUsage
    plan: ApiKeyPlan
    trial_ends_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        monthly_usage = self.monthly_usage.to_dict()

        plan = self.plan.value

        trial_ends_at: None | str | Unset
        if isinstance(self.trial_ends_at, Unset):
            trial_ends_at = UNSET
        elif isinstance(self.trial_ends_at, datetime.datetime):
            trial_ends_at = self.trial_ends_at.isoformat()
        else:
            trial_ends_at = self.trial_ends_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "monthlyUsage": monthly_usage,
                "plan": plan,
            }
        )
        if trial_ends_at is not UNSET:
            field_dict["trialEndsAt"] = trial_ends_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_summary import KeySummary
        from ..models.monthly_usage import MonthlyUsage

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = KeySummary.from_dict(data_item_data)

            data.append(data_item)

        monthly_usage = MonthlyUsage.from_dict(d.pop("monthlyUsage"))

        plan = ApiKeyPlan(d.pop("plan"))

        def _parse_trial_ends_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trial_ends_at_type_0 = datetime.datetime.fromisoformat(data)

                return trial_ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        trial_ends_at = _parse_trial_ends_at(d.pop("trialEndsAt", UNSET))

        list_keys_response = cls(
            data=data,
            monthly_usage=monthly_usage,
            plan=plan,
            trial_ends_at=trial_ends_at,
        )

        list_keys_response.additional_properties = d
        return list_keys_response

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
