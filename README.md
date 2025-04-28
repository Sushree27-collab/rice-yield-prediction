# 🌾 Rice Yield Prediction Under Hybrid CO₂ Conditions

Welcome to the **Rice Yield Prediction App**!  
This web application predicts rice grain yield based on important phenological parameters and experimental CO₂ conditions using a Machine Learning model (XGBoost).

---

## 📚 Project Overview

- **Objective:** Predict rice yield under different CO₂ conditions (current and projected)
- **Dataset:** Hybrid dataset combining experimental results
- **Machine Learning Model:** XGBoost Regressor (best performer)
- **Deployment:** Streamlit Cloud

---

## 🚀 Features

- Upload your own CSV file with phenological parameters
- Instant prediction of grain yield (kg/ha)
- Download predicted results in CSV format
- Easy-to-use and mobile-friendly

---

## 🛠️ How to Use

1. Click on **Upload File** button.
2. Upload a CSV file with the following columns:
   - `Panicle_Initiation`
   - `Anthesis`
   - `Physiological_Maturity`
   - `Runs`
   - `Condition_Encoded`
     - `0 = Current CO₂`
     - `1 = Projected CO₂`
3. View the predicted Grain Yield (kg/ha).
4. Download the results as a CSV file.

---

## 📂 Sample Input Format

| Panicle_Initiation | Anthesis | Physiological_Maturity | Runs | Condition_Encoded |
|:------------------:|:--------:|:----------------------:|:----:|:-----------------:|
| 45                 | 80       | 110                    | 1    | 0                 |
| 48                 | 82       | 112                    | 2    | 0                 |
| 52                 | 85       | 115                    | 3    | 1                 |
| 50                 | 78       | 109                    | 4    | 0                 |
| 47                 | 83       | 113                    | 5    | 1                 |

---

## 🧠 Technologies Used

- Python 3.11
- Streamlit
- XGBoost
- Scikit-learn
- LightGBM
- CatBoost
- Pandas
- Matplotlib
- Seaborn

---

## 👨‍💻 About the Author

Built with ❤️ by **Siya**.  
Machine Learning enthusiast, Agricultural Researcher, and Data Scientist.

---

## 📣 Acknowledgements

- Streamlit Community for easy app deployment
- Research team for providing experimental datasets
- Inspiration from field applications of AI in Agriculture
