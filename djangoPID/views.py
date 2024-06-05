from django.shortcuts import render
from .forms import PIDPredictionForm
import pandas as pd
import joblib

# Function to load the model once when the server starts
pipeline = joblib.load('')

def predict_pid(age, stds_uti_history, iud_use, past_pelvic_pain, imaging_results, abnormal_discharge, irregular_periods, dyspareunia, dysuria, wbc_count, esr, crp_level):
    new_data = pd.DataFrame({
        'Age': [age],
        'STDs/UTI History': [stds_uti_history],
        'IUD Use': [iud_use],
        'Past Pelvic Pain': [past_pelvic_pain],
        'Imaging Results': [imaging_results],
        'Abnormal Discharge': [abnormal_discharge],
        'Irregular Periods': [irregular_periods],
        'Dyspareunia': [dyspareunia],
        'Dysuria': [dysuria],
        'WBC Count': [wbc_count],
        'ESR': [esr],
        'CRP Level': [crp_level]
    })
    return pipeline.predict(new_data)[0]

def predictions(request):
    if request.method == 'POST':
        form = PIDPredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            prediction = predict_pid(
                data['age'],
                data['stds_uti_history'],
                data['iud_use'],
                data['past_pelvic_pain'],
                data['imaging_results'],
                data['abnormal_discharge'],
                data['irregular_periods'],
                data['dyspareunia'],
                data['dysuria'],
                data['wbc_count'],
                data['esr'],
                data['crp_level']
            )
            result = "PID Positive" if prediction == 1 else "PID Negative"
            return render(request, 'pid_app/predictions.html', {'form': form, 'result': result})
    else:
        form = PIDPredictionForm()

    return render(request, 'djangoPID/predictions.html', {'form': form})

def index(request):
    return render(request, 'djangoPID/index.html')
