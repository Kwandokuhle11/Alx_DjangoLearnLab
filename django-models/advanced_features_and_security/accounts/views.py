from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

@permission_required('app_name.can_view', raise_exception=True)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

@permission_required('app_name.can_create', raise_exception=True)
def post_create(request):
    if request.method == 'POST':
        
        pass
    return render(request, 'post_form.html')

@permission_required('app_name.can_edit', raise_exception=True)
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        
        pass
    return render(request, 'post_form.html', {'post': post})

@permission_required('app_name.can_delete', raise_exception=True)
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')
