from django.conf.urls import url
from todo_app.endpoints import list

urlpatterns = [
    #GET, POST, DELETE
    url(r'^api/tutorials$', list.tutorial_list),

    #GET, PUT, DELETE
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', list.tutorial_detail),

    #GET
    url(r'^api/tutorials/published$', list.tutorial_list_published),
]
