from django.contrib import admin
from .models import UploadedFile
from .models import StudentData

admin.site.register(StudentData)

admin.site.register(UploadedFile)
