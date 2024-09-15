from django import forms
from .models import MiningActivity, CarbonSink

class MiningActivityForm(forms.ModelForm):
    class Meta:
        model = MiningActivity
        fields = ['excavation', 'fuel_usage', 'machinery_details']

class CarbonSinkForm(forms.ModelForm):
    class Meta:
        model = CarbonSink
        fields = ['forest_area', 'tree_count', 'carbon_capture_tech']