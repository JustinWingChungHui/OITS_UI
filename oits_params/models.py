from django.db import models
import uuid

# Create your models here.
class OitsParams(models.Model):

    NEW = 'N'
    PROCESSING = 'P'
    COMPLETE = 'C'
    STATUS_CHOICES = [
        ('N', 'New'),
        ('P', 'Processing'),
        ('C', 'Complete'),
    ]

    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=NEW,
    )

    parameters = models.TextField()



