
from django.contrib import admin
from django.urls import path,include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# from rest_framework.routers import DefaultRouter

# router= DefaultRouter()
# router.register('user',views.Test,basename='user')
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/user/', views.Test.as_view()),
    path('',include('accounts.urls')),
    path('', include('posts.urls')),

   
  
   

    #path('',include(router.urls)),
]
