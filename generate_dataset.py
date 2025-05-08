import pandas as pd
import random
import os

# Dopant element info (extended)
dopants = [
    {"dopant": "B",  "atomic_number": 5,  "electronegativity": 2.04},
    {"dopant": "N",  "atomic_number": 7,  "electronegativity": 3.04},
    {"dopant": "P",  "atomic_number": 15, "electronegativity": 2.19},
    {"dopant": "As", "atomic_number": 33, "electronegativity": 2.18},
    {"dopant": "Sb", "atomic_number": 51, "electronegativity": 2.05},
    {"dopant": "Al", "atomic_number": 13, "electronegativity": 1.61},
    {"dopant": "Ga", "atomic_number": 31, "electronegativity": 1.81},
    {"dopant": "In", "atomic_number": 49, "electronegativity": 1.78},
    {"dopant": "Tl", "atomic_number": 81, "electronegativity": 1.62},
    {"dopant": "Si", "atomic_number": 14, "electronegativity": 1.90}
]

# Generate synthetic data
data = []

for i in range(50):  # 50 samples
    dopant = random.choice(dopants)
    # Simulate bandgap shift: more electronegative → slightly increase, heavy atoms → reduce
    shift = round(random.uniform(-0.15, 0.1) + 0.02 * (dopant["electronegativity"] - 2.0), 4)
    data.append({
        "dopant": dopant["dopant"],
        "atomic_number": dopant["atomic_number"],
        "electronegativity": dopant["electronegativity"],
        "bandgap_shift": shift
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save the dataset
os.makedirs("data", exist_ok=True)
df.to_csv("data/doping_data.csv", index=False)

print("✅ Synthetic dataset saved to data/doping_data.csv")



