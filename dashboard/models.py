# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DimAlumni(models.Model):
    nim = models.CharField(primary_key=True, max_length=32)
    namamhs = models.CharField(max_length=255, blank=True, null=True)
    periodewisuda = models.CharField(max_length=255, blank=True, null=True)
    alamatdomisili = models.CharField(max_length=255, blank=True, null=True)
    propinsidomisili = models.CharField(max_length=255, blank=True, null=True)
    kodestrata = models.ForeignKey(
        "DimStrata", models.DO_NOTHING, db_column="kodestrata"
    )
    tahunlulus = models.ForeignKey(
        "DimTahunlulus", models.DO_NOTHING, db_column="tahunlulus"
    )
    kodetahunakadkul = models.ForeignKey(
        "DimTahunakademik", models.DO_NOTHING, db_column="kodetahunakadkul"
    )
    kodenim = models.ForeignKey("DimProdi", models.DO_NOTHING, db_column="kodenim")
    peringkatlulus = models.ForeignKey(
        "DimPeringkatlulus", models.DO_NOTHING, db_column="peringkatlulus"
    )
    tahuntracer = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_alumni"


class DimFakultas(models.Model):
    kodefak = models.CharField(primary_key=True, max_length=255)
    namafak = models.CharField(max_length=255, blank=True, null=True)
    isfakultas = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.namafak)

    class Meta:
        managed = False
        db_table = "dim_fakultas"


class DimJenisstatus(models.Model):
    idstatus = models.CharField(primary_key=True, max_length=1)
    ketstatus = models.CharField(max_length=25, blank=True, null=True)
    idkodepdpt = models.CharField(max_length=2, blank=True, null=True)
    id_stat_mhs = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_jenisstatus"


class DimJurusan(models.Model):
    kodejurusan = models.CharField(primary_key=True, max_length=2)
    namajurusan = models.CharField(max_length=255, blank=True, null=True)
    kodefak = models.ForeignKey(DimFakultas, models.DO_NOTHING, db_column="kodefak")

    class Meta:
        managed = False
        db_table = "dim_jurusan"


class DimMahasiswa(models.Model):
    nim = models.CharField(primary_key=True, max_length=255)
    nama = models.CharField(max_length=255, blank=True, null=True)
    progkodenim = models.CharField(max_length=255, blank=True, null=True)
    tahunangkatan = models.SmallIntegerField(blank=True, null=True)
    kode_status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_mahasiswa"


class DimPeringkatlulus(models.Model):
    peringkatlulus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_peringkatlulus"


class DimPredikat(models.Model):
    namapredikat = models.CharField(primary_key=True, max_length=155)
    predikat_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_predikat"


class DimProdi(models.Model):
    kodenim = models.CharField(primary_key=True, max_length=255)
    namaprodi = models.CharField(max_length=255, blank=True, null=True)
    kodejurusan = models.ForeignKey(
        DimJurusan, models.DO_NOTHING, db_column="kodejurusan"
    )

    class Meta:
        managed = False
        db_table = "dim_prodi"


class DimProdiFakultas(models.Model):
    kodenim = models.CharField(primary_key=True, max_length=12)
    kodeprog = models.CharField(max_length=15, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=150, blank=True, null=True)
    jenisprodi = models.CharField(max_length=25, blank=True, null=True)
    namaprogdikti = models.CharField(max_length=150, blank=True, null=True)
    peringkatakreditasi = models.CharField(max_length=20, blank=True, null=True)
    kodejenjang = models.CharField(max_length=2, blank=True, null=True)
    namajenjang = models.CharField(max_length=20, blank=True, null=True)
    lamastudi = models.CharField(max_length=25, blank=True, null=True)
    kodefak = models.CharField(max_length=1, blank=True, null=True)
    namafakultas = models.CharField(max_length=100, blank=True, null=True)
    noskakreditasi = models.CharField(max_length=255, blank=True, null=True)
    tanggalakreditasi = models.DateField(blank=True, null=True)
    tanggalakhirakreditasi = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_prodi_fakultas"


class DimProgrammbkm(models.Model):
    idprogram = models.SmallIntegerField(primary_key=True)
    namaprogram = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_programmbkm"


class DimStatus(models.Model):
    kode_status = models.AutoField(primary_key=True)
    nama_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_status"


