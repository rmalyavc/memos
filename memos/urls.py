from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name="memos"

urlpatterns = [
    path('', views.Index, name='Index'),
    path('memos/', views.memos, name='memos'),
    path('memo_del/', views.memo_del, name='memo_del'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
