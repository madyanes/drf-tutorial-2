from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('', views.SnippetListGeneric.as_view()),
    path('<int:pk>/', views.SnippetDetailGeneric.as_view()),
    path('users/', views.UserListGeneric.as_view()),
    path('users/<int:pk>', views.UserDetailGeneric.as_view()),
]

# We don't necessarily need to add these extra url patterns in, but it gives us a simple, clean way of referring to a specific format.
urlpatterns = format_suffix_patterns(urlpatterns)

"""
EXAMPLE how to access (using httpie):
http http://127.0.0.1:8000/ Accept:application/json           # Request JSON
http http://127.0.0.1:8000/ Accept:text/html         # Request HTML

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
