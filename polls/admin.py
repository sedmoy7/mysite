from django.contrib import admin

from .models import Question        #, Choice

# admin.site.register(Question)
# admin.site.register(Choice)


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    # inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    list_display = ['question_text', 'pub_date', 'was_published_recently']


# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#
#     def save_model(self, request, obj, form, change):
#         """
#         Переопределяем метод сохранения модели
#         """
#
#         if not change:  # Проверяем что запись только создаётся
#             obj.author = request.user  # Присваеваем полю автор текущего пользователя
#
#         super(QuestionAdmin, self).save_model(request=request, obj=obj, form=form, change=change)


# admin.site.register(Choice, ChoiceInline)

