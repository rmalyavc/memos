from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url

app_name="memos"

urlpatterns = [
    path('', views.Index, name='Index'),
    # path('add_note/', views.AddNote, name='add_note'),
    # path('del_note/', views.DelNote, name='del_note'),
    path('memos/', views.memos, name='memos'),
    path('memo_del/', views.memo_del, name='memo_del')
    # path('accounts/login/', views.Login, name='Login'),
    # path('accounts/register/', views.Register, name='Register'),
]