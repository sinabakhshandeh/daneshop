from ninja import NinjaAPI

from blog.api.views import blog_router

api = NinjaAPI(
    # auth=AuthBearer(),
)

api.add_router("blog/", blog_router, tags=["blog"])
