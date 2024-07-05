from django.urls import path
from .views import learn_poem, poem_detail

app_name = 'poem'
urlpatterns = [
    path('', learn_poem, name='learn_poem'),
    path('poem_detail/<int:poem_post_id>/', poem_detail, name='poem_detail'),  # <int:poem_post_id> 추가
]
