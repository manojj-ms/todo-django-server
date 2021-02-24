from django.conf.urls import url
from todo_app.endpoints import list

urlpatterns = [
    #GET, POST, DELETE
    url('tutorials', list.tutorial_list),

    #GET, PUT, DELETE
    url('tutorials/:id', list.tutorial_detail),

    #GET
    url('tutorials/published', list.tutorial_list_published),
]
