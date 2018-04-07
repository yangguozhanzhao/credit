#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by yangguozhanzhao 
#应用api的urls配置

from django.conf.urls import url,include
from weixin import views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'law_category', views.LawCategoryViewSet)
router.register(r'law_document', views.LawDocumentViewSet)
router.register(r'case', views.CaseViewSet)
router.register(r'qa', views.QAViewSet)
router.register(r'story', views.StoryViewSet)
router.register(r'story_image', views.StoryImageViewSet)
router.register(r'outlet', views.OutletViewSet)
router.register(r'guide_category', views.GuideCategoryViewSet)
router.register(r'guide', views.GuideViewSet)
router.register(r'feedback', views.FeedbackViewSet)
router.register(r'exam', views.ExamViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^docs/', include_docs_urls(title='Credit API')),
    url(r'^token/', obtain_jwt_token),
    url(r'^login/',views.login),
    url(r'^search/',views.search),
]
