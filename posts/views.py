from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import Posts,Comments
import io
from rest_framework.parsers import JSONParser
from . import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view


class CreatePost(APIView):
    def post(self,request,format=None):
        author=get_user_model().objects.get(pk=request.user.id)
        json_data=request.body 
        stream=io.BytesIO(json_data) 
        pythondata=JSONParser().parse(stream)
        serializer=serializers.CreatePostSerializer(data=pythondata)
        
        if serializer.is_valid():
            currentpost=Posts.objects.create(author=author,Title=pythondata['Title'],Description=pythondata['Description'],likes=0)
            context={
                "POST-ID":currentpost.id,
                "Title":currentpost.Title,
                "Description":currentpost.Description,
                "Created Time":currentpost.CreatedTime
            }
            return Response(context)


# class DeletePost(APIView):
#     def delete(self,request,pk,format=None):
#         deletepost=Posts.objects.get(pk=pk)
#         deletepost.delete()
#         return Response({'msg':'Data Deleted Succesfully'})

class LikePost(APIView):
    def patch(self,request,pk,format=None):
        likepost=Posts.objects.get(pk=pk)
        likepost.likes=likepost.likes+1
        likepost.save()
        return Response({'msg':'Post liked'})
        

class UnlikePost(APIView):
    def patch(self,request,pk,format=None):
        unlikepost=Posts.objects.get(pk=pk)
        if(unlikepost.likes>0):
            unlikepost.likes=unlikepost.likes-1
            unlikepost.save()
            return Response({'msg':'Post unliked'})
        else:
            unlikepost.like=0
            return Response({'msg':'likes can not be negative'})

 


class CommentPost(APIView):
    def post(self,request,pk,format=None):
        postinstance=Posts.objects.get(pk=pk)
        json_data=request.body 
        stream=io.BytesIO(json_data) 
        pythondata=JSONParser().parse(stream)
        serializer=serializers.CommentSerializer(data=pythondata)
        if serializer.is_valid():
            currentcomment=Comments.objects.create(post_id=postinstance,comments=pythondata['Comment'])
            context={
                "Comment Id": currentcomment.id
            }

            return Response(context)

@api_view(['GET','DELETE'])
def GetPostDelete(request,pk):
    if request.method=="DELETE":
        deletepost=Posts.objects.get(pk=pk)
        deletepost.delete()
        return Response({'msg':'Data Deleted Succesfully'})  

    if request.method=="GET": 
        singlepost=Posts.objects.get(pk=pk)
        comm=Comments.objects.filter(post_id=pk)
        listcomm=[]
        for i in comm:
            listcomm.append(i.comments)
        #print(listcomm)

        context={
            "id":singlepost.id,
            "likes":singlepost.likes,
            "comments":listcomm
        }
        return Response(context)

        #print(comm[0].comments)

                   

# class GetSinglePost(APIView):
#     def get(self,request,pk,format=None):
#         singlepost=Posts.objects.get(pk=pk)
#         serializer=serializers.GetSinglePostSerializer(singlepost)
#         return Response(serializer.data)
        


class GetAllPost(APIView):
    def get(self,request,format=None):
        allpostuser=Posts.objects.filter(author=request.user.id)
        
        j=1
        dictofpost={}
        for i in allpostuser:
            id=i.id
            title=i.Title
            desc=i.Description
            created_at=i.CreatedTime

            comm=Comments.objects.filter(post_id=id)
            listcomm=[]
            for k in comm:
                listcomm.append(k.comments)

            comments=listcomm  
            likes=i.likes

            singlepostdata={
                "id":id,
                "title":title,
                "desc":desc,
                "created_at":created_at,
                "comments":comments,
                "likes":likes
            }  
            
            dictofpost['Post '+str(j)]=singlepostdata
            j=j+1

        return Response(dictofpost)

