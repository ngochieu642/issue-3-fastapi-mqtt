# Behavior

## Environment

- Linux: Ubuntu 20
- Docker: python:3.7-stretch

## Test on local

### 1. Run run.py directly

- Raise Error as below

```bash
python run.py

ERROR:    Traceback (most recent call last):
  File "/home/coder/.pyenv/versions/3.7.8/envs/webdev/lib/python3.7/site-packages/starlette/routing.py", line 526, in lifespan
    async for item in self.lifespan_context(app):
  File "/home/coder/.pyenv/versions/3.7.8/envs/webdev/lib/python3.7/site-packages/starlette/routing.py", line 467, in default_lifespan
    await self.startup()
  File "/home/coder/.pyenv/versions/3.7.8/envs/webdev/lib/python3.7/site-packages/starlette/routing.py", line 502, in startup
    await handler()
  File "/home/coder/Data/Programming/Language/Python/projects/fastapi-mqtt-dev/app/main.py", line 13, in startapp
    await mqtt.connection()
  File "/home/coder/.pyenv/versions/3.7.8/envs/webdev/lib/python3.7/site-packages/fastapi_mqtt/fastmqtt.py", line 130, in connection
    await self.client.connect(self.client._host,self.client._port,self.client._ssl,self.client._keepalive,version)
  File "/home/coder/.pyenv/versions/3.7.8/envs/webdev/lib/python3.7/site-packages/gmqtt/client.py", line 165, in connect
    await self._connected.wait()
  File "/home/coder/.pyenv/versions/3.7.8/lib/python3.7/asyncio/locks.py", line 293, in wait
    await fut
RuntimeError: Task <Task pending coro=<LifespanOn.main() running at /home/coder/.pyenv/versions/3.7.8/envs/webdev/lib/python3.7/site-packages/uvicorn/lifespan/on.py:55>> got Future <Future pending> attached to a different loop
```

### 2. Start uvicorn inside app

```
cd app
uvicorn main:app --reload
```

- Work as expected:
  - Connected to Broker
  - Receive messages

## Test inside docker

1. Run run.py
```bash
make local-fail
docker logs -f api-mqtt-fail
```

2. Run uvicorn directly with app
```bash
make local-work
docker logs -f api-mqtt-work
```