from django.db import models

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.file.name