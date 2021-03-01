from django.urls import path
from . import views

urlpatterns = [
    path('postMarks/', views.PostMarks.as_view()),
    path('leaderBoard/', views.LeaderBoard.as_view()),
    path('leaderBoardSearch/', views.leaderBoardSearch.as_view()),
]
