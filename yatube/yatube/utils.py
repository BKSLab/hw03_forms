from django.conf import settings
from django.core.paginator import Paginator


def paginate(request, posts, post_per_one_page=settings.OBJECTS_PER_PAGE):
    paginator = Paginator(posts, post_per_one_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
