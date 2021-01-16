from django.shortcuts import render,redirect

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images=Image.objects.all()
    comments=Comments.objects.all()
    return render(request,'instagram/index.html',{"images":images,"comments":comments})


@login_required
def profile(request):
    current_user=request.user
    profile_info = Profile.objects.filter(user=current_user).first()
    posts =  request.user.image_set.all()
    return render(request,'registration/profile.html',{"images":posts,"profile":profile_info,"current_user":current_user})

def search_username(request):

    if 'search_username' in request.GET and request.GET["search_username"]:
        searched_name = request.GET.get("search_username")
        searched_user = User.objects.filter(username__icontains=search_username)
        message = f"{searched_name}"

        return render(request, 'search.html', {"message": message, "username": username})

    else:
        message = "Sorry, No one by this username"
        return render(request, 'instagram/search.html', {"message": message})
    
def upload_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
        return redirect('index')

    else:
        form = ImageForm()
        return render(request,'instagram/upload_image.html', {"form":form})
    