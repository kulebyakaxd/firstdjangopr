from django.contrib import admin
from .models import ToDo,ToDoHistory

# Register your models here.


admin.site.register(ToDo)
admin.site.register(ToDoHistory)