from django.shortcuts import render, HttpResponse
from django.http import response, JsonResponse
from django.utils.encoding import smart_str
import mimetypes

import os
import json
import socket


def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return d

def home_page(request):

    hostname = socket.gethostname()  
    print(hostname)  
    ip_address = socket.gethostbyname(hostname) 
    try:
        path = '/home'
        root = os.listdir(path)
    except Exception as e:
        path = '/Users'
        root = os.listdir(path)
    finally:
        root_dir = os.listdir(f'{path}/{root[0]}')
    
    list_dir = []
    for d in root_dir:
        if d[0] != '.':
            list_dir.append(d)
    root = {
        'roots' : list_dir
    }
    context = { 'ip_address' : ip_address, 'root' : json.dumps(root)}
    return render(request,'index.html',context)



def download(request):
    fl_path = '/home/sensen/Downloads/demo.mp4'
      # fill these variables with real values
    # fl_path = ‘/file/path'
    filename = 'new.mp4'

    fl = open(fl_path,'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

    

