from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    #model = Post
    #ordering = '-title'
    queryset = Post.objects.order_by('-time_in')
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = 'Распродажа в среду!'
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
