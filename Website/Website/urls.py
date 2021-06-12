from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.core.mail import send_mail
from Users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', user_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'),name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name = 'logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='Users/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='Users/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='Users/password_reset.html'), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='Users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='Users/password_reset_complete.html'), name='password_reset_complete'),
    
    path('', include('Contents.urls')),
    path('', include('pwa.urls')),

    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)