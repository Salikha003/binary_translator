from django.db import models

class BinaryTranslation(models.Model):
    binary_code = models.CharField(max_length=200)
    translated_text = models.TextField()
