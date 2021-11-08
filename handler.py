from .main import process

async def handle(req: str):
    return await process(req)

