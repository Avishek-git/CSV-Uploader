from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return 'uploads/{}'.format(filename)

class UploadedFile(models.Model):
    csv_file = models.FileField(upload_to=upload_to)