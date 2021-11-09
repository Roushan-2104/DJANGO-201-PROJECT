from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    image = ImageField(default='profiles/default_rWpNfNs.jpg',upload_to='profiles')
    bg_image = ImageField(default='bg_image/back_default.jpg',upload_to='bg_image')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)