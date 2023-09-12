from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app import views

router = DefaultRouter()
router.register(r'adcopy', views.AdCopyViewSet, basename='adcopy')

urlpatterns = [
    path('', views.index, name='index'),
    # for djoser_JWT
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('accounts/', include('accounts.urls')),
    # for rest_framework
    path('api/', include(router.urls)),
    path('api/adcopy/', views.ad_copy_api, name='ad_copy_api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]