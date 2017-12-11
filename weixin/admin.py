# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

# Register your models here.
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from weixin.models import *

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('openId','name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('openId', 'password', 'name', 'is_active', 'is_admin','avatar')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('openId', 'name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('openId', 'password')}),
        ('Personal info', {'fields': ('name','avatar')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('openId', 'name', 'password1', 'password2')}
        ),
    )
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','title','types','answer')

class LawCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class LawDocumentAdmin(admin.ModelAdmin):
    list_display = ('id','title','types')

class CaseAdmin(admin.ModelAdmin):
    list_display = ('id','title')

class QAAdmin(admin.ModelAdmin):
    list_display = ('id','title')

class StoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')

class StoryImgaeAdmin(admin.ModelAdmin):
    list_display = ('id','story')

class OutletAdmin(admin.ModelAdmin):
    list_display = ('id','title','tel','address')

class GuideCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class GuideAdmin(admin.ModelAdmin):
    list_display = ('id','title','category')

# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(LawCategory, LawCategoryAdmin)
admin.site.register(LawDocument, LawDocumentAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(QA, QAAdmin)
admin.site.register(Story,StoryAdmin)
admin.site.register(StoryImage,StoryImgaeAdmin)
admin.site.register(Outlet,OutletAdmin)
admin.site.register(GuideCategory, GuideCategoryAdmin)
admin.site.register(Guide, GuideAdmin)


# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
