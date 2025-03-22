import pandas as pd

df = pd.read_csv('/content/spectral signature_cotton_maddur.csv', header=None, delim_whitespace=True)  # Ensure correct parsing

data = {"wavelength": [], "reflectance": []}

for index, row in df.iterrows():
    data["wavelength"].append(float(row[0]))  # First column as wavelength
    data["reflectance"].append(float(row[1]))  # Second column as reflectance

import pandas as pd

# Create a DataFrame from the data dictionary
df_new = pd.DataFrame(data)

# Save the DataFrame to a new CSV file
df_new.to_csv('processed_data.csv', index=False)

print("New CSV file 'processed_data.csv' has been created successfully.")




import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
df = pd.read_csv('processed_data.csv')

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(df['wavelength'], df['reflectance'], marker='o', linestyle='-', color='b', label='Reflectance')

# Labels and title
plt.xlabel('Wavelength (nm)')
plt.ylabel('Reflectance')
plt.title('Wavelength vs Reflectance')
plt.legend()
plt.grid()

# Show the plot
plt.show()



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
