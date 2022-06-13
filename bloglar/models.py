from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
#timezone ile bulunan konuma göre zaman çekiliyor

class blog(models.Model):
   tipler = (
        ('Saglik', 'Sağlık'),
        ('Egitim', 'Eğitim'),
        ('Spor', 'Spor'),
    )
   baslik = models.CharField(max_length = 200)
   konu = models.TextField()
   resim =  models.ImageField(upload_to ='uploads/% Y/% m/% d/')
   kategori=models.CharField(max_length=10, choices=tipler)
   tarih=models.DateTimeField(auto_now=True)
   #tarihin otomatik zamanı çekmesi için burada
   #auto_now true komutunu kullanıyoruz.
   #veritabanında oluşacak model dosyası

   def __str__(self):
        return self.baslik
        #admin panelinde gözükecek kısımlar
   