from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

def new_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", post_id=post.id)
    else:
        form = CommentForm()
    return render(request, "blog/new_comment.html", {"form": form, "post": post})

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail", post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, "blog/edit_comment.html", {"form": form, "comment": comment})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    comment.delete()
    return redirect("post_detail", post_id=post_id)






from django.shortcuts import render
from django.db.models import Q
from .models import Post, Tag

def search_posts(request):
    query = request.GET.get("q", "")
    results = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct()
    return render(request, "blog/search_results.html", {"results": results, "query": query})

def posts_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    posts = tag.posts.all()
    return render(request, "blog/posts_by_tag.html", {"tag": tag, "posts": posts})






from django.shortcuts import render

# Create your views here.
