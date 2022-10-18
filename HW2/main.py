
import pandas as pd
import numpy as np

url = 'https://drive.google.com/file/d/1He5GI5_Gd8uXYfeETLBISQ5BszX0o4pU/view?usp=sharing'
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url, names=['index', 'gender', 'age', 'hypertension', 'heart_disease',
                               'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level',
                               'bmi', 'smoking_status', 'stroke'])
data = data.drop('index', axis=1)
print(data.head(10))

