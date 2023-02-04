from typing import List

import django.core.handlers.wsgi
from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpResponseRedirect

# Register your models here.
from .models import MyModel , Student , Company


@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    ordering = ('-pk' ,)

    class Meta:
        pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    ordering = ('-pk' ,)

    class Meta:
        pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    ordering = ('-pk' ,)

    @admin.action(description='Export')
    def export_objects(self , request: django.core.handlers.wsgi.WSGIRequest , queryset: QuerySet):
        selected = queryset.values_list('pk' , flat=True)
        return HttpResponseRedirect(
            redirect_to=f"/export?ids={','.join(str(pk) for pk in selected)}"
        )

    # 선택 카운터
    # actions_selection_counter = True

    # 변경 목록 페이지에서 사용할 수 있는 작업 목록
    # admin에서 action 함수를 정의한다.
    # 쿼리셋에서 선택된 객체의
    actions = [export_objects]

    list_display: List[str] = ('name' , 'company_type' , 'founded' , 'status' ,)

    list_filter: List[str] = ('company_type' ,)  # 오른쪽 사이드바에서 필터를 활성화하도록 설정한다.
