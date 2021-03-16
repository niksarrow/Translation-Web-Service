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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import  path
from translation.views import myView, pageView, addTodo, deleteTodo, translate, index, yourName, deleteAll
from translation.views import fluent_translate, translateUnmt, deleteAllUnmt, deleteUnmt, sampleText, pdfView
from translation.views import deleteAllDC, deleteDC
import translation.views as views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    path('fluenttrans', views.fluent_translate, name='fluent_translate'),
    path('fluenttrans/sampleText/<str:type>/', sampleText),
]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
