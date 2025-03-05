#rymme
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Due to Koyeb's free hobby plan restrictions, the bot will sleep if inactive for an hour. The only way to wake it up is by visiting this link. Sorry for the inconvenience caused")
