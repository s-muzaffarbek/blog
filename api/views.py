from django.contrib.auth import authenticate
from django.utils.text import slugify
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, TagSerializer, BlogSerializer, CommentSerializer
from blog.models import Category,Tag, Blog, Comment
from account.models import MyUser
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from .serializers.account import RegisterSerializer

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagModelViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class BlogListCreateAPIView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                image = request.data.get('image')
            )
            return Response({'mess': "yaratildi!"}),
        return Response({'mess': 'yaratilmadi'})

class BlogModelViewSet(ModelViewSet):
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data['slug'] = slugify(serializer.validated_data['title'])
        serializer.validated_data['user'] = self.request.user
        serializer.save()

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            username = user.username
            token = Token.objects.get(user=user).key
            return Response({'mess': f'{username} foydalanuvchi yaratildi',
                            'token': token})

        return Response({'error': 'Yaratilmadi'})

class LoginAPIView(APIView):
    def post(self, request):
        parser_class = JSONParser
        username = request.data['username']
        password = request.data['password']
        if username is None or password is None:
            return Response({'error': 'Passsword yoki username kiritilmadi'})
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Password yoki username xato'})
        token, created = Token.objects.get_or_create(user=user)
        return Response({'mess': 'siz login qildingiz!', 'token': str(token)})

