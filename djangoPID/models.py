from django.db import models

from django.db import models

class PIDData(models.Model):
    age = models.IntegerField()
    stds_uti_history = models.CharField(max_length=100)
    iud_use = models.CharField(max_length=100)
    past_pelvic_pain = models.CharField(max_length=100)
    imaging_results = models.CharField(max_length=100)
    abnormal_discharge = models.CharField(max_length=100)
    irregular_periods = models.CharField(max_length=100)
    dyspareunia = models.CharField(max_length=100)
    dysuria = models.CharField(max_length=100)
    wbc_count = models.CharField(max_length=100)
    esr = models.CharField(max_length=100)
    crp_level = models.CharField(max_length=100)
