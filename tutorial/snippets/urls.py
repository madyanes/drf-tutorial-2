from django.urls import include, path
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

snippet_list = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
})

user_list = views.UserViewSet.as_view({
    'get': 'list'
})

user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    # path('snippets/', snippet_list, name='snippet-list'),
    # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    # path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    # path('users/', user_list, name='user-list'),
    # path('users/<int:pk>', user_detail, name='user-detail'),
]

"""
EXAMPLE how to access (using httpie):
http http://127.0.0.1:8000/ Accept:application/json          # Request JSON
http http://127.0.0.1:8000/ Accept:text/html                 # Request HTML

Or by appending a format suffix:
http http://127.0.0.1:8000/.json  # JSON suffix
http http://127.0.0.1:8000/.api   # Browsable API suffix

Similarly, we can control the format of the request that we send, using the Content-Type header.
# POST using form data
http --form POST http://127.0.0.1:8000/ code="print(123)"

{
  "id": 3,
  "title": "",
  "code": "print(123)",
  "linenos": false,
  "language": "python",
  "style": "friendly"
}

# POST using JSON
http --json POST http://127.0.0.1:8000/ code="print(456)"

{
    "id": 4,
    "title": "",
    "code": "print(456)",
    "linenos": false,
    "language": "python",
    "style": "friendly"
}

If you add a --debug switch to the http requests above, you will be able to see the request type in request headers.
Now go and open the API in a web browser, by visiting http://127.0.0.1:8000/.
"""
