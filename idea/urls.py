from django.urls import path, include

from .views import IdeaView

app_name = 'idea'

urlpatterns = [
    path('', IdeaView.as_view(), name='idea')
]
