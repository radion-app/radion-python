# radion-sdk

[![PyPI version](https://img.shields.io/pypi/v/radion-sdk.svg)](https://pypi.org/project/radion-sdk/)
[![Python versions](https://img.shields.io/pypi/pyversions/radion-sdk.svg)](https://pypi.org/project/radion-sdk/)
[![license](https://img.shields.io/pypi/l/radion-sdk.svg)](./LICENSE)

Official, async-first, fully-typed SDK for the [Radion](https://radion.app) platform.

One client, one API key, every Radion product surface. Install `radion-sdk`; import it as `radion`.

```python
radion = Radion(api_key=os.getenv("RADION_API_KEY"))
await radion.realtime.connect()
await radion.realtime.subscribe(Subscription(id="trades", channel="trades"))

@radion.realtime.on_channel("trades")
async def handle_trade(event):
    print(event.id, event.data)
```

## Features

- **Unified client** — `Radion(api_key=...)` is the single entry point for every product surface
- **Auto-reconnect** — exponential backoff with jitter; stops on graceful shutdown
- **Subscription restore** — active channels are re-subscribed after every reconnect
- **Heartbeats** — ping/pong keep-alive that detects stale connections and reconnects
- **Typed end-to-end** — channel names, frame models, and errors
- **Async-first** — built on `asyncio`; handlers may be sync or async

## Requirements

- Python >= 3.10

## Install

```bash
uv add radion-sdk
# or: pip install radion-sdk
```

## Quick start

```python
import asyncio
import os

from radion import Radion, Subscription


async def main() -> None:
    radion = Radion(api_key=os.getenv("RADION_API_KEY"))

    await radion.realtime.connect()
    await radion.realtime.subscribe(Subscription(id="trades", channel="trades"))

    @radion.realtime.on_channel("trades")
    async def handle_trade(event):
        print(event.id, event.channel, event.data)

    await asyncio.sleep(60)
    await radion.realtime.close()


asyncio.run(main())
```

## Usage

### Configuration

```python
Radion(api_key, *, base_url=..., ws_url=..., reconnect=True, heartbeat=True,
       heartbeat_interval=15.0, heartbeat_timeout=10.0)
```

| Argument             | Type    | Default                   | Description                                       |
| -------------------- | ------- | ------------------------- | ------------------------------------------------- |
| `api_key`            | `str`   | —                         | **Required.** Sent as the `X-API-Key` header.     |
| `base_url`           | `str`   | `https://api.radion.app`  | Base URL for the Radion API.                      |
| `ws_url`             | `str`   | `wss://api.radion.app/ws` | Override the realtime endpoint.                   |
| `reconnect`          | `bool`  | `True`                    | Auto-reconnect on unexpected disconnect.          |
| `heartbeat`          | `bool`  | `True`                    | Enable heartbeats / stale detection.              |
| `heartbeat_interval` | `float` | `15.0`                    | Seconds between pings.                            |
| `heartbeat_timeout`  | `float` | `10.0`                    | Extra grace before a quiet connection is stale.   |

Extra keyword arguments are forwarded to the realtime client.

### Realtime client

`radion.realtime` is a `RealtimeClient`. It can also be imported and
constructed standalone:

```python
from radion import RealtimeClient

client = RealtimeClient(api_key=os.getenv("RADION_API_KEY"))
```

| Method                              | Description                                                  |
| ----------------------------------- | ------------------------------------------------------------ |
| `await connect()`                   | Open the connection. Resolves once established.             |
| `await subscribe(subscription)`     | Subscribe with `Subscription(id, channel, filters)`. Replayed on reconnect.|
| `await unsubscribe(id)`             | Unsubscribe by subscription id.                             |
| `on_channel(channel)`               | Decorator for a specific channel handler (incl. `mempool.` channels). |
| `off_channel(channel, handler=None)`| Remove a channel handler (or all for that channel).         |
| `on_any_channel()`                  | Decorator for a wildcard handler — every channel event.     |
| `off_any_channel(handler=None)`     | Remove a wildcard handler (or all of them).                 |
| `on_lifecycle(event)`               | Decorator for a lifecycle handler: `open`, `close`, `reconnect`, `error`. |
| `off_lifecycle(event, handler=None)`| Remove a lifecycle handler (or all for that event).         |
| `await close(code=1000, ...)`       | Graceful shutdown. Stops reconnect attempts.                |
| `connected`                         | Property — whether the socket is currently open.            |

### Subscriptions & filters

A subscription is `Subscription(id, channel, filters=None)`. The `id` is your
own string, echoed back on every event so you can tell subscriptions apart;
`channel` may carry a `mempool.` prefix. Some channels require a filter:

```python
from radion import ChannelFilters, Subscription

await radion.realtime.subscribe(
    Subscription(id="whales", channel="large_trades", filters=ChannelFilters(min_usd=10_000))
)

# on_any_channel fires for every channel; the event carries id + channel + data.
@radion.realtime.on_any_channel()
async def on_any(event):
    print(event.id, event.channel, event.data)
```

`ChannelFilters`: `wallets`, `market_ids`, `token_ids`, `min_usd`.

### Channels

```
global · trades · activity · lifecycle · oracle · collateral
combos · prices · wallets · markets · large_trades
```

Available as the `CHANNELS` tuple and the `Channel` type.

```python
from radion import CHANNELS, Subscription

for channel in CHANNELS:
    await radion.realtime.subscribe(Subscription(id=channel, channel=channel))
```

### Lifecycle events

```python
@radion.realtime.on_lifecycle("open")
async def opened(_):
    print("connected")

@radion.realtime.on_lifecycle("close")
async def closed(info):
    print(info["code"], info["reason"])

@radion.realtime.on_lifecycle("reconnect")
async def reconnecting(info):
    print(info["attempt"], info["delay"])

@radion.realtime.on_lifecycle("error")
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
from radion import RadionConnectionError, RadionServerError

@radion.realtime.on_lifecycle("error")
async def errored(err):
    if isinstance(err, RadionServerError):
        print("server error", err.code, err.channel)
    elif isinstance(err, RadionConnectionError):
        print("connection error", err)
```

A throwing consumer handler is reported via the `error` event and never retried.

## License

MIT
