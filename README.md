# radion-ws

[![PyPI version](https://img.shields.io/pypi/v/radion-ws.svg)](https://pypi.org/project/radion-ws/)
[![Python versions](https://img.shields.io/pypi/pyversions/radion-ws.svg)](https://pypi.org/project/radion-ws/)
[![license](https://img.shields.io/pypi/l/radion-ws.svg)](./LICENSE)

Async-first, fully-typed WebSocket SDK for the [Radion](https://radion.app) realtime API.

```python
client = RadionWS(api_key=os.getenv("RADION_API_KEY"))
await client.connect()
await client.subscribe("trades")

@client.on("trades")
async def handle_trade(event):
    print(event.data)
```

## Features

- **Connection lifecycle** — `connect()` / `subscribe()` / `unsubscribe()` / `close()`
- **Auto-reconnect** — exponential backoff with jitter; stops on graceful shutdown
- **Subscription restore** — active channels are re-subscribed after every reconnect
- **Heartbeats** — ping/pong keep-alive that detects stale connections and reconnects
- **Typed end-to-end** — channel names, frame models, and errors
- **Async-first** — built on `asyncio`; handlers may be sync or async

## Requirements

- Python >= 3.10

## Install

```bash
uv add radion-ws
# or: pip install radion-ws
```

## Quick start

```python
import asyncio
import os

from radion_ws import RadionWS


async def main() -> None:
    client = RadionWS(api_key=os.getenv("RADION_API_KEY"))

    await client.connect()
    await client.subscribe("trades")

    @client.on("trades")
    async def handle_trade(event):
        print(event.channel, event.data)

    await asyncio.sleep(60)
    await client.close()


asyncio.run(main())
```

## Usage

### Configuration

```python
RadionWS(api_key, *, url=..., reconnect=True, heartbeat=True,
         heartbeat_interval=15.0, heartbeat_timeout=10.0)
```

| Argument             | Type    | Default                   | Description                                       |
| -------------------- | ------- | ------------------------- | ------------------------------------------------- |
| `api_key`            | `str`   | —                         | **Required.** Sent as the `X-API-Key` header.     |
| `url`                | `str`   | `wss://api.radion.app/ws` | Override the endpoint.                            |
| `reconnect`          | `bool`  | `True`                    | Auto-reconnect on unexpected disconnect.          |
| `heartbeat`          | `bool`  | `True`                    | Enable heartbeats / stale detection.              |
| `heartbeat_interval` | `float` | `15.0`                    | Seconds between pings.                            |
| `heartbeat_timeout`  | `float` | `10.0`                    | Extra grace before a quiet connection is stale.   |

### Methods

| Method                          | Description                                                  |
| ------------------------------- | ------------------------------------------------------------ |
| `await connect()`               | Open the connection. Resolves once established.             |
| `await subscribe(channel)`      | Subscribe to a channel. Replayed automatically on reconnect.|
| `await unsubscribe(channel)`    | Unsubscribe from a channel.                                 |
| `on(event)`                     | Decorator registering a channel or lifecycle handler.       |
| `off(event, handler=None)`      | Remove a handler (or all for that event).                   |
| `await close(code=1000, ...)`   | Graceful shutdown. Stops reconnect attempts.                |
| `connected`                     | Property — whether the socket is currently open.            |

### Channels

```
global · trades · activity · lifecycle · oracle · collateral
combos · prices · wallets · markets · large_trades
```

Available as the `CHANNELS` tuple and the `Channel` type.

```python
from radion_ws import CHANNELS

for channel in CHANNELS:
    await client.subscribe(channel)
```

### Lifecycle events

```python
@client.on("open")
async def opened(_):
    print("connected")

@client.on("close")
async def closed(info):
    print(info["code"], info["reason"])

@client.on("reconnect")
async def reconnecting(info):
    print(info["attempt"], info["delay"])

@client.on("error")
async def errored(err):
    print(err)
```

### Reconnect & subscription restore

On an unexpected disconnect the client reconnects with exponential backoff and
re-sends every active subscription once the socket reopens. After `close()` no
further attempts run.

### Heartbeats

A ping is sent every `heartbeat_interval` seconds. Any inbound frame counts as
liveness; if the connection goes quiet past the timeout window it is terminated
and reconnected.

### Error handling

```python
from radion_ws import RadionConnectionError, RadionServerError

@client.on("error")
async def errored(err):
    if isinstance(err, RadionServerError):
        print("server error", err.code, err.channel)
    elif isinstance(err, RadionConnectionError):
        print("connection error", err)
```

A throwing consumer handler is reported via the `error` event and never retried.

## License

MIT
