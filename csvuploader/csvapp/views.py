from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import CSVUploadForm

def index(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CSVUploadForm()
    
    uploaded_files = UploadedFile.objects.all()
    context = {'form': form, 'uploaded_files': uploaded_files}
    return render(request, 'csvapp/index.html', context)


def plot(request):
    uploaded_files = UploadedFile.objects.all()
    context = {'uploaded_files': uploaded_files}
    return render(request, 'csvapp/plot.html', context)