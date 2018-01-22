#!/usr/bin/env python
#coding:utf-8
 
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "credit.settings")
 
'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''
 
import django
if django.VERSION >= (1, 7):#自动判断版本
	django.setup()
 
 
def main():
	from weixin.models import Question
	f = open('question.csv')
	for line in f:

		types,title,option_A,option_B,option_C,option_D,option_E,answer = line.split(',')
		print(types,title,option_A,option_B,option_C,option_D,option_E,answer)
		if types=="单选":
			type_num=1
		elif types=="多选":
			type_num=2
		else :
			type_num=3
		Question.objects.create(types=type_num,title=title,option_A=option_A,option_B=option_B,\
			option_C=option_C,option_D=option_D,option_E=option_E,answer=answer)
	f.close()
 
if __name__ == "__main__":
	main()
	print('Done!')