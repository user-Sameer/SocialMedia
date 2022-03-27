from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
# from rest_framework.routers import DefaultRouter

# router= DefaultRouter()
# router.register('api/user/',views.Test,basename='user')


urlpatterns = [
    
    path('api/authenticate/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/<int:pk>', views.GetProfile.as_view(),),
    path('api/follow/<int:pk>', views.FollowUser.as_view()),
    path('api/unfollow/<int:pk>', views.UnfollowUser.as_view()),
    path('api/test',views.Test.as_view()),
]