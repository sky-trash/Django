from django.urls import path
from practic6.views import get_info, get_author, get_author_task, get_author_taskPublisher

urlpatterns = [
    path('main/', get_info),
    path('authors/', get_author),
    path('authorsTask/', get_author_task),
    path('authorsTaskPublisher/', get_author_taskPublisher),
]