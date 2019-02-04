from django.contrib import admin

from .models import (Student,
                     Trainer,
                     Technology)

admin.site.register(Student)
admin.site.register(Technology)
admin.site.register(Trainer)
