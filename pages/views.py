from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def home(request):

    fss = FileSystemStorage()

    file_url = fss.url('static\media\ex1.jpg')
    file_url_2 = fss.url('static\media\ex1.png')
    file_url_3 = fss.url('static\media\ex2.jpg')
    file_url_4 = fss.url('static\media\ex2.png')
    file_url_5 = fss.url('static\media\ex3.jpg')
    file_url_6 = fss.url('static\media\ex3.png')
    file_url_7 = fss.url('static\media\ex4.jpg')
    file_url_8 = fss.url('static\media\ex4.png')
    file_url_9 = fss.url('static\media\ex5.jpg')
    file_url_10 = fss.url('static\media\ex5.png')

    context = {
        'file_url': file_url,
        'file_url_2': file_url_2,
        'file_url_3': file_url_3,
        'file_url_4': file_url_4,
        'file_url_5': file_url_5,
        'file_url_6': file_url_6,
        'file_url_7': file_url_7,
        'file_url_8': file_url_8,
        'file_url_9': file_url_9,
        'file_url_10': file_url_10,
    }
    return render(request, 'home.html', context)