from django.urls import path
from .views import IndexView, paginaEmConstrucaoView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('paginaEmConstrucao/', paginaEmConstrucaoView.as_view(), name='paginaEmConstrucao'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)