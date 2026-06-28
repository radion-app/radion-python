from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_key_response import DeleteKeyResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    key_label: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/auth/keys/{key_label}".format(
            key_label=quote(str(key_label), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteKeyResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DeleteKeyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteKeyResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_label: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteKeyResponse | ErrorResponse]:
    """Delete an API key

    Args:
        key_label (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteKeyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        key_label=key_label,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_label: str,
    *,
    client: AuthenticatedClient,
) -> DeleteKeyResponse | ErrorResponse | None:
    """Delete an API key

    Args:
        key_label (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteKeyResponse | ErrorResponse
    """

    return sync_detailed(
        key_label=key_label,
        client=client,
    ).parsed


async def asyncio_detailed(
    key_label: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteKeyResponse | ErrorResponse]:
    """Delete an API key

    Args:
        key_label (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteKeyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        key_label=key_label,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_label: str,
    *,
    client: AuthenticatedClient,
) -> DeleteKeyResponse | ErrorResponse | None:
    """Delete an API key

    Args:
        key_label (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteKeyResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            key_label=key_label,
            client=client,
        )
    ).parsed
