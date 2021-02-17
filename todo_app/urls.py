from django.urls import path
from todo_app.endpoints import list

urlpatterns = [
    #GET, POST, DELETE
    path('/api/tutorials', list.tutorial_detail),

    #GET, PUT, DELETE
    path('/api/tutorials/:id', list.tutorial_detail),

    #GET
    path('/api/tutorials/published', list.tutorial_detail),
]
