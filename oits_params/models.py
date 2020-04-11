from django.core.exceptions import ValidationError
from django.db import models
import uuid
import json

class OitsParams(models.Model):
    '''
    Represents a set of submitted parameters to OITS
    Parameters should be stored as JSON
    '''
    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
        ]

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
    created_at = models.DateTimeField(auto_now_add=True)


    def clean(self):
        '''
        Model validation
        '''

        # Make sure text deserializes
        try:
            params = json.loads(self.parameters)
        except Exception as e:
            raise ValidationError(e)

        if not isinstance(params['trajectory_optimization'], bool):
            raise ValidationError('trajectory_optimization must be true or false')

        if not isinstance(params['Nbody'], int) or params['Nbody'] <= 1:
            raise ValidationError('Nbodymust be an integer > 1')

        # blah, blah









