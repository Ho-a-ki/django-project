from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm

class IndexView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts' 
    def get_queryset(self):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return posts

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})