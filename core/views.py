from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse

def frontpage(request):
    posts = Post.objects.all 
    return render(request, 'core/frontpage.html' , {'posts':posts})


def about(request):
    return render(request, 'core/about.html')



def robots_txt(request):
    text =[
        "USER-AGENT:*",
        "Disallow:/admin/",
    ] 

    return HttpResponse("\n".join(text , content_type="text/plain"))   