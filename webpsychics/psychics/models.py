from django.db import models


class PsychicsModel(models.Model):
    
    name = models.CharField(max_length=80)
    
    class Meta:
        verbose_name = 'экстрасенсы'
        verbose_name_plural = 'экстрасенсы'

    
    def __str__(self):
        return self.name



