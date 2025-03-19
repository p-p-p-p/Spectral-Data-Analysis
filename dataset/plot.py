import numpy as np
import pandas as pd

# Load the CSV file
df = pd.read_csv('processed_data.csv')

# Moving average to smooth the curve
window_size = 5
df['smoothed_reflectance'] = df['reflectance'].rolling(window=window_size, center=True).mean()

plt.figure(figsize=(10, 5))
plt.plot(df['wavelength'], df['smoothed_reflectance'], linestyle='-', color='b', label='Smoothed Reflectance')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Reflectance')
plt.title('Smoothed Wavelength vs Reflectance')
plt.legend()
plt.grid()
plt.show()
