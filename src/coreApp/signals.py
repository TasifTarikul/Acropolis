from .models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from userProfileApp.models import AcropolisModel, SarawakModel, VisaModel


@receiver(post_save, sender=User)
def create_model_object(sender, instance, created, **kwrgs):
    if created:
        if instance.is_superuser and instance.is_staff:
            return None
        else:
            AcropolisModel.objects.create(user_profile=instance)
            SarawakModel.objects.create(user_profile=instance)
            VisaModel.objects.create(user_profile=instance)

