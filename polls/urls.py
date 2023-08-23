from django.urls import path

from .views import *


urlpatterns = [
    path("", IndexView.as_view(), name="polls"),
    path("<int:pk>/", DetailPollView.as_view(), name="detail"),
    path("<int:pk>/results/", ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),
    path('addpoll/', AddQuest.as_view(), name='add_quest'),
    # path("<int:question_id>/add_choice/", AddChoice.as_view(), name='add_choice'),
]

# urlpatterns = [
#     path('', index, name='index'),
#     path("<int:question_id>/", detail, name="detail"),
#     path("<int:question_id>/results/", results, name="results"),
#     path("<int:question_id>/vote/", vote, name="vote"),
# ]
