from rest_framework import viewsets
from rest_framework import filters
from .models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("author",)

