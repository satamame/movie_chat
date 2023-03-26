from django.urls import path, include

from .views import IdeaView

urlpatterns = [
    path('', IdeaView.as_view(), name='idea')
]
