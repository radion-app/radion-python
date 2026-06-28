from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cursor_page_trade import CursorPageTrade
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    condition_id: str,
    *,
    side: int | Unset = UNSET,
    outcome: int | Unset = UNSET,
    trader: str | Unset = UNSET,
    min_usd: int | Unset = UNSET,
    max_usd: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["side"] = side

    params["outcome"] = outcome

    params["trader"] = trader

    params["min_usd"] = min_usd

    params["max_usd"] = max_usd

    params["from"] = from_

    params["to"] = to

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/polymarket/markets/{condition_id}/trades".format(
            condition_id=quote(str(condition_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CursorPageTrade | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = CursorPageTrade.from_dict(response.json())

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
) -> Response[CursorPageTrade | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    condition_id: str,
    *,
    client: AuthenticatedClient | Client,
    side: int | Unset = UNSET,
    outcome: int | Unset = UNSET,
    trader: str | Unset = UNSET,
    min_usd: int | Unset = UNSET,
    max_usd: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[CursorPageTrade | ErrorResponse]:
    """List trades for a market

    Args:
        condition_id (str):
        side (int | Unset):
        outcome (int | Unset):
        trader (str | Unset):
        min_usd (int | Unset):
        max_usd (int | Unset):
        from_ (int | Unset):
        to (int | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CursorPageTrade | ErrorResponse]
    """

    kwargs = _get_kwargs(
        condition_id=condition_id,
        side=side,
        outcome=outcome,
        trader=trader,
        min_usd=min_usd,
        max_usd=max_usd,
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    condition_id: str,
    *,
    client: AuthenticatedClient | Client,
    side: int | Unset = UNSET,
    outcome: int | Unset = UNSET,
    trader: str | Unset = UNSET,
    min_usd: int | Unset = UNSET,
    max_usd: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> CursorPageTrade | ErrorResponse | None:
    """List trades for a market

    Args:
        condition_id (str):
        side (int | Unset):
        outcome (int | Unset):
        trader (str | Unset):
        min_usd (int | Unset):
        max_usd (int | Unset):
        from_ (int | Unset):
        to (int | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CursorPageTrade | ErrorResponse
    """

    return sync_detailed(
        condition_id=condition_id,
        client=client,
        side=side,
        outcome=outcome,
        trader=trader,
        min_usd=min_usd,
        max_usd=max_usd,
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    condition_id: str,
    *,
    client: AuthenticatedClient | Client,
    side: int | Unset = UNSET,
    outcome: int | Unset = UNSET,
    trader: str | Unset = UNSET,
    min_usd: int | Unset = UNSET,
    max_usd: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[CursorPageTrade | ErrorResponse]:
    """List trades for a market

    Args:
        condition_id (str):
        side (int | Unset):
        outcome (int | Unset):
        trader (str | Unset):
        min_usd (int | Unset):
        max_usd (int | Unset):
        from_ (int | Unset):
        to (int | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CursorPageTrade | ErrorResponse]
    """

    kwargs = _get_kwargs(
        condition_id=condition_id,
        side=side,
        outcome=outcome,
        trader=trader,
        min_usd=min_usd,
        max_usd=max_usd,
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    condition_id: str,
    *,
    client: AuthenticatedClient | Client,
    side: int | Unset = UNSET,
    outcome: int | Unset = UNSET,
    trader: str | Unset = UNSET,
    min_usd: int | Unset = UNSET,
    max_usd: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> CursorPageTrade | ErrorResponse | None:
    """List trades for a market

    Args:
        condition_id (str):
        side (int | Unset):
        outcome (int | Unset):
        trader (str | Unset):
        min_usd (int | Unset):
        max_usd (int | Unset):
        from_ (int | Unset):
        to (int | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CursorPageTrade | ErrorResponse
    """

    return (
        await asyncio_detailed(
            condition_id=condition_id,
            client=client,
            side=side,
            outcome=outcome,
            trader=trader,
            min_usd=min_usd,
            max_usd=max_usd,
            from_=from_,
            to=to,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
