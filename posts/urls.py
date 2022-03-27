from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
# from rest_framework.routers import DefaultRouter

# router= DefaultRouter()
# router.register('api/user/',views.Test,basename='user')


urlpatterns = [
    
    path('api/posts/', views.CreatePost.as_view(), name='create_post'),
    path('api/posts/<int:pk>', views.GetPostDelete, name='delete_post'),
    path('api/like/<int:pk>', views.LikePost.as_view(),),
    path('api/unlike/<int:pk>', views.UnlikePost.as_view()),
    path('api/comment/<int:pk>', views.CommentPost.as_view()),
    path('api/all_posts',views.GetAllPost.as_view(),)
]