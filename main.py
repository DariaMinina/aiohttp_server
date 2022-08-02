from aiohttp import web
import jinja2
import aiohttp_jinja2

from app.settings import config, BASE_DIR


def setup_config(app: web.Application):
    app["config"] = config


def setup_routes(app: web.Application) -> None:
    from app.forum.routes import setup_routes as setup_forum_routes
    setup_forum_routes(app)


def setup_external_libraries(app: web.Application) -> None:
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(f"{BASE_DIR}/templates")
    )


def setup_app(app: web.Application) -> None:
    setup_config(app)
    setup_external_libraries(app)
    setup_routes(app)


app = web.Application()


if __name__ == "__main__":
    setup_app(app)
    web.run_app(app, port=config["common"]["port"])


