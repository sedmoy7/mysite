from django.db.models import Count
from polls.urls import urlpatterns
from .models import *

menu = [{'title': "Блог", 'url_name': 'home'},
        {'title': "Опросы", 'url_name': 'polls'},
        {'title': "Добавить пост", 'url_name': 'add_post'},
]


class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
        context['menu'] = user_menu
        return context
