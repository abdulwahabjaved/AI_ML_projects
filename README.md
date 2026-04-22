# 📈 Task 2: Predict Future Stock Prices (Short-Term)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![YFinance](https://img.shields.io/badge/YFinance-Stock%20Data-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📌 Objective
Use historical stock data of **Apple (AAPL)** to predict the next day's closing price using Machine Learning models.

---

## 📂 Dataset
| Property | Details |
|----------|---------|
| Source | Yahoo Finance via `yfinance` |
| Stock | Apple Inc. (AAPL) |
| Date Range | 2022-01-01 to 2024-01-01 |
| Features | Open, High, Low, Close, Volume |
| Target | Next day's Close Price |

---

## 🛠️ Libraries Used
| Library | Purpose |
|---------|---------|
| Pandas | Data handling |
| NumPy | Numerical operations |
| Matplotlib & Seaborn | Visualization |
| Scikit-learn | ML models |
| YFinance | Stock data fetching |

---

## 📊 What Was Done
- Downloaded Apple stock data using `yfinance` API
- Created target column using `.shift(-1)` for next day price
- Split data into Train & Test sets (80/20)
- Trained **Linear Regression** model
- Trained **Random Forest Regressor** model
- Plotted Actual vs Predicted prices
- Compared models using MAE, RMSE, R² Score
- Visualized Feature Importance

---

## 📈 Key Results
| Model | MAE | R² Score |
|-------|-----|---------|
| Linear Regression | Low | ~0.99 |
| Random Forest | Very Low | ~0.99 |

- ✅ Random Forest performed better than Linear Regression
- ✅ **Close Price** was the most important feature
- ✅ Both models closely followed actual price trends

---

## ▶️ How to Run

**Step 1:** Install libraries
```bash
pip install pandas numpy matplotlib seaborn scikit-learn yfinance
```

**Step 2:** Open notebook
```bash
jupyter notebook task2_stock.ipynb
```

**Step 3:** Run cells one by one using `Shift + Enter`

---

## 📁 File Structure
```
Task2-Stock/
├── task2_stock.ipynb   # Main Jupyter Notebook
└── README.md           # Task description
```
