# Copyright (c) Alex Ellis 2017. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import sys
import asyncio
from main import process

async def handle(req: str):
    print("handle: ", req)
    return await process(req)

def get_stdin():
    buf = ""
    while(True):
        line = sys.stdin.readline()
        buf += line
        if line=="":
            break
    return buf

if(__name__ == "__main__"):
    st = get_stdin()
    print("stdin: ", st)
    loop = asyncio.get_event_loop()
    ret = loop.run_until_complete(handle(st))    
    if ret !=None:
        print(ret)
