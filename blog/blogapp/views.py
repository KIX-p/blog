from msilib.schema import ListView
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.views.generic import ListView
# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blogapp/post/list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug = post, status = 'published', publish__year = year, publish__month = month, publish__day = day)
    return render(request, 'blogapp/post/detail.html', {'post':post})

