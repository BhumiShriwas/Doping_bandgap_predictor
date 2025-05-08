import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("data/doping_data.csv")

# Split features and target
X = df[["atomic_number", "electronegativity"]]
y = df["bandgap_shift"]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Print the scaled features
print("Scaled Features:\n", X_scaled)
