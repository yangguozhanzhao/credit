# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
	def create_user(self, openId,name, password=None):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		if not openId:
			raise ValueError('Users must have an openId')

		user = self.model(
			openId=openId,
			name=name,
		)
		user.set_password("1234pttk")
		user.save(using=self._db)
		return user

	def create_superuser(self, openId,name, password):
		"""
		Creates and saves a superuser with the given email, date of
		birth and password.
		"""
		user = self.create_user(
			openId,
			password=password,
			name=name,
		)
		user.is_admin = True
		user.save(using=self._db)
		return user


class MyUser(AbstractBaseUser):
	openId = models.CharField(
		verbose_name='openId',
		max_length=50,
		unique=True,
	)
	name=models.CharField(max_length=100)
	gender=models.IntegerField(default=1)
	avatar = models.URLField()
	create_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now=True)
	
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	objects = MyUserManager()
	USERNAME_FIELD = 'openId'
	REQUIRED_FIELDS = ['name']
	def get_full_name(self):
		# The user is identified by their email address
		return self.name

	def get_short_name(self):
		# The user is identified by their email address
		return self.name

	def __str__(self):
	# __unicode__ on Python 2
		return self.name

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True
	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin

	def __unicode__(self):
		return '%s'%(self.name)
# 题库
class Question(models.Model):
	question_type=(
         (1, u'单选'),
         (2, u'多选'),
         (3, u'判断'),
    )
	types=models.PositiveSmallIntegerField(choices=question_type,verbose_name='题型')
	title=models.CharField(max_length=200,verbose_name='问题')
	option_A=models.CharField(max_length=200,verbose_name='A',blank=True,null=True)
	option_B=models.CharField(max_length=200,verbose_name='B',blank=True,null=True)
	option_C=models.CharField(max_length=200,verbose_name='C',blank=True,null=True)
	option_D=models.CharField(max_length=200,verbose_name='D',blank=True,null=True)
	option_E=models.CharField(max_length=200,verbose_name='E',blank=True,null=True)
	answer=models.CharField(max_length=10,verbose_name='答案')

	create_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return '%s%s' % (self.types,self.title)


# 法律法规
class LawCategory(models.Model):
	name=models.CharField(max_length=100)
	create_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return '%s' % (self.name)
class LawDocument(models.Model):
	types=models.ForeignKey("LawCategory",related_name="law")
	title=models.CharField(max_length=200,blank=True)
	doc=models.FileField(upload_to='docs',blank=True)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return '%s'%(self.title)

# 案例
class Case(models.Model):
	title = models.CharField(max_length=200,verbose_name="案例标题")
	content = models.TextField(verbose_name="案例内容")
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return '%s'%(self.title)

		
# 宣传
class Publicity(models.Model):
	title = models.CharField(max_length=200,verbose_name="标题")
	content = models.TextField(verbose_name="内容")
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return '%s'%(self.title)