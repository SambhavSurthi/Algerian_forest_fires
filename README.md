# Algerian Forest Fires Dataset Analysis

A comprehensive data science project analyzing forest fire data from two regions in Algeria using machine learning and statistical techniques.

## 📋 Project Overview

This project analyzes the **Algerian Forest Fires Dataset**, containing fire data from two regions:
- **Bejaia Region**
- **Sidi-Bel Abbes Region**

The analysis includes data cleaning, exploratory data analysis (EDA), feature engineering, and predictive modeling for both regression and classification tasks.

## 📊 Dataset

### Features
**Input Features (11):**
- `day` - Day of the month
- `month` - Month of the year
- `year` - Year of observation
- `Temperature` - Temperature in °C
- `RH` - Relative Humidity (%)
- `Ws` - Wind Speed (km/h)
- `Rain` - Rainfall (mm)
- `FFMC` - Fine Fuel Moisture Code
- `DMC` - Duff Moisture Code
- `DC` - Drought Code
- `ISI` - Initial Spread Index

**Target Features:**
- `FWI` - Fire Weather Index (for regression)
- `Classes` - Fire/Not Fire classification (for classification)
- `BUI` - Buildup Index

### Files
- `Algerian_forest_fires_dataset.csv` - Original raw dataset
- `Algerian_forest_fires_cleaned_dataset.csv` - Cleaned and processed dataset

## 🔧 Technologies & Libraries

- **Python 3.10**
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **scikit-learn** - Machine learning algorithms
- **matplotlib** - Data visualization
- **seaborn** - Statistical visualization
- **plotly** - Interactive visualizations
- **ydata-profiling** - Automated EDA reports
- **ipykernel** - Jupyter kernel support
- **ipywidgets** - Interactive widgets

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Algerian_forest_fires
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📝 Project Structure

```
Algerian_forest_fires/
├── project.ipynb                              # Main Jupyter notebook with complete analysis
├── Algerian_forest_fires_dataset.csv          # Raw dataset
├── Algerian_forest_fires_cleaned_dataset.csv  # Cleaned dataset
├── requirements.txt                           # Python dependencies
└── README.md                                  # This file
```

## 🔍 Workflow

The project follows these main steps:

### 1. Data Loading
- Import dataset from CSV files
- Load both Bejaia and Sidi-Bel Abbes regions

### 2. Data Cleaning
- Remove region header rows
- Add region encoding (Bejaia=0, Sidi-Bel Abbes=1)
- Handle missing/null values
- Remove invalid rows
- Reset indices

### 3. Exploratory Data Analysis (EDA)
- Generate automated profiles using ydata-profiling
- Analyze data distributions and relationships
- Identify patterns and correlations
- Visualize features using matplotlib, seaborn, and plotly

### 4. Feature Engineering
- Standardize features using StandardScaler
- Prepare data for machine learning models

### 5. Model Development
- **Regression Model**: Predict FWI (Fire Weather Index)
- **Classification Model**: Predict fire occurrence (Classes)
- Train-test split: Typical 80-20 or 70-30 split
- Evaluate using R² score and Mean Squared Error (MSE)

## 📈 Key Metrics

- **R² Score** - Coefficient of determination for regression models
- **Mean Squared Error (MSE)** - Average squared difference between predicted and actual values
- **Classification Accuracy** - Proportion of correct predictions

## 💡 Usage

To run the analysis:

1. Open the Jupyter notebook:
   ```bash
   jupyter notebook project.ipynb
   ```

2. Execute cells sequentially to:
   - Load and explore the data
   - Clean and preprocess the dataset
   - Generate visualizations and statistics
   - Train machine learning models
   - Evaluate performance

## 📊 Model Pipeline

The project implements a pipeline approach:

```python
Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])
```

This ensures:
- Reproducible preprocessing
- Proper train-test handling
- Easy model deployment

## 🎯 Objectives

- [x] Load and explore the forest fires dataset
- [x] Clean and prepare data for analysis
- [x] Perform comprehensive EDA
- [x] Build predictive regression model for FWI
- [x] Build classification model for fire detection
- [x] Evaluate model performance
- [ ] Deploy model (optional)

## 📚 Dataset Source

The Algerian Forest Fires Dataset contains observations from:
- **Time Period**: June to September 2012
- **Regions**: Bejaia and Sidi-Bel Abbes in Algeria
- **Records**: 244 observations per region

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request


## 👤 Author

Created as a data science analysis project

## 🙏 Acknowledgments

- Algerian Forest Fires Dataset - source of the data
- scikit-learn documentation and community
- Python data science community

## ❓ FAQ

**Q: Which model performs better for fire prediction?**
A: See the model evaluation section in the notebook for detailed performance comparison.

**Q: Can I use this model for real-time fire prediction?**
A: The current model can be integrated with real-time data pipelines. Evaluate its accuracy and false positive rate before deployment.

**Q: How do I update the model with new data?**
A: Retrain the model using the pipeline with updated dataset and validate performance.

## 📧 Support

For questions or issues, please open an issue in the repository.

---

**Last Updated**: January 2026
