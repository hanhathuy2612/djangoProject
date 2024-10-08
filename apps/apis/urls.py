from django.urls import re_path, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.apis.views.admin_info import AdminInfoView
from apps.apis.views.info import InfoView

urlpatterns = [
    re_path(r"^info/(?P<info_id>\d+)$", InfoView.as_view(), name="info"),
    re_path(r"^admin/info/(?P<info_id>\d+)$", AdminInfoView.as_view(), name="info"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
