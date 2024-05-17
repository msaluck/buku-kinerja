# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import MasastudiIpkv2Lulusan
from django.core import serializers


def dashboard_with_pivot(request):
    return render(request, "dashboard_with_pivot.html", {})


# def pivot_data(request):
#     dataset = FactMasaStudi.objects.select_related(
#         "fakultas",
#         "dim_jurusankode_jurusan",
#         "dim_prodikode_prodi",
#         "dim_tahun_akadkode_tahun_akad",
#         "dim_mahasiswanim",
#         "dim_statuskode_status",
#     ).all()
#     dataset = dataset[:1]
#     hasil_iterasi = []
#     for data in dataset:
#         nama_fakultas = data.fakultas.namafak

#     data = serializers.serialize("json", dataset)
#     print(data)
#     return JsonResponse(data, safe=False)


def pivot_data(request):
    dataset = MasastudiIpkv2Lulusan.objects.all()
    data = serializers.serialize("json", dataset)
    return JsonResponse(data, safe=False)
