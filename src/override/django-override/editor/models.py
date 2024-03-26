from django.db import models

# Create your models here.


class Override(models.Model):
    vendor_name = models.CharField(max_length=100)
    vendor_file_name = models.CharField(max_length=100)
    valid_from = models.DateField()
    valid_to = models.DateField()
    archival_date = models.DateField(null=True)
    key_field_name = models.CharField(max_length=80)
    key_field_value = models.CharField(max_length=200)
    value_field_name = models.CharField(max_length=200)
    value_field_current_value = models.CharField(max_length=200)
    value_field_new_value = models.CharField(max_length=200)
    description = models.TextField()
