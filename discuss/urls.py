from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('Discussion/<int:id>', view=views.detail, name='detail'),
    path('Discussion/Delete/<int:id>', view=views.delete, name='delete'),
    path('Discussion/Create', view=views.create, name='create'),
    path('Discussion/Update/<int:id>', view=views.update, name='update'),
    path('Discussion/Topic/<int:topic_pk>', view=views.getTopic, name='topic'),
]


