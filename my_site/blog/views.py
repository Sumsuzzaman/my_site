from django.shortcuts import render

# Create your views here.

def index(request):
        
    return render(request, "blog/index.html")
    

def posts(request):
    # return render(request, 'posts.html')
    pass

def post_detail(request):
    # return render(request, 'post.html')
    pass
