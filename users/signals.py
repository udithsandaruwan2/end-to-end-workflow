from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

# @receiver(post_save, sender=Profile)
# def update_user_from_profile(sender, instance, **kwargs):
#     user = instance.user

#     # Example: sync fields (adjust based on your model)
#     user.first_name = instance.first_name
#     user.last_name = instance.last_name

#     # IMPORTANT: prevent infinite loop
#     user.save(update_fields=["first_name", "last_name"])

        