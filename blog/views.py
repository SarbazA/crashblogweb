from django.shortcuts import get_object_or_404 , render , redirect 
from.models import Post,Category
from django.db.models import Q

from .forms import CommentForm

def detail (request, category_slug ,slug):
    post = get_object_or_404 (Post ,  slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.post = post 
            comment.save()

            return redirect('/')

    else:    

      form = CommentForm()

    



    return render ( request , 'blog/detail.html' ,{'post':post ,'form':form})


def category (request ,slug):

  category = get_object_or_404(Category , slug=slug)

  return render(request , 'blog/category.html' ,{'category':category})


def search (request): 
  query = request.GET.get('query','')
  posts = Post.objects.filter(Q(title__icontains=query)| Q(body__icontains=query)|Q(intro__icontains=query))


  return render (request, 'blog/search.html' , {'posts':posts ,'query':query})