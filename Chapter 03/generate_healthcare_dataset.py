
import pandas as pd
import numpy as np

np.random.seed(42)  # Setting the random seed for reproducibility
n_samples = 1000  # Number of samples

# Generating random data for the given parameters
df = pd.DataFrame({
    'pregnancies': np.random.randint(0, 18, n_samples),  # Assuming a range from 0 to 17 pregnancies
    'glucose': np.random.randint(50, 200, n_samples),    # Random glucose levels between 50 and 200 mg/dL
    'blood_pressure': np.random.randint(60, 140, n_samples),  # Random blood pressure values (in mmHg)
    'skin_thickness': np.random.randint(10, 60, n_samples),  # Random skin thickness (in mm)
    'insulin': np.random.randint(10, 300, n_samples),   # Random insulin levels
    'bmi': np.random.uniform(15, 45, n_samples),   # Random BMI values
    'DPF': np.random.uniform(0.1, 2.0, n_samples),  # Random pedigree function values
    'age': np.random.randint(20, 80, n_samples),  # Random ages between 20 and 80
})

# Adding the disease_present column based on the conditions specified
df['disease_present'] = np.where(
    (df['glucose'] < 70) | 
    (df['glucose'] > 130) | 
    (df['blood_pressure'] < 80) | 
    (df['blood_pressure'] > 130), 
    1, 0)

# Save the dataset to a CSV file
df.to_csv('healthcare_dataset.csv', index=False)
