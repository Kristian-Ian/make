from django.shortcuts import redirect
from . import views

def index_redirect(request):
    return redirect('/web/')

def inex(request):
    if request.method== 'POST':
        member= Member(username=request.POST &#91; 'username'], password=request.POST&#91;'password'], firstname = request.POST&#91;'firstname'], lastname=request.POST&#91;'lastname'], email=request.POST&#91;'email'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'web/index.html')

def login(request):
    return render(request, 'web/login.html')

def home(request):
    if request.method == 'POST':
        if member.objects.filter (username=request.POST &#91; 'username'], password=request.POST&#91;'password'], firstname = request.POST&#91;'firstname'], lastname=request.POST&#91;'lastname'], email=request.POST&#91;'email']).exists():
            return render(request, 'web/home.html',{'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'web/login.html', context)
