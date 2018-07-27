from django.contrib import admin

from .models import Task, Category, Assignee, Status, AssingUserToTask, Comment

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Assignee)
admin.site.register(Status)
admin.site.register(AssingUserToTask)
admin.site.register(Comment)
