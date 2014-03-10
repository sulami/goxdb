from django.shortcuts import render

from master.models import *

def index(request):
    if request.method == 'POST':
        resultlist = Balance.objects.get(acc=request.POST['userid']
        context = {'resultlist': resultlist}
        render(request, 'master/result.html', context)
    render(request, 'master/index.html')

