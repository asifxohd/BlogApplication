from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

class Blog(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    content = models.TextField()
    image = models.ImageField(
        upload_to='blog_images/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])] 
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
