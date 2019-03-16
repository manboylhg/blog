from django.shortcuts import render
from apps.myblog.models import Article
from comment.models import Comment
from comment.form import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.conf import settings


def home(request):  # 主页
    posts = Article.objects.all()  # 获取全部的Article对象
    paginator = Paginator(posts, settings.PAGE_NUM)  # 每页显示数量，对应settings.py中的PAGE_NUM
    page = request.GET.get('page')  # 获取URL中page参数的值
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):  # 查看文章详情
    try:
        post = Article.objects.get(id=str(id))
        post.viewed()   # 更新浏览次数
        tags = post.tags.all()  # 获取文章对应所有标签
        form = CommentForm()
        comments = post.comment_set.all()

    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post, 'tags': tags, 'form': form, 'comments': comments})


def category_art(request, type):  #按文章分类显示
    posts = Article.objects.filter(category__name=type)  # 获取全部 category 为type 的文章
    paginator = Paginator(posts, settings.PAGE_NUM)  # 每页显示数量，对应settings.py中的PAGE_NUM
    page = request.GET.get('page')  # 获取URL中page参数的值
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})

def tag_art(request,tag_type):
    posts = Article.objects.filter(tag__name=tag_type)  # 获取全部 tag 为type 的文章
    paginator = Paginator(posts, settings.PAGE_NUM)  # 每页显示数量，对应settings.py中的PAGE_NUM
    page = request.GET.get('page')  # 获取URL中page参数的值
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})
