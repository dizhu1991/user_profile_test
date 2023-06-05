from django.contrib import admin

from user_profile_test.models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    fields = ['email', 'age', 'gender', 'profile_picture']


admin.site.register(MyUser, MyUserAdmin)
