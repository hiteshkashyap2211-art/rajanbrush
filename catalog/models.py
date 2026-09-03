from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100) # e.g., Wall Brushes, Industrial
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200) # e.g., Rajan Super Grip 4-Inch
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/')
    size_in_inches = models.CharField(max_length=50, help_text="e.g., 2 Inch, 3 Inch, 4 Inch")
    filament_type = models.CharField(max_length=100, default="Synthetic Bristle")
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"