class DimStatusObsolete(models.Model):
    nim = models.CharField(max_length=9, blank=True, null=True)
    tanggaltransaksi = models.DateField(blank=True, null=True)
    kodetahunakadkul = models.CharField(max_length=12, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    idstatus = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_status-obsolete"


class DimStrata(models.Model):
    kodestrata = models.CharField(primary_key=True, max_length=2)
    strata = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_strata"


class DimSumberbiaya(models.Model):
    sumberbiaya = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_sumberbiaya"


class DimSumberdanambkm(models.Model):
    idsumberdana = models.SmallIntegerField(primary_key=True)
    sumberdana = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_sumberdanambkm"


class DimTahunAkad(models.Model):
    kode_tahun_akad = models.CharField(primary_key=True, max_length=255)
    nama_tahun_akad = models.CharField(max_length=255, blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    tgl_awal_sem = models.DateTimeField(blank=True, null=True)
    tgl_akhir_sem = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_tahun_akad"


class DimTahunakademik(models.Model):
    kodetahunakadkul = models.CharField(primary_key=True, max_length=12)
    tahunakademik = models.CharField(max_length=20, blank=True, null=True)
    id_smt = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_tahunakademik"


class DimTahunangkatan(models.Model):
    tahunangkatan = models.IntegerField(primary_key=True)
    namatahun = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_tahunangkatan"


class DimTahunlulus(models.Model):
    tahunlulus = models.IntegerField(primary_key=True)
    namatahun = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dim_tahunlulus"


class FactAnomalikelulusan(models.Model):
    nim = models.CharField(primary_key=True, max_length=255)
    kodetahunakadkul_lulus = models.CharField(max_length=255, blank=True, null=True)
    tanggal_lulus = models.DateField(blank=True, null=True)
    ipk_lulus = models.FloatField(blank=True, null=True)
    jmlsks_lulus = models.FloatField(blank=True, null=True)
    masastudi = models.FloatField(blank=True, null=True)
    namaprogstudi = models.CharField(max_length=255, blank=True, null=True)
    ipk_rekap = models.FloatField(blank=True, null=True)
    jmlsks_rekap = models.IntegerField(blank=True, null=True)
    namajenjang = models.CharField(max_length=255, blank=True, null=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    kodenim = models.CharField(max_length=255, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_anomalikelulusan"


class FactDimJmt(models.Model):
    nim = models.CharField(max_length=9, blank=True, null=True)
    noujian = models.CharField(max_length=25, blank=True, null=True)
    kodenim = models.ForeignKey(
        DimProdiFakultas, models.DO_NOTHING, db_column="kodenim", blank=True, null=True
    )
    idstatus = models.ForeignKey(
        DimJenisstatus, models.DO_NOTHING, db_column="idstatus", blank=True, null=True
    )
    tahunangkatan = models.CharField(max_length=4, blank=True, null=True)
    isbidikmisi = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_dim_jmt"


class FactIkad(models.Model):
    idkuispembelajaran = models.IntegerField(primary_key=True)
    jawabankuis = models.SmallIntegerField(blank=True, null=True)
    idmasterkuispembelajaran = models.IntegerField(blank=True, null=True)
    idmasterkuis = models.CharField(max_length=255, blank=True, null=True)
    isikuis = models.TextField(blank=True, null=True)
    nourut = models.CharField(max_length=255, blank=True, null=True)
    kodetahunakadkul = models.CharField(max_length=255, blank=True, null=True)
    waktusubmit = models.DateTimeField(blank=True, null=True)
    saran = models.TextField(blank=True, null=True)
    idgroupmengajarserial = models.IntegerField(blank=True, null=True)
    idkrskhsserial = models.IntegerField(blank=True, null=True)
    idjeniskuis = models.SmallIntegerField(blank=True, null=True)
    namajeniskuis = models.CharField(max_length=255, blank=True, null=True)
    nim = models.CharField(max_length=255, blank=True, null=True)
    namamhs = models.CharField(max_length=255, blank=True, null=True)
    namadosen = models.CharField(max_length=255, blank=True, null=True)
    kodekul = models.CharField(max_length=255, blank=True, null=True)
    namakulindo = models.CharField(max_length=255, blank=True, null=True)
    kodenim = models.CharField(max_length=255, blank=True, null=True)
    namaprogdikti = models.CharField(max_length=255, blank=True, null=True)
    kodejurusan = models.CharField(max_length=255, blank=True, null=True)
    namajurusan = models.CharField(max_length=255, blank=True, null=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_ikad"


class FactIpk(models.Model):
    nim = models.CharField(
        primary_key=True, max_length=255
    )  # The composite primary key (nim, kodetahunakadkul) found, that is not supported. The first column is selected.
    kodetahunakadkul = models.CharField(max_length=25)
    kodenim = models.CharField(max_length=25, blank=True, null=True)
    ip = models.FloatField(blank=True, null=True)
    skssem = models.IntegerField(blank=True, null=True)
    ipk = models.FloatField(blank=True, null=True)
    skstotal = models.IntegerField(blank=True, null=True)
    namamhs = models.CharField(max_length=255, blank=True, null=True)
    tahunangkatan = models.IntegerField(blank=True, null=True)
    kodefak = models.CharField(max_length=25, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)
    kodeprog = models.CharField(max_length=25, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=255, blank=True, null=True)
    jumlah = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_ipk"
        unique_together = (("nim", "kodetahunakadkul"),)


class FactJmt(models.Model):
    nim = models.CharField(
        primary_key=True, max_length=9
    )  # The composite primary key (nim, tglgenerate) found, that is not supported. The first column is selected.
    namamhs = models.CharField(max_length=250, blank=True, null=True)
    kodenim = models.ForeignKey(
        DimProdiFakultas, models.DO_NOTHING, db_column="kodenim", blank=True, null=True
    )
    tahunangkatan = models.CharField(max_length=4, blank=True, null=True)
    kodejeniskelamin = models.CharField(max_length=1, blank=True, null=True)
    isbidikmisi = models.BooleanField(blank=True, null=True)
    kewarganegaraan = models.CharField(max_length=3, blank=True, null=True)
    idstatus = models.ForeignKey(
        DimJenisstatus, models.DO_NOTHING, db_column="idstatus", blank=True, null=True
    )
    ketstatus = models.CharField(max_length=50, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=200, blank=True, null=True)
    kodejenjang = models.CharField(max_length=2, blank=True, null=True)
    namajenjang = models.CharField(max_length=20, blank=True, null=True)
    kodefak = models.CharField(max_length=1, blank=True, null=True)
    namafakultas = models.CharField(max_length=100, blank=True, null=True)
    tglgenerate = models.DateField()
    kodetahunakadkul = models.ForeignKey(
        DimTahunakademik,
        models.DO_NOTHING,
        db_column="kodetahunakadkul",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "fact_jmt"
        unique_together = (("nim", "tglgenerate"),)


class FactKelaskolaboratif(models.Model):
    id_smt = models.CharField(max_length=255, blank=True, null=True)
    kodetahunakadkul = models.CharField(max_length=255, blank=True, null=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)
    kodeprog = models.CharField(max_length=255, blank=True, null=True)
    namaprogdikti = models.CharField(max_length=255, blank=True, null=True)
    namajenjang = models.CharField(max_length=255, blank=True, null=True)
    idtemplatekurikulumserial = models.CharField(max_length=255, blank=True, null=True)
    kodekul = models.CharField(max_length=255, blank=True, null=True)
    namakulindo = models.CharField(max_length=255, blank=True, null=True)
    tahunkurik = models.CharField(max_length=255, blank=True, null=True)
    aktivitaspartisipatif = models.CharField(max_length=255, blank=True, null=True)
    hasilproyek = models.CharField(max_length=255, blank=True, null=True)
    kognitifpengetahuan = models.CharField(max_length=255, blank=True, null=True)
    bobottotal = models.CharField(max_length=255, blank=True, null=True)
    total = models.CharField(max_length=255, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_kelaskolaboratif"


class FactKetepatanlulus(models.Model):
    nim = models.CharField(primary_key=True, max_length=255)
    namamhs = models.CharField(max_length=255, blank=True, null=True)
    kodenim = models.CharField(max_length=255, blank=True, null=True)
    namajenjang = models.CharField(max_length=255, blank=True, null=True)
    namagelar = models.CharField(max_length=255, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=255, blank=True, null=True)
    kodeprog = models.CharField(max_length=255, blank=True, null=True)
    tahunangkatan = models.IntegerField(blank=True, null=True)
    tempatlahir = models.CharField(max_length=255, blank=True, null=True)
    tgllhrmhs = models.DateField(blank=True, null=True)
    alamatasalmhs = models.CharField(max_length=255, blank=True, null=True)
    namajeniskelamin = models.CharField(max_length=255, blank=True, null=True)
    agama = models.CharField(max_length=255, blank=True, null=True)
    masastudi = models.IntegerField(blank=True, null=True)
    masastudibulan = models.IntegerField(blank=True, null=True)
    masastuditahun = models.IntegerField(blank=True, null=True)
    tanggallulus = models.DateField(blank=True, null=True)
    tahunlulus = models.IntegerField(blank=True, null=True)
    ipk = models.FloatField(blank=True, null=True)
    jmlsks = models.IntegerField(blank=True, null=True)
    namapredikat = models.CharField(max_length=255, blank=True, null=True)
    namaayah = models.CharField(max_length=255, blank=True, null=True)
    namaibu = models.CharField(max_length=255, blank=True, null=True)
    wisudake = models.IntegerField(blank=True, null=True)
    noskyudisium = models.CharField(max_length=255, blank=True, null=True)
    kodetahunakadkul = models.CharField(max_length=255, blank=True, null=True)
    masastudihitung = models.FloatField(blank=True, null=True)
    tepatwaktu = models.IntegerField(blank=True, null=True)
    ipkrange = models.CharField(max_length=255, blank=True, null=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    predikat_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_ketepatanlulus"


class FactMasaStudi(models.Model):
    dim_fakultaskode_fak = models.ForeignKey(
        DimFakultas, models.DO_NOTHING, db_column="dim_fakultaskode_fak"
    )
    dim_jurusankode_jurusan = models.ForeignKey(
        DimJurusan, models.DO_NOTHING, db_column="dim_jurusankode_jurusan"
    )
    dim_prodikode_prodi = models.ForeignKey(
        DimProdi, models.DO_NOTHING, db_column="dim_prodikode_prodi"
    )
    dim_tahun_akadkode_tahun_akad = models.ForeignKey(
        DimTahunAkad,
        models.DO_NOTHING,
        unique=True,
        db_column="dim_tahun_akadkode_tahun_akad",
    )
    dim_mahasiswanim = models.ForeignKey(
        DimMahasiswa, models.DO_NOTHING, unique=True, db_column="dim_mahasiswanim"
    )
    dim_statuskode_status = models.ForeignKey(
        DimStatus, models.DO_NOTHING, db_column="dim_statuskode_status"
    )
    tahun_tempuh = models.FloatField(blank=True, null=True)
    bulan_tempuh = models.FloatField(blank=True, null=True)
    hari_tempuh = models.IntegerField(blank=True, null=True)
    ips = models.FloatField(blank=True, null=True)
    ipk = models.FloatField(blank=True, null=True)
    sks = models.IntegerField(blank=True, null=True)
    kumulatif_sks_nilai = models.IntegerField(blank=True, null=True)
    semester_ke = models.IntegerField(blank=True, null=True)
    jumlah_hari = models.IntegerField(blank=True, null=True)
    acc_yudisium = models.BooleanField(blank=True, null=True)
    acc_yudisium_at = models.DateTimeField(blank=True, null=True)
    acc_yudisium_by = models.CharField(max_length=255, blank=True, null=True)
    tahunlulus = models.SmallIntegerField(blank=True, null=True)

    @staticmethod
    def get_nama_fakultas():
        try:
            fakultas = DimFakultas.objects.get(
                kodefak=FactMasaStudi.dim_fakultaskode_fak
            )
            return fakultas.namafak
        except DimFakultas.DoesNotExist:
            return None

    class Meta:
        managed = False
        db_table = "fact_masa_studi"


class DataLulusanPerWisuda(models.Model):
    wisudake = models.IntegerField()
    jumlah = models.IntegerField()

    class Meta:
        managed = False
        db_table = "datalulusanperwisuda"
        verbose_name = "Data Lulusan Per Wisuda"
        verbose_name_plural = "Data Lulusan Per Wisuda"


class MasaStudiV2Kumulatif(models.Model):
    dim_mahasiswanim = models.CharField(max_length=255, primary_key=True)
    jumlah_hari = models.IntegerField()
    masa_studi = models.FloatField()
    ipk = models.FloatField()
    tahunlulus = models.IntegerField()
    nama_status = models.CharField(max_length=10, default="Lulus")
    tahunangkatan = models.IntegerField()
    namajenjang = models.CharField(max_length=255)
    namaprodi = models.CharField(max_length=255)
    namafak = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "masastudiv2_kumulatif"


class FactMasastudilulus(models.Model):
    nim = models.CharField(primary_key=True, max_length=255)
    tahunlulus = models.IntegerField(blank=True, null=True)
    jmlsks = models.FloatField(blank=True, null=True)
    ipk = models.FloatField(blank=True, null=True)
    masastudi = models.FloatField(blank=True, null=True)
    masastudibulantotal = models.IntegerField(blank=True, null=True)
    masastuditahun = models.IntegerField(blank=True, null=True)
    masastudibulan = models.IntegerField(blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=255, blank=True, null=True)
    namajenjang = models.CharField(max_length=255, blank=True, null=True)
    jumlah = models.IntegerField(blank=True, null=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    kodenim = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_masastudilulus"


class FactMatakuliah(models.Model):
    idtemplatekurikulumserial = models.IntegerField(
        primary_key=True
    )  # The composite primary key (idtemplatekurikulumserial, kodenim, kodetahunakadkul) found, that is not supported. The first column is selected.
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)
    kodeprog = models.CharField(max_length=255, blank=True, null=True)
    namaprogdikti = models.CharField(max_length=255, blank=True, null=True)
    kodenim = models.CharField(max_length=255)
    kodekul = models.CharField(max_length=255, blank=True, null=True)
    namakulindo = models.CharField(max_length=255, blank=True, null=True)
    namakuleng = models.CharField(max_length=255, blank=True, null=True)
    tahunkurik = models.SmallIntegerField(blank=True, null=True)
    sifat = models.CharField(max_length=255, blank=True, null=True)
    namasifat = models.CharField(max_length=255, blank=True, null=True)
    nourutkul = models.SmallIntegerField(blank=True, null=True)
    sks = models.SmallIntegerField(blank=True, null=True)
    semester = models.SmallIntegerField(blank=True, null=True)
    skstatapmuka = models.SmallIntegerField(blank=True, null=True)
    skspraktikum = models.SmallIntegerField(blank=True, null=True)
    skslapangan = models.SmallIntegerField(blank=True, null=True)
    isskripsi = models.BooleanField(blank=True, null=True)
    kodekelompokmk = models.CharField(max_length=255, blank=True, null=True)
    namakelompokmk = models.CharField(max_length=255, blank=True, null=True)
    is_mbkm = models.BooleanField(blank=True, null=True)
    is_mkdu = models.BooleanField(blank=True, null=True)
    kodetahunakadkul = models.CharField()

    class Meta:
        managed = False
        db_table = "fact_matakuliah"
        unique_together = (
            ("idtemplatekurikulumserial", "kodenim", "kodetahunakadkul"),
        )


class FactMbkm(models.Model):
    nim = models.CharField(max_length=255, blank=True, null=True)
    namamhs = models.CharField(max_length=255, blank=True, null=True)
    kodenim = models.CharField(max_length=255, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=255, blank=True, null=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)
    idkrskhsserial = models.BigIntegerField(primary_key=True)
    idjadwalserial = models.BigIntegerField(blank=True, null=True)
    kodehari = models.BigIntegerField(blank=True, null=True)
    idruangserial = models.BigIntegerField(blank=True, null=True)
    kodetahunakadkul = models.CharField(max_length=255, blank=True, null=True)
    idkelas = models.CharField(max_length=255, blank=True, null=True)
    indexnilai = models.CharField(max_length=255, blank=True, null=True)
    idpaketmbkm = models.BigIntegerField(blank=True, null=True)
    namapaket = models.CharField(max_length=255, blank=True, null=True)
    jenispaket = models.CharField(max_length=255, blank=True, null=True)
    namapaketmbkm = models.CharField(max_length=255, blank=True, null=True)
    nourut = models.SmallIntegerField(blank=True, null=True)
    kodekul = models.CharField(max_length=255, blank=True, null=True)
    namakulindo = models.CharField(max_length=255, blank=True, null=True)
    tahunkurik = models.SmallIntegerField(blank=True, null=True)
    sks = models.SmallIntegerField(blank=True, null=True)
    tahuniku = models.IntegerField(blank=True, null=True)
    idprogrammbkm = models.IntegerField(blank=True, null=True)
    namaprogrammbkm = models.CharField(blank=True, null=True)
    idjenisprogram = models.CharField(blank=True, null=True)
    jenisprogram = models.CharField(blank=True, null=True)
    idsumberpendanaan = models.IntegerField(blank=True, null=True)
    sumberpendanaan = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_mbkm"


class FactMhsbaru(models.Model):
    nim = models.CharField(
        primary_key=True, max_length=255
    )  # The composite primary key (nim, kodetahunakadkul) found, that is not supported. The first column is selected.
    namamhs = models.CharField(max_length=255, blank=True, null=True)
    tahunangkatan = models.CharField(max_length=255, blank=True, null=True)
    kodetahunakadkul = models.CharField(max_length=255)
    idstatus = models.CharField(max_length=255, blank=True, null=True)
    ketstatus = models.CharField(max_length=255, blank=True, null=True)
    kodenim = models.CharField(max_length=255, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=255, blank=True, null=True)
    jenisprodi = models.CharField(max_length=255, blank=True, null=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)
    mhsbaru = models.SmallIntegerField(blank=True, null=True)
    mhstransfer = models.SmallIntegerField(blank=True, null=True)
    mhsreguler = models.SmallIntegerField(blank=True, null=True)
    jumlah = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_mhsbaru"
        unique_together = (("nim", "kodetahunakadkul"),)


class FactPeminat(models.Model):
    tahun = models.IntegerField(
        primary_key=True
    )  # The composite primary key (tahun, namaprogstudi, jenispenerimaan) found, that is not supported. The first column is selected.
    kodenim = models.CharField(max_length=255, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=255)
    jenispenerimaan = models.CharField(max_length=255)
    peminat = models.IntegerField(blank=True, null=True)
    diterima = models.IntegerField(blank=True, null=True)
    registrasi = models.IntegerField(blank=True, null=True)
    dayatampung = models.IntegerField(blank=True, null=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_peminat"
        unique_together = (("tahun", "namaprogstudi", "jenispenerimaan"),)


class FactPengambilanmatakuliahmhs(models.Model):
    nim = models.CharField(
        primary_key=True, max_length=255
    )  # The composite primary key (nim, kodenim, tahunkurikulum, kodekul) found, that is not supported. The first column is selected.
    kodenim = models.CharField(max_length=255)
    tahunkurikulum = models.CharField(max_length=255)
    kodekul = models.CharField(max_length=255)
    namakulindo = models.CharField(max_length=255, blank=True, null=True)
    sifat = models.SmallIntegerField(blank=True, null=True)
    nourutkul = models.SmallIntegerField(blank=True, null=True)
    sks = models.SmallIntegerField(blank=True, null=True)
    semester = models.SmallIntegerField(blank=True, null=True)
    is_mkdu = models.BooleanField(blank=True, null=True)
    sudahdiambil = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_pengambilanmatakuliahmhs"
        unique_together = (("nim", "kodenim", "tahunkurikulum", "kodekul"),)


class FactPrestasi(models.Model):
    id = models.IntegerField(primary_key=True)
    nim = models.CharField(max_length=255, blank=True, null=True)
    namaprestasi = models.CharField(max_length=255, blank=True, null=True)
    jenisprestasi_id = models.IntegerField(blank=True, null=True)
    tingkatprestasi_id = models.IntegerField(blank=True, null=True)
    tahun_id = models.IntegerField(blank=True, null=True)
    penyelenggara = models.CharField(max_length=255, blank=True, null=True)
    peringkat = models.CharField(max_length=255, blank=True, null=True)
    aktivitasmahasiswa_id = models.IntegerField(blank=True, null=True)
    statusverifikasi_id = models.IntegerField(blank=True, null=True)
    tglverifikasi = models.DateTimeField(blank=True, null=True)
    namaverifikator = models.CharField(max_length=255, blank=True, null=True)
    tglprosesfeeder = models.DateTimeField(blank=True, null=True)
    id_prestasi = models.UUIDField(blank=True, null=True)
    tglinput = models.DateTimeField(blank=True, null=True)
    diinputoleh = models.CharField(max_length=255, blank=True, null=True)
    namajenisprestasi = models.CharField(max_length=255, blank=True, null=True)
    namatingkatprestasi = models.CharField(max_length=255, blank=True, null=True)
    namastatus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_prestasi"


class FactPrestasi2(models.Model):
    id = models.IntegerField(primary_key=True)
    nim = models.CharField(max_length=255, blank=True, null=True)
    namaprestasi = models.CharField(max_length=255, blank=True, null=True)
    jenisprestasi_id = models.IntegerField(blank=True, null=True)
    tingkatprestasi_id = models.IntegerField(blank=True, null=True)
    tahun_id = models.IntegerField(blank=True, null=True)
    penyelenggara = models.CharField(max_length=255, blank=True, null=True)
    peringkat = models.CharField(max_length=255, blank=True, null=True)
    aktivitasmahasiswa_id = models.IntegerField(blank=True, null=True)
    namajenisprestasi = models.CharField(max_length=255, blank=True, null=True)
    namatingkatprestasi = models.CharField(max_length=255, blank=True, null=True)
    semester_id = models.IntegerField(blank=True, null=True)
    jenisaktivitas_id = models.IntegerField(blank=True, null=True)
    namajenisaktivitas = models.CharField(max_length=255, blank=True, null=True)
    statusverifikasi_id = models.IntegerField(blank=True, null=True)
    namastatus = models.CharField(max_length=255, blank=True, null=True)
    judul = models.CharField(max_length=255, blank=True, null=True)
    lokasi = models.CharField(max_length=255, blank=True, null=True)
    nosk = models.CharField(max_length=255, blank=True, null=True)
    tanggalsk = models.DateField(blank=True, null=True)
    jenisanggota = models.CharField(max_length=255, blank=True, null=True)
    keterangan = models.CharField(max_length=500, blank=True, null=True)
    tanggalverifikasi = models.DateTimeField(blank=True, null=True)
    namaverifikator = models.CharField(max_length=255, blank=True, null=True)
    tglmulai = models.DateField(blank=True, null=True)
    tglselesai = models.DateField(blank=True, null=True)
    unitverifikator = models.CharField(max_length=255, blank=True, null=True)
    mbkm_id = models.IntegerField(blank=True, null=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)
    kodenim = models.CharField(max_length=255, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=255, blank=True, null=True)
    kodeprog = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_prestasi2"


class FactRasiodosenmhsv2(models.Model):
    kodenim = models.CharField(
        primary_key=True, max_length=25
    )  # The composite primary key (kodenim, kodetahunakadkul) found, that is not supported. The first column is selected.
    namaprogstudi = models.CharField(max_length=255, blank=True, null=True)
    kodefak = models.CharField(max_length=25, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)
    jmlmhsaktif = models.IntegerField(blank=True, null=True)
    jmldosenaktif = models.IntegerField(blank=True, null=True)
    tahunakademik = models.CharField(max_length=25, blank=True, null=True)
    kodetahunakadkul = models.CharField(max_length=25)
    kodejurusan = models.CharField(max_length=25, blank=True, null=True)
    namajursan = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_rasiodosenmhsv2"
        unique_together = (("kodenim", "kodetahunakadkul"),)


class FactRekapjmtpersemester(models.Model):
    kodetahunakadkul = models.CharField(max_length=255, blank=True, null=True)
    tahuniku = models.CharField(max_length=255, blank=True, null=True)
    kodenim = models.CharField(max_length=255, blank=True, null=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    jmt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_rekapjmtpersemester"


class FactSekolahmhs(models.Model):
    noujian = models.CharField(primary_key=True, max_length=50)
    kodekabupaten = models.CharField(max_length=10, blank=True, null=True)
    namakabupaten = models.CharField(max_length=100, blank=True, null=True)
    kodeprop = models.CharField(max_length=5, blank=True, null=True)
    namapropinsi = models.CharField(max_length=100, blank=True, null=True)
    tahunmasuk = models.IntegerField(blank=True, null=True)
    namamhs = models.CharField(max_length=200, blank=True, null=True)
    asalsma = models.CharField(max_length=150, blank=True, null=True)
    kodesma = models.CharField(max_length=10, blank=True, null=True)
    kodenim = models.ForeignKey(
        DimProdiFakultas, models.DO_NOTHING, db_column="kodenim", blank=True, null=True
    )
    kodeprog = models.CharField(max_length=10, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=150, blank=True, null=True)
    kodefak = models.CharField(max_length=2, blank=True, null=True)
    namafak = models.CharField(max_length=100, blank=True, null=True)
    jumlah = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_sekolahmhs"


class FactStatusObsolete(models.Model):
    nim = models.CharField(
        primary_key=True, max_length=9
    )  # The composite primary key (nim, kodetahunakadkul) found, that is not supported. The first column is selected.
    namamhs = models.CharField(max_length=250, blank=True, null=True)
    tahunangkatan = models.CharField(max_length=4, blank=True, null=True)
    isbidikmisi = models.BooleanField(blank=True, null=True)
    idstatus = models.ForeignKey(
        DimJenisstatus, models.DO_NOTHING, db_column="idstatus", blank=True, null=True
    )
    ketstatus = models.CharField(max_length=50, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=200, blank=True, null=True)
    namajenjang = models.CharField(max_length=20, blank=True, null=True)
    namafakultas = models.CharField(max_length=100, blank=True, null=True)
    tglcatat = models.DateField(blank=True, null=True)
    thncatat = models.FloatField(blank=True, null=True)
    kodetahunakadkul = models.ForeignKey(
        DimTahunakademik, models.DO_NOTHING, db_column="kodetahunakadkul"
    )
    status = models.CharField(max_length=25, blank=True, null=True)
    tanggaltransaksi = models.DateField(blank=True, null=True)
    bulantransaksi = models.CharField(max_length=25, blank=True, null=True)
    tahuntransaksi = models.FloatField(blank=True, null=True)
    tahunakademik = models.CharField(max_length=12, blank=True, null=True)
    jumlah = models.IntegerField(blank=True, null=True)
    kodenim = models.ForeignKey(
        DimProdiFakultas, models.DO_NOTHING, db_column="kodenim", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "fact_status-obsolete"
        unique_together = (("nim", "kodetahunakadkul"),)


class FactStatusmhs(models.Model):
    nim = models.CharField(
        primary_key=True, max_length=255
    )  # The composite primary key (nim, kodetahunakadkul) found, that is not supported. The first column is selected.
    tahunangkatan = models.IntegerField(blank=True, null=True)
    kodetahunakadkul = models.CharField(max_length=255)
    idstatus = models.CharField(max_length=255, blank=True, null=True)
    ketstatus = models.CharField(max_length=255, blank=True, null=True)
    kodenim = models.CharField(max_length=255, blank=True, null=True)
    kodeprog = models.CharField(max_length=255, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=255, blank=True, null=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)
    jml = models.IntegerField(blank=True, null=True)
    alamatasalmhs = models.TextField(blank=True, null=True)
    nohp = models.CharField(max_length=255, blank=True, null=True)
    emailunsoed = models.CharField(max_length=255, blank=True, null=True)
    emailayah = models.CharField(max_length=255, blank=True, null=True)
    emailibu = models.CharField(max_length=255, blank=True, null=True)
    nohpayah = models.CharField(max_length=255, blank=True, null=True)
    nohpibu = models.CharField(max_length=255, blank=True, null=True)
    namadosenpa = models.CharField(max_length=255, blank=True, null=True)
    tahuniku = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_statusmhs"
        unique_together = (("nim", "kodetahunakadkul"),)


class FactStatusmhsObsolete(models.Model):
    nim = models.CharField(
        primary_key=True, max_length=255
    )  # The composite primary key (nim, kodetahunakadkul) found, that is not supported. The first column is selected.
    tahunangkatan = models.IntegerField(blank=True, null=True)
    kodetahunakadkul = models.CharField(max_length=255)
    idstatus = models.CharField(max_length=255, blank=True, null=True)
    ketstatus = models.CharField(max_length=255, blank=True, null=True)
    kodenim = models.CharField(max_length=255, blank=True, null=True)
    kodeprog = models.CharField(max_length=255, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=255, blank=True, null=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)
    jml = models.IntegerField(blank=True, null=True)
    alamatasalmhs = models.TextField(blank=True, null=True)
    nohp = models.CharField(max_length=255, blank=True, null=True)
    emailunsoed = models.CharField(max_length=255, blank=True, null=True)
    emailayah = models.CharField(max_length=255, blank=True, null=True)
    emailibu = models.CharField(max_length=255, blank=True, null=True)
    nohpayah = models.CharField(max_length=255, blank=True, null=True)
    nohpibu = models.CharField(max_length=255, blank=True, null=True)
    namadosenpa = models.CharField(max_length=255, blank=True, null=True)
    tahuniku = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_statusmhs-obsolete"
        unique_together = (("nim", "kodetahunakadkul"),)


class FactStudentbody(models.Model):
    nim = models.CharField(primary_key=True, max_length=25)
    namamhs = models.CharField(max_length=255, blank=True, null=True)
    tahunmasuk = models.CharField(max_length=25, blank=True, null=True)
    namajeniskelamin = models.CharField(max_length=25, blank=True, null=True)
    kodenim = models.CharField(max_length=25, blank=True, null=True)
    namaprogstudi = models.CharField(max_length=255, blank=True, null=True)
    kodefak = models.CharField(max_length=25, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)
    kodekabupaten = models.CharField(max_length=25, blank=True, null=True)
    namakabupaten = models.CharField(max_length=255, blank=True, null=True)
    kodejeniskelamin = models.CharField(max_length=25, blank=True, null=True)
    ipk = models.FloatField(blank=True, null=True)
    jumlah = models.IntegerField(blank=True, null=True)
    jumlahlulus = models.IntegerField(blank=True, null=True)
    jumlahaktif = models.IntegerField(blank=True, null=True)
    namaujian = models.CharField(max_length=150, blank=True, null=True)
    kodejenjang = models.CharField(max_length=10, blank=True, null=True)
    namajenjang = models.CharField(max_length=50, blank=True, null=True)
    idstatus = models.CharField(max_length=25, blank=True, null=True)
    ketstatus = models.CharField(max_length=255, blank=True, null=True)
    nik = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_studentbody"


class FactTemplatematakuliah(models.Model):
    idtemplatekurikulumserial = models.SmallIntegerField(primary_key=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    namafakultas = models.CharField(max_length=255, blank=True, null=True)
    kodeprog = models.CharField(max_length=255, blank=True, null=True)
    namaprogdikti = models.CharField(max_length=255, blank=True, null=True)
    kodenim = models.CharField(max_length=255, blank=True, null=True)
    kodekul = models.CharField(max_length=255, blank=True, null=True)
    namakulindo = models.CharField(max_length=255, blank=True, null=True)
    namakuleng = models.CharField(max_length=255, blank=True, null=True)
    tahunkurik = models.SmallIntegerField(blank=True, null=True)
    sifat = models.CharField(max_length=255, blank=True, null=True)
    namasifat = models.CharField(max_length=255, blank=True, null=True)
    nourutkul = models.SmallIntegerField(blank=True, null=True)
    sks = models.SmallIntegerField(blank=True, null=True)
    semester = models.SmallIntegerField(blank=True, null=True)
    skstatapmuka = models.SmallIntegerField(blank=True, null=True)
    skspraktikum = models.SmallIntegerField(blank=True, null=True)
    skslapangan = models.SmallIntegerField(blank=True, null=True)
    isskripsi = models.BooleanField(blank=True, null=True)
    kodekelompokmk = models.CharField(max_length=255, blank=True, null=True)
    namakelompokmk = models.CharField(max_length=255, blank=True, null=True)
    is_mbkm = models.BooleanField(blank=True, null=True)
    is_mkdu = models.BooleanField(blank=True, null=True)
    jumlah = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_templatematakuliah"


class FactTracer(models.Model):
    pembuat = models.CharField(
        db_column="Pembuat", primary_key=True, max_length=500
    )  # Field name made lowercase.
    number_1769 = models.CharField(
        db_column="1769", max_length=500, blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    alamatasal = models.CharField(max_length=500, blank=True, null=True)
    alamatdomisili = models.CharField(max_length=500, blank=True, null=True)
    emailmsmh = models.CharField(max_length=500, blank=True, null=True)
    f1001 = models.CharField(max_length=500, blank=True, null=True)
    f1002 = models.CharField(max_length=500, blank=True, null=True)
    f1101 = models.CharField(max_length=500, blank=True, null=True)
    f1102 = models.CharField(max_length=500, blank=True, null=True)
    f1201 = models.CharField(max_length=500, blank=True, null=True)
    f1202 = models.CharField(max_length=500, blank=True, null=True)
    f14 = models.CharField(max_length=500, blank=True, null=True)
    f15 = models.CharField(max_length=500, blank=True, null=True)
    f1601 = models.CharField(max_length=500, blank=True, null=True)
    f1602 = models.CharField(max_length=500, blank=True, null=True)
    f1603 = models.CharField(max_length=500, blank=True, null=True)
    f1604 = models.CharField(max_length=500, blank=True, null=True)
    f1605 = models.CharField(max_length=500, blank=True, null=True)
    f1606 = models.CharField(max_length=500, blank=True, null=True)
    f1607 = models.CharField(max_length=500, blank=True, null=True)
    f1608 = models.CharField(max_length=500, blank=True, null=True)
    f1609 = models.CharField(max_length=500, blank=True, null=True)
    f1610 = models.CharField(max_length=500, blank=True, null=True)
    f1611 = models.CharField(max_length=500, blank=True, null=True)
    f1612 = models.CharField(max_length=500, blank=True, null=True)
    f1613 = models.CharField(max_length=500, blank=True, null=True)
    f1614 = models.CharField(max_length=500, blank=True, null=True)
    f1761 = models.CharField(max_length=500, blank=True, null=True)
    f1762 = models.CharField(max_length=500, blank=True, null=True)
    f1763 = models.CharField(max_length=500, blank=True, null=True)
    f1764 = models.CharField(max_length=500, blank=True, null=True)
    f1765 = models.CharField(max_length=500, blank=True, null=True)
    f1766 = models.CharField(max_length=500, blank=True, null=True)
    f1767 = models.CharField(max_length=500, blank=True, null=True)
    f1768 = models.CharField(max_length=500, blank=True, null=True)
    f1770 = models.CharField(max_length=500, blank=True, null=True)
    f1771 = models.CharField(max_length=500, blank=True, null=True)
    f1772 = models.CharField(max_length=500, blank=True, null=True)
    f1773 = models.CharField(max_length=500, blank=True, null=True)
    f1774 = models.CharField(max_length=500, blank=True, null=True)
    f18a = models.CharField(max_length=500, blank=True, null=True)
    f18b = models.CharField(max_length=500, blank=True, null=True)
    f18c = models.CharField(max_length=500, blank=True, null=True)
    f18d = models.CharField(max_length=500, blank=True, null=True)
    f21 = models.CharField(max_length=500, blank=True, null=True)
    f22 = models.CharField(max_length=500, blank=True, null=True)
    f23 = models.CharField(max_length=500, blank=True, null=True)
    f24 = models.CharField(max_length=500, blank=True, null=True)
    f25 = models.CharField(max_length=500, blank=True, null=True)
    f26 = models.CharField(max_length=500, blank=True, null=True)
    f27 = models.CharField(max_length=500, blank=True, null=True)
    f301 = models.CharField(max_length=500, blank=True, null=True)
    f302 = models.CharField(max_length=500, blank=True, null=True)
    f303 = models.CharField(max_length=500, blank=True, null=True)
    f401 = models.CharField(max_length=500, blank=True, null=True)
    f402 = models.CharField(max_length=500, blank=True, null=True)
    f403 = models.CharField(max_length=500, blank=True, null=True)
    f404 = models.CharField(max_length=500, blank=True, null=True)
    f405 = models.CharField(max_length=500, blank=True, null=True)
    f406 = models.CharField(max_length=500, blank=True, null=True)
    f407 = models.CharField(max_length=500, blank=True, null=True)
    f408 = models.CharField(max_length=500, blank=True, null=True)
    f409 = models.CharField(max_length=500, blank=True, null=True)
    f410 = models.CharField(max_length=500, blank=True, null=True)
    f411 = models.CharField(max_length=500, blank=True, null=True)
    f412 = models.CharField(max_length=500, blank=True, null=True)
    f413 = models.CharField(max_length=500, blank=True, null=True)
    f414 = models.CharField(max_length=500, blank=True, null=True)
    f415 = models.CharField(max_length=500, blank=True, null=True)
    f416 = models.CharField(max_length=500, blank=True, null=True)
    f502 = models.CharField(max_length=500, blank=True, null=True)
    f504 = models.CharField(max_length=500, blank=True, null=True)
    f505 = models.CharField(max_length=500, blank=True, null=True)
    f506 = models.CharField(max_length=500, blank=True, null=True)
    f5a1 = models.CharField(max_length=500, blank=True, null=True)
    f5a2 = models.CharField(max_length=500, blank=True, null=True)
    f5b = models.CharField(max_length=500, blank=True, null=True)
    f5c = models.CharField(max_length=500, blank=True, null=True)
    f5d = models.CharField(max_length=500, blank=True, null=True)
    f6 = models.CharField(max_length=500, blank=True, null=True)
    f7 = models.CharField(max_length=500, blank=True, null=True)
    f7a = models.CharField(max_length=500, blank=True, null=True)
    f8 = models.CharField(max_length=500, blank=True, null=True)
    h21 = models.CharField(max_length=500, blank=True, null=True)
    h31 = models.CharField(max_length=500, blank=True, null=True)
    h41 = models.CharField(max_length=500, blank=True, null=True)
    ijazahmsmh = models.CharField(max_length=500, blank=True, null=True)
    kdpstmsmh = models.CharField(max_length=500, blank=True, null=True)
    kdptimsmh = models.CharField(max_length=500, blank=True, null=True)
    kontakkeluarga = models.CharField(max_length=500, blank=True, null=True)
    nik = models.CharField(max_length=500, blank=True, null=True)
    nimhsmsmh = models.CharField(max_length=500, blank=True, null=True)
    nmmhsmsmh = models.CharField(max_length=500, blank=True, null=True)
    npwp = models.CharField(max_length=500, blank=True, null=True)
    slipgaji = models.CharField(max_length=500, blank=True, null=True)
    tahun_lulus = models.CharField(max_length=500, blank=True, null=True)
    telpomsmh = models.CharField(max_length=500, blank=True, null=True)
    kodefak = models.CharField(max_length=255, blank=True, null=True)
    namafak = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_tracer"


class FactTracerstudy(models.Model):
    id = models.BigAutoField(primary_key=True)
    nim = models.CharField(max_length=32)
    sumberbiaya = models.ForeignKey(DimSumberbiaya, models.DO_NOTHING)
    aktivitassaatini = models.CharField(max_length=255, blank=True, null=True)
    namauniversitas = models.CharField(max_length=255, blank=True, null=True)
    namaprodi = models.CharField(max_length=255, blank=True, null=True)
    jenjangpendidikan = models.CharField(max_length=255, blank=True, null=True)
    durasilulus_studilanjut = models.CharField(max_length=255, blank=True, null=True)
    isstudilanjut = models.SmallIntegerField(blank=True, null=True)
    pekerjaankurang6bulan = models.BooleanField(
        blank=True, null=True, db_comment="ya/tidak"
    )
    bulandapatpekerjaan = models.IntegerField(blank=True, null=True)
    namaperusahaan_instansi = models.CharField(max_length=255, blank=True, null=True)
    alamatperusahaan_instansi = models.CharField(max_length=255, blank=True, null=True)
    levelperusahaan = models.CharField(max_length=255, blank=True, null=True)
    bergerakdibidang = models.CharField(max_length=255, blank=True, null=True)
    gajipertama = models.CharField(max_length=255, blank=True, null=True)
    umktempatkerja = models.DecimalField(
        max_digits=19, decimal_places=0, blank=True, null=True
    )
    takehomepay = models.DecimalField(
        max_digits=19, decimal_places=0, blank=True, null=True
    )
    pendapatanperbulan_utama = models.DecimalField(
        max_digits=19, decimal_places=0, blank=True, null=True
    )
    pendapatanperbulan_tip_lembur = models.DecimalField(
        max_digits=19,
        decimal_places=0,
        blank=True,
        null=True,
        db_comment="dari tip atau lembur",
    )
    pendapatanperbulan_pekerjaanlain = models.DecimalField(
        max_digits=19, decimal_places=0, blank=True, null=True
    )
    isbekerja = models.SmallIntegerField(blank=True, null=True)
    jenisusaha = models.CharField(max_length=255, blank=True, null=True)
    namaperusahaan = models.CharField(max_length=255, blank=True, null=True)
    jabatansaatini = models.CharField(max_length=255, blank=True, null=True)
    alamattempatusaha = models.CharField(max_length=255, blank=True, null=True)
    levelusaha = models.CharField(
        max_length=255, blank=True, null=True, db_comment="regional/lokal"
    )
    berbadanhukum = models.BooleanField(blank=True, null=True, db_comment="ya/tidak")
    pendapatanperbulan = models.CharField(max_length=255, blank=True, null=True)
    umktempatusaha = models.DecimalField(
        max_digits=19, decimal_places=0, blank=True, null=True
    )
    iswiraswasta = models.SmallIntegerField(blank=True, null=True)
    jumlah = models.IntegerField(blank=True, null=True)
    tahuntracer = models.SmallIntegerField(blank=True, null=True)
    tanggaltracer = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fact_tracerstudy"
