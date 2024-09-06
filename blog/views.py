from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Post
from blog.forms import CommentForm


def post_list(request):
    object_list = Post.objects.filter(status=1).order_by("-created_on")
    paginator = Paginator(object_list, 5)
    # 3 posts in each page
    page = request.GET.get("page")
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request, "index.html", {"page": page, "post_list": post_list})


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
