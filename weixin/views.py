# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from weixin.models import *
from weixin.serializers import *

from rest_framework.permissions import *
from rest_framework.decorators import api_view,parser_classes,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework_jwt import authentication
#from WXBizDataCrypt import WXBizDataCrypt
import requests
import json
import random
import string
import time


APPID="wx792afb48d3249315"
APPSECRET="8145f1c123ddef11dd514f69314e7032"

# code换取openId登录
@api_view(['POST'])
def login(request,format=None):
	code=request.data['code']
	#print code
	#code -> openid
	keyURL= 'https://api.weixin.qq.com/sns/jscode2session?appid='+APPID+'&secret='+APPSECRET+'&js_code='+code+'&grant_type=authorization_code'
	r = requests.post(keyURL).json()
	#print "r:",r

	openId= r['openid']	
	user = MyUser.objects.filter(openId=openId)
	if user:
		pass
	else:
		userSerializer=UserSerializer()
		data={
				"openId":openId,
			}
		userSerializer.create(data)

	user = MyUser.objects.get(openId=openId)
	serializer = UserSerializer(user,context={'request': request})
	#print type(serializer.data)
	return Response(serializer.data)

#法规
@api_view(['POST'])
@permission_classes((AllowAny, ))
def search(request,format=None):
	results=[]
	key=request.data["key"]
	laws= LawDocument.objects.filter(content__icontains=key)
	for law in laws:
		serializer=LawDocumentSerializer(law,context={'request':request})
		results.append(serializer.data)
	return JsonResponse({'results':results})


## list／create／retrieve／update／partial_update／destroy

class UserViewSet(viewsets.ModelViewSet):
	"""
	create: AllowAny,新建用户通过openId和用户名即可，测试OK
	read: IsAuthenticated,公司内部人员，查看个人信息
	partial_update:IsAuthenticated,管理者和自己，修改个人信息
	delete: IsAdminUser
	list: IsAdminUser
	update: IsAdminUser
	"""
	queryset = MyUser.objects.all()
	serializer_class = UserSerializer

	# permission 管理
	permission_classes=[IsAuthenticated, ]
	permissionByAction = {'create':[AllowAny,],
					#'partial_update':[AllowAny,],
						}
	def get_permissions(self):
		try:
			return [permission() for permission in self.permissionByAction[self.action]]
		except KeyError: 
			return [permission() for permission in self.permission_classes]

class QuestionViewSet(viewsets.ModelViewSet):
	"""
	create: IsAuthenticated
	read: IsAuthenticated
	partial_update:IsAuthenticated
	delete: IsAuthenticated
	list: IsAuthenticated
	update: IsAuthenticated
	本身应该是IsOnwer
	"""
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

	# permission 管理
	permission_classes=[IsAuthenticated, ]
	permissionByAction = {'retrieve':[AllowAny,],
							'list':[AllowAny,],
						}
	def get_permissions(self):
		try:
			return [permission() for permission in self.permissionByAction[self.action]]
		except KeyError: 
			return [permission() for permission in self.permission_classes]

class LawCategoryViewSet(viewsets.ModelViewSet):
	"""
	create: IsAdminUser
	read: AllowAny
	partial_update:IsAdminUser
	delete: IsAdminUser
	list: AllowAny
	update: IsAdminUser
	"""
	queryset = LawCategory.objects.all()
	serializer_class = LawCategorySerializer

	# permission 管理
	permission_classes=[IsAdminUser, ]
	permissionByAction = {'retrieve':[AllowAny,],
							'list':[AllowAny,],
						}
	def get_permissions(self):
		try:
			return [permission() for permission in self.permissionByAction[self.action]]
		except KeyError: 
			return [permission() for permission in self.permission_classes]

