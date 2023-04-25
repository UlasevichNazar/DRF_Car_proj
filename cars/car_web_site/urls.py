from django.urls import path, include, re_path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
# router = routers.DefaultRouter()
# router.register(r'cars', views.CarViewSet, basename='cars')
# print(router.urls)
urlpatterns = [

    path('cars/', views.CarAPIList.as_view()),
    path('cars/<int:pk>', views.CarAPIList.as_view()),
    path('cars/update/<int:pk>', views.CarAPIUpdate.as_view()),
    path('cars/destroy/<int:pk>', views.CarAPIDestroy.as_view()),
    path('cars/details/<int:pk>', views.CarAPIDetailView.as_view()),
    path('cars/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('', include(router.urls)),
    path('register/', views.RegisterUserView.as_view()),


]
