from django.contrib import admin
from .models import Quizzes, Question, Answer, Category
# Register your models here.

admin.site.register(Quizzes)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Category)
