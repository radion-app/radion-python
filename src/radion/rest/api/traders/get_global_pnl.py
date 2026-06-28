from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cursor_page_trader_pnl import CursorPageTraderPnl
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sort_by: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sort_by"] = sort_by

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/polymarket/traders/global-pnl",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CursorPageTraderPnl | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = CursorPageTraderPnl.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CursorPageTraderPnl | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    sort_by: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[CursorPageTraderPnl | ErrorResponse]:
    """PnL leaderboard

    Args:
        sort_by (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CursorPageTraderPnl | ErrorResponse]
    """

    kwargs = _get_kwargs(
        sort_by=sort_by,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    sort_by: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> CursorPageTraderPnl | ErrorResponse | None:
    """PnL leaderboard

    Args:
        sort_by (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CursorPageTraderPnl | ErrorResponse
    """

    return sync_detailed(
        client=client,
        sort_by=sort_by,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    sort_by: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[CursorPageTraderPnl | ErrorResponse]:
    """PnL leaderboard

    Args:
        sort_by (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CursorPageTraderPnl | ErrorResponse]
    """

    kwargs = _get_kwargs(
        sort_by=sort_by,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    sort_by: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> CursorPageTraderPnl | ErrorResponse | None:
    """PnL leaderboard

    Args:
        sort_by (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CursorPageTraderPnl | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            sort_by=sort_by,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
