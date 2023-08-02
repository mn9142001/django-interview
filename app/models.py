from django.db import models
import random
import string
from django.conf import settings

# Create your models here.
class Upload(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    image = models.ImageField()
    slug = models.CharField(max_length=12, unique=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.slugify()
        return super().save(*args, **kwargs)
    
    def slugify(self):
        self.slug = "".join(random.choices(string.ascii_lowercase, k=12))
        if self.__class__.objects.filter(slug=self.slug).exists():
            return self.slugify()
        