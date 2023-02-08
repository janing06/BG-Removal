from django.shortcuts import  render
from rembg import remove
from PIL import Image
import os

from django.core.files.storage import FileSystemStorage

def removeBackground(request):

    return render(request, 'removebg/removebackground.html')

def bg_removal(request):

    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)

        input_path = fss.path(file)
        output_path = 'static/media/output.png'

        input = Image.open(input_path)
        output = remove(input)
        output.save(output_path)
        
        file_url = fss.url('static/media/output.png')
        os.remove(fss.path(file))
        print(file_url)
        return render(request, 'removebg/removebackground.html', {'file_url': file_url})

    return render(request,'removebg/removebackground.html',{})
