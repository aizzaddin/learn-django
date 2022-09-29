from rest_framework import serializers

from .models import Tagihan, Pesanan, Pemesan


class TagihanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tagihan
        fields = '__all__'


class PesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesanan
        fields = '__all__'


class PemesanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemesan
        fields = '__all__'

