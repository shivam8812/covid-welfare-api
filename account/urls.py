from django.urls import path

from .views import AuthenticationView

urlpatterns = [
    path('user/register/', AuthenticationView.as_view({'post':'post'})),
]
