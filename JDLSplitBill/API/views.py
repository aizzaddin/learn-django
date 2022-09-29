from rest_framework import generics


from .models import Tagihan, Pesanan, Pemesan
from .serializers import TagihanSerializer, PesananSerializer, PemesanSerializer


class TagihanListApiView(generics.ListCreateAPIView):
    queryset = Tagihan.objects.all()
    serializer_class = TagihanSerializer


class TagihanDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tagihan.objects.all()
    serializer_class = TagihanSerializer


class PesananListApiView(generics.ListCreateAPIView):
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer


class PesananDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer


class PemesanListApiView(generics.ListCreateAPIView):
    queryset = Pemesan.objects.all()
    serializer_class = PemesanSerializer


class PemesanDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pemesan.objects.all()
    serializer_class = PemesanSerializer

