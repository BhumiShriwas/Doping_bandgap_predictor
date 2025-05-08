 🧪 Doping Bandgap Shift Predictor

A lightweight machine learning project to predict the **bandgap shift ** in semiconductor materials caused by doping. Designed for research applications in **solid-state physics**, particularly within defense R&D contexts like DRDO.


 🔍 Project Objective

This project simulates how different dopants (like Boron, Nitrogen, Phosphorus) affect the **electronic bandgap** of materials. Using features such as **atomic number** and **electronegativity**, it predicts the expected shift in bandgap using ML regression models.


 🧰 Tech Stack

- **Language:** Python 3.10+
- **Libraries:**  
  - `pandas`, `numpy` – Data handling  
  - `scikit-learn` – Machine learning  
  - `matplotlib` – Visualization  
  - `joblib` – Model saving/loading  
  - `streamlit` – Web UI



 🗂️ Project Structure
Doping_bandgap_predictor/
├── data/ # Synthetic dataset (CSV)
├── model/ # Trained model and scaler
├── app/ # Streamlit app
├── generate_dataset.py # Script to create synthetic data
├── preprocess_data.py # Preprocess features
├── train_model.py # Train & evaluate ML model
└── README.md    # This file  



---

## 🧠 Tech Stack

- Python 3.10
- scikit-learn
- pandas, matplotlib
- Streamlit
- joblib



 ⚙️ Setup Instructions

 🔹 1. Clone the Repository

git clone https://github.com/BhumiShriwas/Doping_bandgap_predictor.git
cd doping-bandgap-predictor 

🔹 2. Run the App

streamlit run app/streamlit_app.py 


📈 Sample Visualization
The model predicts bandgap shifts and can visualize predicted vs. actual values: 


🤖 Machine Learning Details
Input Features:

Atomic Number

Electronegativity

Target:

Bandgap Shift (ΔE)

Models Tried:

Linear Regression

Random Forest Regressor

Performance Metrics:

MAE (Mean Absolute Error)

R² Score (Coefficient of Determination)


📌 Use Cases
Pre-screen dopants for semiconductors or insulators

Assist in material design with AI tools

Integrate ML in solid-state device simulation pipelines


👨‍💻 Author
Bhumika Shriwas
2nd Year CSE (AI) student 
GitHub: @BhumiShriwas


