#!/venv/bin/env python
# -*- coding: utf-8 -*-
#copyRight by yangguozhanzhao
#序列化数据库的查询结果到json，rest_framwork最方便的地方

from rest_framework import serializers
from weixin.models import *

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Question
		fields = ('url','id','types','title','option_A','option_B','option_C','option_D','option_E','answer')


class LawDocumentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = LawDocument
		fields = ('url','id','title','types','content')

class LawSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = LawDocument
		fields = ('url','id','title','types')

class LawCategorySerializer(serializers.HyperlinkedModelSerializer):
	law=LawSerializer(many=True,read_only=True)
	class Meta:
		model = LawCategory
		fields = ('url','id','name','law')

class CaseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Case
		fields = ('url','id','title','content')

class QASerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = QA
		fields = ('url','id','title','content')


class StoryImageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = StoryImage
		fields = ('url','id','image')

class StorySerializer(serializers.HyperlinkedModelSerializer):
	images=StoryImageSerializer(many=True,read_only=True)
	class Meta:
		model = Story
		fields = ('url','id','title','images')

class OutletSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Outlet
		fields = ('url','id','title','tel','address','latitude','longitude')

class GuideSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Guide
		fields = ('url','id','title','category','doc')

class GuideCategorySerializer(serializers.HyperlinkedModelSerializer):
	guide=GuideSerializer(many=True,read_only=True)
	class Meta:
		model = GuideCategory
		fields = ('url','id','name','guide')
			
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

