from django.db import models
from django.contrib.auth.models import User
import string
import random

def generate_short_code(length=6):
    """Generate a unique random short code."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

class URL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)  # allow blank
    clicks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """Auto-generate unique short code if blank."""
        if not self.short_code:
            code = generate_short_code()
            while URL.objects.filter(short_code=code).exists():
                code = generate_short_code()
            self.short_code = code
        super().save(*args, **kwargs)

    def __str__(self):
        return self.short_code
