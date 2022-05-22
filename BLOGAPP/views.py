from django.shortcuts import render,redirect
from .models import Article

# Create your views here.
def home(request):
    '''renders the page when the user is logged in'''
    my_article = Article.objects.all()
    return render(request,'index.html',{'my_article': my_article})

def sign(request):
    return render(request,'sign.html')
def log(request):
    return render(request,'log.html')


def index(request):
    return render(request,'content.html')
def index(request):
    return render(request,'edit.html')
def index(request):
    return render(request,'profile.html')
def index(request):
    return render(request,'email.html')

def join(request):
    '''Add a task to the database'''
    if request.method == 'POST':
       join_passed = request.POST.get('join')
       if join_passed:
          print(join_passed)
        # # new_join = Article()
        # new_join.name = join_passed
        # new_join.save()
    return render(request,'index.html')