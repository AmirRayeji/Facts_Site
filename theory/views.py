from django.views import generic
from django.urls import reverse_lazy

from theory.models import Post
from theory.forms import PostForm


class PostListView(generic.ListView):
    template_name = 'theory/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    template_name = 'theory/post_detail.html'
    model = Post
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'theory/post_create.html'

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'theory/post_create.html'

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'theory/post_delete.html'
    success_url = reverse_lazy('post_list')
