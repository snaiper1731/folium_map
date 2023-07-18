from django.shortcuts import render
from django.http import HttpResponse
import os
import subprocess

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
    context = {}
    return render(request, 'page/index.html', context)

def run_script(request):
    dirname = os.path.join(BASE_DIR, 'page', 'map_generate.py')
    os.system('python' + ' map_generate.py')
    return HttpResponse('Script executed')
