from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.conf import settings

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def clear_cache(sender, instance, **kwargs):
    user = instance
    lang_codes = [i[0] for i in settings.LANGUAGES]

    for lang_code in lang_codes:
        key = make_template_fragment_key("profile_page", [lang_code, user.username])
        cache.delete(key)
