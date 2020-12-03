from django.urls import path, include
from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from listings.apis import views

urlpatterns = [
    path('listings/propertyTypeImages/', views.PropertyTypeImageList.as_view(), name='p_type_list_api'),
    #Home endpoints
    path('listings/property/homes/', views.HomeListApi.as_view(), name='home_list_api'),
    path('listings/property/home/create/', views.HomeCreateApi.as_view(), name='home_create_api'),
    path('listings/property/home/<int:pk>/retrieve/', views.HomeDetailApi.as_view(), name='home_detail_api'),
    path('listings/property/home/<int:pk>/edit/', views.HomeUpdateApi.as_view(), name='home_update_api'),
    path('listings/property/home/<int:pk>/save/', views.HomeSavesSerializer.as_view(), name='home_saves_api'),
    path('listings/property/home/<int:pk>/delete/', views.HomeDeleteApi.as_view(), name='home_delete_api'),
    #Users & authentication
    path('accounts/user_listings/property/home/', views.UserHomeListings.as_view(), name='user_home_listings'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
