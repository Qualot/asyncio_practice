#!/usr/bin/env python3
import asyncio

async def nested():
    return 42

async def main():
    #Nothing happens. Coroutine is created
    nested()

    #runs
    print(await nested())

asyncio.run(main())