from django.contrib import admin

from students.models import student

# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ("id", "stdName", "stdID", "stdSex", "stdBirth")
    # 過濾器
    list_filter = ("stdName", "stdSex")
    # 查詢功能
    search_fields = ("stdName", "stdID")
    # 排序方式
    ordering = ("id",)

admin.site.register(student, studentAdmin)