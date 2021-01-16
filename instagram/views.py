from django.shortcuts import render,redirect

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images=Image.objects.all()
    comments=Comments.objects.all()
    return render(request,'instagram/index.html',{"images":images,"comments":comments})

