from .models import Category, Tag

def category(request):
    categories = Category.objects.all()

    return {'categories': categories}

def tag(request):
    tags = Tag.objects.all()
    return {'tags': tags}