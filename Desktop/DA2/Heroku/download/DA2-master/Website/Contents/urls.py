from django.urls import path
from . import views

app_name = 'Contents'
urlpatterns = [
    path('', views.PostList.as_view(), name='contents'),
    path('offline/', views.Offline.as_view(), name='offline'),
   
    path('giaynu/', views.List_giay_nu.as_view(),name='giaynu'),
    path('giaynam/', views.List_giay_nam.as_view(),name='giaynam'),
    path('giaybegai/', views.List_giay_begai.as_view(),name='begai'),

    path('productdetail/<slug>/', views.ProductDetail,name='productdetail'),
    path('addcart/<slug>/', views.themgiohang, name = 'addcart'),
    path('muangay/<slug>/', views.muangay, name = 'muangay'),
    
    path('giohang/', views.giohang, name = 'giohang'),
    path('themsoluongsanpham/<slug>/', views.themsoluongsanpham, name = 'themsoluongsanpham'),
    path('xoasoluongsanpham/<slug>/', views.xoasoluongsanpham, name = 'xoasoluongsanpham'),
    path('xoasanphamgiohang/<int:id>/', views.xoasanphamgiohang, name = 'xoasanphamgiohang'),
    path('thanhtoan/', views.thanhtoan, name = 'thanhtoan'),

    path('profile/', views.profile,name='profile'),
    path('Address/', views.Themdiachi,name='Address'),

    path('donmua/', views.donmua,name='donmua'),
    path('huydonhang/<int:pk>/', views.huydonhang, name = 'huydonhang'),
    path('chitietdonmua/<int:pk>', views.chitietdonmua,name='chitietdonmua'),
    
    path('danhgiasanpham/<slug>/', views.danhgiasanpham, name='danhgiasanpham'),
]