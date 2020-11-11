from django.urls import path

from .views import AuthenticationView
from .detailview import DetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('user/register/', AuthenticationView.as_view({'post':'post'})),
    path('user/login/', obtain_auth_token, name = 'login'),
    path('<slug>/', DetailView.as_view({'get':'get', 'post':'post'})),
    path('<slug>/seek/', DetailView.as_view({'post':'post_seek', 'get':'get_seek'})),
    path('<slug>/seeklist/', DetailView.as_view({'get':'seek_list'})),
    path('<slug>/providelist/', DetailView.as_view({'get':'provide_list'})),
]

#localhost:8000/api/hee/seek/