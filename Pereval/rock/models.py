from django.db import models
from rock.func import get_path_upload_photos


class User(models.Model):
    email = models.EmailField()
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['email'], name="user_unique")]
    def __str__(self):
        return f"{self.fam} {self.name} {self.otc}"


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    def __str__(self):
        return f"широта: {self.latitude}, долгота: {self.longitude}, высота: {self.height}"

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"


class Level(models.Model):
    winter = models.CharField(max_length=10, verbose_name='Зима', null=True, blank=True)
    summer = models.CharField(max_length=10, verbose_name='Лето', null=True, blank=True)
    autumn = models.CharField(max_length=10, verbose_name='Осень', null=True, blank=True)
    spring = models.CharField(max_length=10, verbose_name='Весна', null=True, blank=True)

    def __str__(self):
        return f"зима: {self.winter}, весна: {self.spring}, лето: {self.summer}, осень: {self.autumn}"

    class Meta:
        verbose_name = "Уровень сложности"
        verbose_name_plural = "Уровни сложности"


class Pereval(models.Model):
    STATUS_CHOICES = [
        ("new", "новый"),
        ("pending", "в работе"),
        ("accepted", "принят"),
        ("rejected", "отклонен"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    beauty_title = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True, verbose_name='Название вершины')
    other_titles = models.TextField(blank=True, null=True,verbose_name='Другое название' )
    connect = models.TextField(blank=True, null=True)
    add_time = models.TimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.pk}: {self.beauty_title}"

    class Meta:
        verbose_name = "pereval_added"
        verbose_name_plural = "Перевалы"

    def create_pereval(self, pereval_data):
        pereval_object = self.create(**pereval_data)
        pereval_object.status = "new"
        pereval_object.save()
        return pereval_object


class Image(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    data = models.ImageField(upload_to=get_path_upload_photos, verbose_name='Изображение', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}: {self.title}"

    class Meta:
        verbose_name = "Фотографии"
