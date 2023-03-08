from django.db import models

# Create your models here.

class Participant(models.Model):
    """Participant model."""
    full_name = models.CharField(max_length=255)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.full_name}'
    
    class Meta:
        verbose_name_plural = "Participantes"
        ordering = ('-points',)
