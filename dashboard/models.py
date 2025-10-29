from django.db import models
from django.utils import timezone


class District(models.Model):
    district_id = models.CharField(max_length=100, unique=True, primary_key=True)
    name_en = models.CharField(max_length=200)
    name_hi = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    class Meta:
        ordering = ['name_en']
    
    def __str__(self):
        return f"{self.name_en} ({self.name_hi})"


class MGNREGAData(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='mgnrega_records')
    month = models.CharField(max_length=20)
    employment_provided = models.IntegerField(default=0)
    payments_on_time = models.FloatField(default=0.0)
    avg_payment_delay_days = models.FloatField(default=0.0)
    active_projects = models.IntegerField(default=0)
    grievances_open = models.IntegerField(default=0)
    last_updated = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-month', 'district']
        unique_together = ['district', 'month']
    
    def __str__(self):
        return f"{self.district.name_en} - {self.month}"
