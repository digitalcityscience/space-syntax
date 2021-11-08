# Copyright (c) Alex Ellis 2017. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import sys
import asyncio
from function import handler

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
    loop = asyncio.get_event_loop()
    ret = loop.run_until_complete(handler.handle(st))    
    if ret !=None:
        print(ret)
