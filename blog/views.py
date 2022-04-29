from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import View
from django.views.generic import DetailView, UpdateView, DeleteView, ListView

from .forms import BlogForm, CommentForm
from .models import Blog, Comment, Category, Tag


class CategoryView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category_list.html'


class BlogView(View):
    def get(self, request):
        context = {}
        blogs = Blog.objects.all()
        context['blogs'] = blogs
        return render(request, 'blog_list.html', context)


class CategoryBlogView(View):
    def get(self, request, slug):
        context = {}
        category = Category.objects.get(slug=slug)
        blogs = Blog.objects.filter(category=category)
        context['blogs'] = blogs
        context['category'] = category
        return render(request, 'blog_list.html', context)


class BlogCreateVeiw(View):
    def get(self, request, *args, **kwargs):
        form = BlogForm()
        return render(request, 'blog_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.user = request.user
            form2.slug = slugify(form2.title)
            form2.save()
            form.save_m2m()
            return redirect('blog_list')
        return render(request, 'blog_create.html', {'form': form})


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        comments = Comment.objects.filter(blog=self.object)
        context['comments'] = comments
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        obj = super().get_object()
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.blog = obj
            form2.user = request.user
            form2.save()
            return redirect('blog_detail', obj.slug)


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog_update.html'
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        title = self.request.POST['title']
        form.instance.slug = slugify(title)

        return super(BlogUpdateView, self).form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog_list')


class TagView(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        blogs = Blog.objects.filter(tags=tag)
        context = {
            'tag': tag,
            'blogs': blogs
        }
        return render(request, 'tag_blog_list.html', context)
