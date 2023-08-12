from django.urls import path
from App1 import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from . forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

from django.conf.urls.static import static
urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('search/', views.search, name='search'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name = 'App1/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name = 'App1/passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='App1/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='App1/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='App1/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='App1/password_reset_complete.html'), name='password_reset_complete'),
    path('Action/', views.Action, name='Action'),
    path('Romance/', views.Romance, name='Romance'),
    path('Action/<slug:data>', views.Action, name='Actionitem'),
    path('Romance/<slug:data>', views.Romance, name='Romanceitem'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='App1/login.html',authentication_form=LoginForm), name='login'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    #path('',views.ind, name='index'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)