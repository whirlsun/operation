from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# admin.site.register(Question)

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {"fields": ["question_text"]}),
    #     ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    #
    # 一列显示
    # inlines = [ChoiceInline]
    # 一个列表显示内容，分三个列
    list_display = ["question_text", "pub_date", "was_pubished_recently"]
    # 添加一个侧边过滤栏，按发布日期过滤
    list_filter = ["pub_date"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
