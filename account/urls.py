from django.urls import path

from .views import AuthenticationView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('user/register/', AuthenticationView.as_view({'post':'post'})),
    path('user/login/', obtain_auth_token, name = 'login'),
]
