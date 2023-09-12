from django.db import models
import uuid

# Create your models here.
class AdCopy(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    user_input = models.CharField(max_length=255)
    generated_text = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)