#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from .forms import PubForm
from .models import Post,Category,Tag
from users.models import User
import markdown
from comments.forms import CommentForm



# Create your views here.

# 首页
# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request,'blog/index.html',{'post_list':post_list})

# 首页视图类
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    # 每页显示三篇文章
    paginate_by = 3



# 博客详情页
def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    form = CommentForm()
    comment_list = post.comment_set.all()

    return render (request, 'blog/detail.html', locals())

# 博客详情页视图类
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    # 复写 get方法，每次执行视图执行增加阅读量功能
    def get(self, request, *args, **kwargs):
        # 先调用父类的get方法，self.object属性中才会有Post模型的实例
        response = super().get(request, *args, **kwargs)
        # self.object的值就是被访问的文章对象post
        self.object.increase_views()
        # 返回response
        return response

    # 复写get_object,post的body值进行渲染为markdown
    def get_object(self, queryset=None):
        post = super().get_object(queryset=None)
        post.body = markdown.markdown(post.body,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ])

        return post

    # 复写get_context_data方法，拓展response中context的内容
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
         'form':form,
         'comment_list':comment_list
        })
        return context





# 归档视图
# def archives(request,year,month):
#     post_list = Post.objects.filter(created_time__year=year,
#                                   created_time__month=month).order_by('-created_time')
#     return render(request,'blog/index.html',locals())


# 归档视图类
class ArchivesView(IndexView):
    def get_queryset(self):
        year=self.kwargs.get('year')
        month=self.kwargs.get('month')
        return super().get_queryset().filter(created_time__year=year,created_time__month=month)

# 分类视图
# def category(request,pk):
#     cate=get_object_or_404(Category,pk=pk)
#     post_list=Post.objects.filter(category=cate).order_by('-created_time')
#     return render(request,'blog/index.html',locals())

# 分类视图类


class CategoryView (IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)


# 标签云视图类
class TagsView(IndexView):
    def get_queryset(self):
        tag = get_object_or_404(Tag,pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(tags=tag)



# 发布文章的视图函数
def post_pub(request,user_pk):
    # 获得登录的用户对象

    user=get_object_or_404(User,pk=user_pk)
    # 如果为post方法
    if request.method=='POST':
        form=PubForm(request.POST,request.FILES)
        # 如果表单内容合规
        if form.is_valid():
            # 创建文章对象，不保存到数据库
            post=form.save(commit=False)


            post.author=user

            # 保存文章表单数据到数据库,重定向当前页
            post.save()
            return redirect('/index/')
        else:

            # 将当前页面表单内容，文章，评论列表保存后，重新渲染页面
            context={

                'form':form,

            }
            return render(request,'blog/pub.html',context=context)
    else:
        # get访问时，刷新页面
        form = PubForm()
        return render(request,'blog/pub.html',locals())


