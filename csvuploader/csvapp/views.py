import re
from django.shortcuts import render, redirect
from .models import UploadedFile, StudentData
from .forms import CSVUploadForm
import pandas as pd
from django.db import connection



def sanitize_table_name(name):
    return re.sub(r'[^a-zA-Z0-9_]', '_', name.lower())


def index(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            process_uploaded_file(uploaded_file)
            return redirect('index')
    else:
        form = CSVUploadForm()

    uploaded_files = UploadedFile.objects.all()
    context = {'form': form, 'uploaded_files': uploaded_files}
    return render(request, 'csvapp/index.html', context)

def process_uploaded_file(uploaded_file):
    file_path = uploaded_file.file.path
    df = pd.read_csv(file_path)

    table_name = sanitize_table_name(uploaded_file.file.name)
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ("
                       "student_id float, "
                       "marks float, "
                       "attendance float)")

        uploaded_file_instance = UploadedFile.objects.get(pk=uploaded_file.pk)

        for index, row in df.iterrows():
            student_id = float(row['student_id'])
            marks = float(row['marks'])
            attendance = float(row['attendance'])
            
            cursor.execute(f"INSERT INTO {table_name} (student_id, marks, attendance) "
                           "VALUES (%s, %s, %s)",
                           (student_id, marks, attendance))

            StudentData.objects.create(
                uploaded_file=uploaded_file_instance,
                student_id=student_id,
                marks=marks,
                attendance=attendance
            )


def plot(request):
    uploaded_files = UploadedFile.objects.all()
    context = {'uploaded_files': uploaded_files}
    return render(request, 'csvapp/plot.html', context)
