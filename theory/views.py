from django.views import generic

from theory.models import Post


class PostListView(generic.ListView):
    template_name = 'theory/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    template_name = 'theory/post_detail.html'
    model = Post
    context_object_name = 'post'
