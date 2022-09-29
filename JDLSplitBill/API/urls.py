from django.urls import path

from .views import *


urlpatterns = [
    path("tagihan", TagihanListApiView.as_view(), name="add_getlist_tagihan"),
    path("tagihan/<str:pk>", TagihanDetailApiView.as_view(), name="get_update_delete_tagihan"),
    path("pesanan", PesananListApiView.as_view(), name="add_getlist_pesanan"),
    path("pesanan/<str:pk>", PesananDetailApiView.as_view(), name="get_update_delete_pesanan"),
    path("pemesan", PemesanListApiView.as_view(), name="add_getlist_pemesan"),
    path("pemesan/<str:pk>", PemesanDetailApiView.as_view(), name="get_update_delete_pemesan"),
]