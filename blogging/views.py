from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from blogging.forms import PostForm
from django.utils import timezone


class PostListView(ListView):
    model = Post
    template_name = "blogging/list.html"

    def get_queryset(self):
        return Post.objects.exclude(published_date__exact=None).order_by(
            "-published_date"
        )


class PostDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = Post.objects.exclude(published_date__exact=None)
        pk = self.kwargs.get("pk")
        try:
            post = queryset.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404("not exist or published")

        return post


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


@login_required
def add_modelform(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return HttpResponseRedirect("/")
    else:
        form = PostForm()
    return render(request, "blogging/add.html", {"form": form})
