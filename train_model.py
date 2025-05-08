import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

# Step 1: Load dataset
df = pd.read_csv("data/doping_data.csv")

# Step 2: Feature-target split
X = df[["atomic_number", "electronegativity"]]
y = df["bandgap_shift"]

# Step 3: Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)



# Step 5: Model training using Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Model prediction
y_pred = model.predict(X_test)

# Step 7: Evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Step 8: Save model & scaler
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/trained_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("✅ Model and scaler saved in 'model/' folder.")


print("MAE:", mean_absolute_error(y_test, y_pred))

if len(y_test) > 1:
    print("R² Score:", r2_score(y_test, y_pred))
else:
    print("⚠️ R² Score not available (only 1 test sample).")


    

import matplotlib.pyplot as plt 
import os
os.makedirs("results", exist_ok=True)


# Plot actual vs predicted bandgap shifts
plt.scatter(y_test, y_pred, color='blue', alpha=0.7)
plt.xlabel("Actual Bandgap Shift")
plt.ylabel("Predicted Bandgap Shift")
plt.title("Doping Bandgap Shift Prediction")
plt.grid(True)
plt.show()
plt.savefig("results/bandgap_prediction_plot.png")