class LawDocumentViewSet(viewsets.ModelViewSet):
	"""
	create: IsAdminUser
	read: AllowAny
	partial_update:IsAdminUser
	delete: IsAdminUser
	list: AllowAny
	update: IsAdminUser
	"""
	queryset = LawDocument.objects.all()
	serializer_class = LawDocumentSerializer

	# permission 管理
	permission_classes=[IsAdminUser, ]
	permissionByAction = {'retrieve':[AllowAny,],
							'list':[AllowAny,],
						}
	def get_permissions(self):
		try:
			return [permission() for permission in self.permissionByAction[self.action]]
		except KeyError: 
			return [permission() for permission in self.permission_classes]


class CaseViewSet(viewsets.ModelViewSet):
	"""
	create: IsAdminUser
	read: AllowAny
	partial_update:IsAdminUser
	delete: IsAdminUser
	list: AllowAny
	update: IsAdminUser
	"""
	queryset = Case.objects.all()
	serializer_class = CaseSerializer

	# permission 管理
	permission_classes=[IsAdminUser, ]
	permissionByAction = {'retrieve':[AllowAny,],
						'list':[AllowAny,],
						}
	def get_permissions(self):
		try:
			return [permission() for permission in self.permissionByAction[self.action]]
		except KeyError: 
			return [permission() for permission in self.permission_classes]

class QAViewSet(viewsets.ModelViewSet):
	"""
	create: IsAuthenticated
	read: IsAuthenticated
	partial_update:IsAuthenticated
	delete: IsAuthenticated
	list: IsAdminUser
	update: IsAuthenticated
	"""
	queryset = QA.objects.all()
	serializer_class = QASerializer

	# permission 管理
	permission_classes=[IsAuthenticated, ]
	permissionByAction = {'list':[AllowAny,],
							'retrieve':[AllowAny,],
						}
	def get_permissions(self):
		try:
			return [permission() for permission in self.permissionByAction[self.action]]
		except KeyError: 
			return [permission() for permission in self.permission_classes]

class StoryViewSet(viewsets.ModelViewSet):
	"""
	create: IsAuthenticated
	read: IsAuthenticated
	partial_update:IsAuthenticated
	delete: IsAuthenticated
	list: IsAdminUser
	update: IsAuthenticated
	"""
	queryset = Story.objects.all()
	serializer_class = StorySerializer

	# permission 管理
	permission_classes=[IsAuthenticated, ]
	permissionByAction = {'list':[AllowAny,],
							'retrieve':[AllowAny,],
						}
	def get_permissions(self):
		try:
			return [permission() for permission in self.permissionByAction[self.action]]
		except KeyError: 
			return [permission() for permission in self.permission_classes]

class StoryImageViewSet(viewsets.ModelViewSet):
	"""
	create: IsAuthenticated
	read: IsAuthenticated
	partial_update:IsAuthenticated
	delete: IsAuthenticated
	list: IsAdminUser
	update: IsAuthenticated
	"""
	queryset = StoryImage.objects.all()
	serializer_class = StoryImageSerializer

	# permission 管理
	permission_classes=[IsAuthenticated, ]
	permissionByAction = {'list':[AllowAny,],
							'retrieve':[AllowAny,],
						}
	def get_permissions(self):
		try:
			return [permission() for permission in self.permissionByAction[self.action]]
		except KeyError: 
			return [permission() for permission in self.permission_classes]


class OutletViewSet(viewsets.ModelViewSet):
	"""
	create: IsAuthenticated
	read: IsAuthenticated
	partial_update:IsAuthenticated
	delete: IsAuthenticated
	list: IsAdminUser
	update: IsAuthenticated
	"""
	queryset = Outlet.objects.all()
	serializer_class = OutletSerializer

	# permission 管理
	permission_classes=[IsAuthenticated, ]
	permissionByAction = {'list':[AllowAny,],
							'retrieve':[AllowAny,],
						}
	def get_permissions(self):
		try:
			return [permission() for permission in self.permissionByAction[self.action]]
		except KeyError: 
			return [permission() for permission in self.permission_classes]
