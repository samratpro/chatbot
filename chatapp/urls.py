from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('newchatpage/', views.new_chat, name='newchatpage'),
    path('chat/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('delete_chat/<chat_id>', views.delete_chat, name='delete_chat'),
    path('cookie_data/<chat_id>', views.cookie_data, name='cookie_data'),
    path('add_credit/', views.add_credit, name='add_credit'),
    path('profile/', views.profile, name='profile'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)