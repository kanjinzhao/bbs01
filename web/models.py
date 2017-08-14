#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    '''
    文章表
    '''
    title = models.CharField(u"文章标题",max_length=255,unique=True)
    categroy = models.ForeignKey("Category",verbose_name=u"板块")
    head_img = models.ImageField(upload_to="uploads")
    content = models.TextField(u"文章内容",)
    author = models.ForeignKey("UserProfile")
    publish_date = models.DateTimeField(auto_now=True)
    hideden = models.BooleanField(u"是否隐藏",default=True)
    weight = models.IntegerField(u"优先级",default=1000)

    def __unicode__(self):
        return "<%s,author:%s>" %(self.title,self.author)



class UserProfile(models.Model):
    '''
    用户表
    '''

    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    group = models.ManyToManyField('UserGroup')

    def __unicode__(self):
        return self.name




class Comment(models.Model):
    '''
    评论表
    '''
    article = models.ForeignKey(Article)
    user = models.ForeignKey("UserProfile")
    comment = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now=True)
    parent_commment = models.ForeignKey('self',related_name='p_comment')

    def __unicode__(self):
        return "<%s,user:%s>" %(self.comment,self.author)


class ThumUp(models.Model):
    '''
    点赞
    '''

    article = models.ForeignKey('Article')
    user = models.ForeignKey('UserProfile')
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "<%user:%s>" %(self.user)




class Category(models.Model):
    '''
    板块表
    '''
    name = models.CharField(max_length=64,unique=True)
    admin = models.ForeignKey('UserProfile',)


    def __unicode__(self):
        return self.name






class UserGroup(models.Model):
    '''
    用户组
    '''
    name = models.CharField(max_length=60,unique=True)

    def __unicode__(self):
        return self.name
