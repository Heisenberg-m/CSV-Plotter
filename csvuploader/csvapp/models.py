from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


class StudentData(models.Model):
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    student_id = models.FloatField()
    marks = models.FloatField()
    attendance = models.FloatField()

    def __str__(self):
        return f"Student ID: {self.student_id}, Marks: {self.marks}, Attendance: {self.attendance}"
