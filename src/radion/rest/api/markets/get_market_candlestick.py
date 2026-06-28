from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.candlestick_response import CandlestickResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    condition_id: str,
    *,
    resolution: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["resolution"] = resolution

    params["from"] = from_

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/polymarket/markets/{condition_id}/candlestick".format(
            condition_id=quote(str(condition_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CandlestickResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = CandlestickResponse.from_dict(response.json())

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
) -> Response[CandlestickResponse | ErrorResponse]:
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
    resolution: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
) -> Response[CandlestickResponse | ErrorResponse]:
    """OHLC candlesticks for a market

    Args:
        condition_id (str):
        resolution (str | Unset):
        from_ (int | Unset):
        to (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CandlestickResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        condition_id=condition_id,
        resolution=resolution,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    condition_id: str,
    *,
    client: AuthenticatedClient | Client,
    resolution: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
) -> CandlestickResponse | ErrorResponse | None:
    """OHLC candlesticks for a market

    Args:
        condition_id (str):
        resolution (str | Unset):
        from_ (int | Unset):
        to (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CandlestickResponse | ErrorResponse
    """

    return sync_detailed(
        condition_id=condition_id,
        client=client,
        resolution=resolution,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    condition_id: str,
    *,
    client: AuthenticatedClient | Client,
    resolution: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
) -> Response[CandlestickResponse | ErrorResponse]:
    """OHLC candlesticks for a market

    Args:
        condition_id (str):
        resolution (str | Unset):
        from_ (int | Unset):
        to (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CandlestickResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        condition_id=condition_id,
        resolution=resolution,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    condition_id: str,
    *,
    client: AuthenticatedClient | Client,
    resolution: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
) -> CandlestickResponse | ErrorResponse | None:
    """OHLC candlesticks for a market

    Args:
        condition_id (str):
        resolution (str | Unset):
        from_ (int | Unset):
        to (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CandlestickResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            condition_id=condition_id,
            client=client,
            resolution=resolution,
            from_=from_,
            to=to,
        )
    ).parsed
