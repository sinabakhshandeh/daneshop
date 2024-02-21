import logging
from typing import List

from ninja import Router

from blog.api import schemas

blog_router = Router()
logger = logging.getLogger(__name__)


@blog_router.get(
    "",
    response={200: List[schemas.ErrorSchema], 401: schemas.ErrorSchema},
)
def post_list_view(request):
    return [{"message": "test"}]
