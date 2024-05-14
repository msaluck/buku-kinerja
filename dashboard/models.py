from django.db import models


class Order(models.Model):
    product_category = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)


class FactMasaStudi(models.Model):
    dim_fakultaskode_fak = models.CharField(max_length=255)
    dim_jurusankode_jurusan = models.CharField(max_length=255)
    dim_prodikode_prodi = models.CharField(max_length=255)
    dim_tahun_akadkode_tahun_akad = models.CharField(max_length=255)
    dim_mahasiswanim = models.CharField(max_length=255)
