# 🌸 Task 1: Exploring and Visualizing the Iris Dataset

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📌 Objective
Load, inspect, and visualize the famous **Iris Dataset** to understand data trends, distributions, and relationships between features.

---

## 📂 Dataset
| Property | Details |
|----------|---------|
| Source | Seaborn built-in dataset |
| Rows | 150 |
| Columns | 5 |
| Target | Species (setosa, versicolor, virginica) |

---

## 🛠️ Libraries Used
| Library | Purpose |
|---------|---------|
| Pandas | Data loading and inspection |
| Matplotlib | Plotting and visualization |
| Seaborn | Statistical data visualization |

---

## 📊 What Was Done

### 1️⃣ Data Loading & Inspection
- Loaded dataset using `sns.load_dataset('iris')`
- Checked shape, column names using `.head()`
- Used `.info()` and `.describe()` for summary statistics

### 2️⃣ Exploratory Data Analysis (EDA)
- Checked unique species and their counts
- Identified missing values (none found)

### 3️⃣ Visualizations
| Plot | Purpose |
|------|---------|
| Scatter Plot | Relationship between Sepal & Petal features |
| Pairplot | All features compared at once |
| Histogram | Value distributions per species |
| Box Plot | Outlier detection per species |
| Heatmap | Correlation between features |

---

## 📈 Key Results
- ✅ **Setosa** is clearly separable from other species
- ✅ **Petal Length & Width** are highly correlated **(0.96)**
- ✅ **Sepal Width** has some outliers in Setosa
- ✅ No missing values found in dataset

---

## ▶️ How to Run

**Step 1:** Install required libraries
```bash
pip install pandas matplotlib seaborn
```

**Step 2:** Open notebook
```bash
jupyter notebook task1_iris.ipynb
```

**Step 3:** Run cells one by one using `Shift + Enter`

---

## 📁 File Structure
```
Task1-Iris/
├── task1_iris.ipynb   # Main Jupyter Notebook
└── README.md          # Task description
```
