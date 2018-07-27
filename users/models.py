from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


def upload_to(instance, filename):
    return '%s/%s/%s' %('profile_photo', instance.user.username, filename)


class UserProfile(models.Model):
    ERKEK = 'E'
    KIZ = 'K'
    OTHER = 'O'
    CINSIYET = ((ERKEK, 'Erkek'),(KIZ, 'Kız'),(OTHER, 'Other'))

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    telefon_numarasi = models.CharField(max_length=11, verbose_name='Telefon Numarası', blank=True, null=True)
    cinsiyet = models.CharField(max_length=1, default=3, verbose_name='Cinsiyet', choices=CINSIYET, blank=True)
    dogum = models.DateField(blank=True, verbose_name='Doğum tarihi', null=True)
    profil_photo = models.ImageField(upload_to=upload_to, verbose_name='Profil Fotoğrafı', default='profile_photo/default.png')

    class Meta:
        verbose_name='Profil'
        verbose_name_plural='Profil'

    def get_full_name_or_username(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        return self.user.username

    def __str__(self):
        return '%s Profile'%(self.user.get_full_name_or_username())

def created_user_profile(instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(receiver=created_user_profile, sender=User)
#signal işlemi bir işlemden sonra başka bir işlem yaptırmak istiyorsam kullanılır. Örneğin kullanıcı oluşturduktan sonra profilini oluşturmak gibi.