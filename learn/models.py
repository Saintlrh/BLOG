from django.db import models
# from django.contrib.auth.models import User
# from DjangoUeditor.widgets import UEditorWidget
# from DjangoUeditor.forms import UEditorModelForm
from DjangoUeditor.models import UEditorField
# Create your models here.



class Article(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    content = UEditorField('内容', height=300, width=1000, default='', blank=True, toolbars='full',
                           imagePath='ueimages/',  # 上传图片存储的路径，不设置的话默认是配置文件中MEDIA_ROOT路径
                           filePath='files_ue/',
                           upload_settings={"imageMaxSize": 1204000},
                           )
    introduction = models.TextField()
    classify = models.ForeignKey('Classify')
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    #对于数据库里面的表
    #类里面的属性对应表里面的字段


class Classify(models.Model):
    name = models.CharField(max_length=20)
    num = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Comment(models.Model):
    date = models.DateTimeField()
    comment = models.CharField(max_length=200)
    user_id = models.ForeignKey('User')
    article_id = models.ForeignKey('Article')
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.comment


class User(models.Model):
    userName = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=100)
    userEmail = models.EmailField(max_length=30)
    userToken = models.CharField(max_length=50)
    userPhonenum = models.CharField(max_length=11, default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.userName

    @classmethod
    def createuser(cls, name, passwd, emial, phonenum, token):
        u = cls(userName=name, userPassword=passwd, userEmail=emial, userPhonenum=phonenum, userToken=token)
        return (u)


class Share(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    content = UEditorField('内容', height=300, width=1000, default='', blank=True, toolbars='full',
                           imagePath='ueimages/',  # 上传图片存储的路径，不设置的话默认是配置文件中MEDIA_ROOT路径
                           filePath='files_ue/',
                           upload_settings={"imageMaxSize": 1204000},
                           )
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


#模型对应database中的表
#说明：不需要生成主键，自动生成主键，并且自动增加
