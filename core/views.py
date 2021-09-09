from django.views.generic import DetailView, ListView
from django.http.response import JsonResponse
from core.models import Post


class PostListView(ListView):

    model = Post

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(
            data=list(self.get_queryset().values('id', 'title', 'body')),
            safe=False
        )


class PostDetailView(DetailView):

    model = Post

    def render_to_response(self, context, **response_kwargs):
        obj = self.get_object(self.get_queryset())
        return JsonResponse(
            data={'id': obj.id, 'title': obj.title, 'body': obj.body},
        )
