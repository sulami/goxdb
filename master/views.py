from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from master.models import *

@csrf_exempt
def index(request):
    if request.method == 'POST':
        resultlist = Balance.objects.filter(acc=request.POST['userid'])
        context = {'resultlist': resultlist}
        return render(request, 'master/result.html', context)
    return render(request, 'master/index.html')

