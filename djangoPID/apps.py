from django.apps import AppConfig
import joblib

class DjangopidConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangoPID'

    def ready(self):
        global pipeline
        pipeline = joblib.load('djangoPID\ml_model\PID_Model.joblib')