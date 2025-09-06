from django.urls import path
from .views import get_all_posts, get_post_by_id

urlpatterns = [
    path('', get_all_posts, name='all_posts'),
    path('<int:post_id>', get_post_by_id, name='post_by_id'),
]
