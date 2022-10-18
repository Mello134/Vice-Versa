"""viceversa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from django.contrib import admin - удалили админку потому что не пользуемся
from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ] - всё то что удалилил

from . import views #импорт из корневой папки модуль/файл views.py

urlpatterns = [
    path('', views.home),
    path('les/', views.lessons),
    path('reverse/', views.reverse, name='reverse')
]
#это ссылки - путь('что вводим в браузере', функция из файла/модуля vievs.название функции)
#path('url', файл/модуь.функция, name='имя')