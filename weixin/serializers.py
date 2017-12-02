#!/venv/bin/env python
# -*- coding: utf-8 -*-
#copyRight by yangguozhanzhao
#序列化数据库的查询结果到json，rest_framwork最方便的地方

from rest_framework import serializers
from weixin.models import *

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Question
		fields = ('url','id','types','title')

class OptionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Option
		fields = ('url','id','question','content','answer')

class LawCategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = LawCategory
		fields = ('url','id','name')


class LawDocumentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = LawDocument
		fields = ('url','id','title','types','doc')

class CaseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Case
		fields = ('url','id','title','content')

class PublicitySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Publicity
		fields = ('url','id','title','content')

				
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MyUser
		# 直接在fields里面写related_name即可
		fields = ('url','id','openId', 'name','gender','avatar')

	def create(self, validated_data):
		user = MyUser(
			openId=validated_data['openId'],
		)
		user.set_password("1234pttk")
		user.save()
		return user
