import os
from django.shortcuts import render, redirect
from .forms import HospitalCostPredictionForm
import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import seaborn as sns
import matplotlib.pyplot as plt


def index(request):
    form = HospitalCostPredictionForm()
    prediction = None

    if request.method == 'POST':
        form = HospitalCostPredictionForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            marital_status = form.cleaned_data['martial_status']
            complaint = form.cleaned_data['complaint']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']

            # Process the form data
            age = int(age) if age else 0
            ms = 0 if marital_status == 'married' else 1
            weight = int(weight) if weight else 0
            height = int(height) if height else 0

            data = {
                'AGE': [age],
                'MARITAL STATUS': [ms],
                'KEY COMPLAINTS -CODE': [complaint],
                'BODY WEIGHT': [weight],
                'BODY HEIGHT': [height],
            }
            df = pd.DataFrame(data)
            model_file_path = os.path.join(os.path.dirname(__file__), 'linear_regression.pkl')
            model = joblib.load(model_file_path)
            predictions = model.predict(df)
            prediction = format(predictions[0], '.2f')
            return render(request, 'predict/index.html', {'form': form, 'prediction': prediction})
        else:
            return render(request, 'predict/index.html', {'form': form})

    return render(request, 'predict/index.html', {'form': form})

