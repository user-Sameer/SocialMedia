from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .serializers import UserSerializer,GetUserFollowingSerializer
from django.shortcuts import render
from django.http import HttpResponse
from .models import UserFollowing
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class Test(APIView):
    def get(self,request,pk=None,format=None):
        return HttpResponse('hello test')


class GetProfile(APIView):
    def get(self, request ,pk, format=None):
        userinstance=get_user_model().objects.get(pk=pk)
        name=userinstance.get_full_name()
        following=len(UserFollowing.objects.filter(user_id=pk))
        followers=len(UserFollowing.objects.filter(following_user_id=pk))
        userprofile={

                        'username':name,
                        'followers':followers,
                        'following':following,
        }
        #print(request.user.email) prints the curren user email id
        return Response(userprofile)
   
class FollowUser(APIView):
    def post(self,request,pk,format=None):
        print(request.user.id)
        userinstance=get_user_model().objects.get(pk=request.user.id)
        followinginstance=get_user_model().objects.get(pk=pk)
        UserFollowing.objects.create(user_id=userinstance,following_user_id=followinginstance)
        return Response({'msg':'User Followed Succesfully'})

class UnfollowUser(APIView):
    def post(self,request,pk,formate=None):
        detleteinstance=UserFollowing.objects.filter(user_id=request.user.id,following_user_id=pk)
        detleteinstance.delete()
        return Response({'msg':'User Unfollowed Successfully'})


