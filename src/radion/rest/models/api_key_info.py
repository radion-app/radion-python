from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_key_plan import ApiKeyPlan
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monthly_usage import MonthlyUsage


T = TypeVar("T", bound="ApiKeyInfo")


@_attrs_define
class ApiKeyInfo:
    """
    Attributes:
        call_count (int):
        created_at (datetime.datetime):
        key_label (str):
        monthly_usage (MonthlyUsage):
        plan (ApiKeyPlan):
        requests_per_second (int):
        expires_at (datetime.datetime | None | Unset):
        last_used_at (datetime.datetime | None | Unset):
    """

    call_count: int
    created_at: datetime.datetime
    key_label: str
    monthly_usage: MonthlyUsage
    plan: ApiKeyPlan
    requests_per_second: int
    expires_at: datetime.datetime | None | Unset = UNSET
    last_used_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_count = self.call_count

        created_at = self.created_at.isoformat()

        key_label = self.key_label

        monthly_usage = self.monthly_usage.to_dict()

        plan = self.plan.value

        requests_per_second = self.requests_per_second

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        last_used_at: None | str | Unset
        if isinstance(self.last_used_at, Unset):
            last_used_at = UNSET
        elif isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "callCount": call_count,
                "createdAt": created_at,
                "keyLabel": key_label,
                "monthlyUsage": monthly_usage,
                "plan": plan,
                "requestsPerSecond": requests_per_second,
            }
        )
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if last_used_at is not UNSET:
            field_dict["lastUsedAt"] = last_used_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monthly_usage import MonthlyUsage

        d = dict(src_dict)
        call_count = d.pop("callCount")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        key_label = d.pop("keyLabel")

        monthly_usage = MonthlyUsage.from_dict(d.pop("monthlyUsage"))

        plan = ApiKeyPlan(d.pop("plan"))

        requests_per_second = d.pop("requestsPerSecond")

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))

        def _parse_last_used_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_used_at = _parse_last_used_at(d.pop("lastUsedAt", UNSET))

        api_key_info = cls(
            call_count=call_count,
            created_at=created_at,
            key_label=key_label,
            monthly_usage=monthly_usage,
            plan=plan,
            requests_per_second=requests_per_second,
            expires_at=expires_at,
            last_used_at=last_used_at,
        )

        api_key_info.additional_properties = d
        return api_key_info

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
