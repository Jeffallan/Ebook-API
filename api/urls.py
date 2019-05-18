"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views import generic
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from api.apps.book.views import BookViewSet
from api.apps.author.views import AuthorViewSet
from api.apps.category.views import CategoryViewSet

router = DefaultRouter()
router.register(r'api/books', BookViewSet)
router.register(r'api/authors', AuthorViewSet)
router.register(r'api/categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^$', generic.RedirectView.as_view(url='api', permanent=False)),
    url(r'api/$', get_schema_view()),
    url('^', include(router.urls))   
]

