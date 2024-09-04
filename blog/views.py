from django.shortcuts import render, get_object_or_404
from django.views import generic
from blog.models import Post
from blog.forms import CommentForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "index.html"


def post_detail(request, pk):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(validated=True)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
