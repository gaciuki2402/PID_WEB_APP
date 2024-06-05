from django import forms

class PIDPredictionForm(forms.Form):
    AGE_CHOICES = [(i, str(i)) for i in range(18, 100)]
    YES_NO_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    NORMAL_ABNORMAL_CHOICES = [('Normal (US)', 'Normal (US)'), ('Abnormal (US)', 'Abnormal (US)')]
    LEVEL_CHOICES = [('Normal', 'Normal'), ('Elevated', 'Elevated')]

    age = forms.ChoiceField(choices=AGE_CHOICES)
    stds_uti_history = forms.ChoiceField(choices=YES_NO_CHOICES)
    iud_use = forms.ChoiceField(choices=YES_NO_CHOICES)
    past_pelvic_pain = forms.ChoiceField(choices=YES_NO_CHOICES)
    imaging_results = forms.ChoiceField(choices=NORMAL_ABNORMAL_CHOICES)
    abnormal_discharge = forms.CharField(max_length=100)
    irregular_periods = forms.ChoiceField(choices=YES_NO_CHOICES)
    dyspareunia = forms.ChoiceField(choices=YES_NO_CHOICES)
    dysuria = forms.ChoiceField(choices=YES_NO_CHOICES)
    wbc_count = forms.ChoiceField(choices=LEVEL_CHOICES)
    esr = forms.ChoiceField(choices=LEVEL_CHOICES)
    crp_level = forms.ChoiceField(choices=LEVEL_CHOICES)
