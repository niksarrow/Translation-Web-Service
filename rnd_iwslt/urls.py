"""rnd_iwslt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import  path
from translation.views import myView, pageView, addTodo, deleteTodo, translate, wix, index, yourName, deleteAll
from translation.views import translateUnmt, deleteAllUnmt, deleteUnmt, sampleText, pdfView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('translation/', myView),
    path('page/', pageView),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('deleteUnmt/<int:unmt_id>/', deleteUnmt),
    path('translate/', translate),
    path('translate_unmt/', translateUnmt),
    path('index/', index),
    path('wix/', wix),
    path('your_name/', yourName),
    path('deleteAll/', deleteAll),
    path('deleteAllUnmt/', deleteAllUnmt),
    path('sampleText/<str:type>/', sampleText),
    path('pdfView/', pdfView),
]
