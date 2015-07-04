from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from .models import Post


class PostsView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-published_date')[:10]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

   # def post_list(request):
   #   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
   #   return render(request, 'blog/post_list.html', {'posts': posts})

