from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_key_info import ApiKeyInfo


T = TypeVar("T", bound="GetApiKeyInfoResponse")


@_attrs_define
class GetApiKeyInfoResponse:
    """
    Example:
        {'data': {'callCount': 42, 'createdAt': '2026-04-01T12:00:00Z', 'expiresAt': None, 'keyLabel':
            'production_read', 'lastUsedAt': '2026-04-09T15:20:00Z', 'monthlyUsage': {'limit': 3000, 'resetsAt':
            '2026-07-01T00:00:00Z', 'used': 120}, 'plan': 'starter', 'requestsPerSecond': 10}}

    Attributes:
        data (ApiKeyInfo):
    """

    data: ApiKeyInfo
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_info import ApiKeyInfo

        d = dict(src_dict)
        data = ApiKeyInfo.from_dict(d.pop("data"))

        get_api_key_info_response = cls(
            data=data,
        )

        get_api_key_info_response.additional_properties = d
        return get_api_key_info_response

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
