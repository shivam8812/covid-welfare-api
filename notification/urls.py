from django.urls import path
from .seekview import SeekView
from .provideview import ProvideView

urlpatterns = [
    path('seekreq/', SeekView.as_view({'post':'seek_request', 'get':'seek_request_list', 'delete':'delete_request'})),
    path('providereq/', ProvideView.as_view({'post':'provide_request', 'get':'provide_request_list', 'delete':'delete_request'})),
]
