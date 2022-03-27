from django.db import models
from django.contrib.auth import get_user_model


class Posts(models.Model):
    usermodel=get_user_model()
    author=models.ForeignKey(usermodel,on_delete=models.CASCADE,related_name="author")
    Title=models.CharField(max_length=500)
    Description=models.TextField(max_length=10000000)
    CreatedTime=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField()

    def __str__(self):
        return self.Title
    


class Comments(models.Model):
    post_id=models.ForeignKey(Posts,on_delete=models.CASCADE ,related_name="post")
    comments=models.TextField(max_length=1000000)


