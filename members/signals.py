from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Member, MembershipNumber


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    # print('sender', sender)
    # print('instance', instance)
    if created:
        Member.objects.create(user=instance,
                              first_name=instance.first_name,
                              last_name=instance.last_name,
                              email=instance.email)
