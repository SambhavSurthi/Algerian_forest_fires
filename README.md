# Algerian Forest Fires Prediction System

A complete end-to-end machine learning project with Flask web application and AWS deployment for predicting Fire Weather Index (FWI) using environmental and meteorological data.

## 📋 Project Overview

This project predicts the **Fire Weather Index (FWI)** using environmental and meteorological data from two Algerian regions:
- **Bejaia Region**
- **Sidi-Bel Abbes Region**

The system includes:
- **Data Analysis**: Jupyter notebook with comprehensive EDA using ydata-profiling
- **Machine Learning**: Multiple regression models (Linear, Ridge, Lasso, ElasticNet)
- **Web Application**: Flask-based REST API with HTML interface
- **Cloud Deployment**: AWS Elastic Beanstalk with CodePipeline CI/CD
- **Interactive Dashboard**: Prediction interface and EDA report viewer

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

**Core Data Science:**
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

**Web Framework & Deployment:**
- **Flask** - Lightweight web application framework
- **AWS Elastic Beanstalk** - Managed platform for deploying web applications
- **AWS CodePipeline** - Continuous integration and continuous deployment (CI/CD)

## 🚀 Installation

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Algerian_forest_fires
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application locally**
   ```bash
   python application.py
   ```
   The application will be available at `http://localhost:5000`

## 📝 Project Structure

```
Algerian_forest_fires/
├── notebooks/
│   └── project.ipynb                          # Jupyter notebook with complete analysis & EDA
├── dataset/
│   ├── Algerian_forest_fires_dataset.csv      # Raw dataset
│   └── Algerian_forest_fires_cleaned_dataset.csv  # Cleaned dataset
├── models/
│   ├── linear_regression.pkl                  # Linear Regression model
│   ├── ridge_regression.pkl                   # Ridge Regression model
│   ├── lasso_regression.pkl                   # Lasso Regression model
│   └── elasticnet_regression.pkl              # ElasticNet Regression model
├── templates/
│   ├── index.html                             # Home page with project overview
│   ├── prediction.html                        # Prediction form and results
│   └── EDA_report.html                        # Interactive EDA report
├── application.py                             # Flask application entry point
├── requirements.txt                           # Python dependencies
├── .ebextensions/                             # AWS Elastic Beanstalk configuration (optional)
├── .gitignore                                 # Git ignore rules
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
- **Regression Model**: Predict FWI (Fire Weather Index) using Linear Regression,Ridge Regression,Lasso Regression, ElasticNet Regression
- Train-test split: Typical 80-20 or 70-30 split
- Evaluate using R² score and Mean Squared Error (MSE)

## 📈 Key Metrics

- **R² Score** - Coefficient of determination for regression models
- **Mean Squared Error (MSE)** - Average squared difference between predicted and actual values

## 💡 Usage

### Running the Jupyter Notebook Analysis

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

### Running the Flask Web Application

**Locally:**
```bash
python application.py
```

The application will start on `http://localhost:5000` with the following pages:
- **Home (`/`)** - Project overview and model performance metrics
- **Prediction (`/predict`)** - Interactive form to input features and get predictions
- **EDA Report (`/eda`)** - Interactive exploratory data analysis report

**View logs:**
```bash
# Terminal will show request logs and debug information
```

## 📊 Model Performance

The project uses 4 regression models that are evaluated and compared:

| Model | Purpose | Serialized File |
|-------|---------|-----------------|
| **Linear Regression** | Baseline linear model | `models/linear_regression.pkl` |
| **Ridge Regression** | L2 regularized regression | `models/ridge_regression.pkl` |
| **Lasso Regression** | L1 regularized regression | `models/lasso_regression.pkl` |
| **ElasticNet Regression** | Combined L1 & L2 regularization | `models/elasticnet_regression.pkl` |

**Performance Metrics:**
- **R² Score**: ~97.5% (Coefficient of Determination)
- **Mean Squared Error (MSE)**: ~1.10
- **Dataset**: 244 observations per region, 488 total records

All models are trained with:
- StandardScaler for feature normalization
- 80-20 train-test split
- Scikit-learn pipeline for reproducibility

## ☁️ AWS Deployment

### Prerequisites for Deployment

- AWS Account with appropriate IAM permissions
- AWS CLI installed and configured
- EB CLI installed: `pip install awsebcli`
- Git repository initialized

### AWS Elastic Beanstalk Setup

The application can be deployed to AWS Elastic Beanstalk for production:

**Environment Configuration:**
- **Platform**: Python 3.10
- **Environment Name**: `algerian-forest-fires-env` (customizable)
- **Application**: Algerian Forest Fires Prediction

**Key Features:**
- Automatic scaling based on traffic
- Health monitoring and auto-recovery
- CloudWatch integration for logging
- Environment variables support

### Deployment Steps

1. **Install AWS EB CLI:**
   ```bash
   pip install awsebcli
   ```

2. **Initialize Elastic Beanstalk:**
   ```bash
   eb init -p python-3.10 algerian-forest-fires
   # Follow prompts to select region and create SSH key pair
   ```

3. **Create Environment:**
   ```bash
   eb create algerian-forest-fires-env
   # This will create EC2 instance, load balancer, and security groups
   ```

4. **Deploy Application:**
   ```bash
   # After making changes to code
   eb deploy
   ```

5. **Monitor Deployment:**
   ```bash
   # Check environment status
   eb status
   
   # View application logs
   eb logs
   
   # Check environment health
   eb health
   ```

6. **Open Application in Browser:**
   ```bash
   eb open
   # Opens the deployed application URL in your default browser
   ```

### Environment Variables

Set these variables in Elastic Beanstalk Console or via EB CLI:

```bash
FLASK_ENV=production
FLASK_APP=application.py
DEBUG=False
```

### AWS CodePipeline CI/CD (Optional)

For automated deployment on code push:

1. Create CodePipeline in AWS Console
2. Configure source: AWS CodeCommit repository
3. Configure build stage (optional): CodeBuild with `buildspec.yml`
4. Configure deploy stage: Elastic Beanstalk deployment

**buildspec.yml example:**
```yaml
version: 0.2
phases:
  install:
    runtime-versions:
      python: 3.10
  build:
    commands:
      - pip install -r requirements.txt
      - python -m pytest (if tests exist)
artifacts:
  files:
    - '**/*'
```

### Monitoring & Logging

- **CloudWatch Logs**: View application logs in AWS Console
- **Elastic Beanstalk Dashboard**: Monitor environment health, CPU, memory
- **Application Logs**: Access via `eb logs` command
- **Email Notifications**: Enable for deployment events

## 🎯 Objectives

- [x] Load and explore the forest fires dataset
- [x] Clean and prepare data for analysis
- [x] Perform comprehensive EDA with ydata-profiling
- [x] Build and train 4 regression models (Linear, Ridge, Lasso, ElasticNet)
- [x] Evaluate models (R² Score: 97.5%, MSE: 1.10)
- [x] Serialize models to pickle format
- [x] Create Flask web application with HTML templates
- [x] Implement prediction endpoint with form-based input
- [x] Add EDA report viewer endpoint
- [x] Deploy to AWS Elastic Beanstalk (optional)
- [ ] Implement API authentication (optional)
- [ ] Add database integration (optional)
- [ ] Create REST API for programmatic access (optional)

## 📚 Dataset Source

The Algerian Forest Fires Dataset contains observations from:
- **Time Period**: June to September 2012
- **Regions**: 
  - Bejaia Region (244 records)
  - Sidi-Bel Abbes Region (244 records)
- **Total Records**: 488 observations
- **Features**: 12 input features + 3 target variables

**Feature Breakdown:**
- Temporal: day, month, year
- Weather: Temperature, Relative Humidity (RH), Wind Speed (Ws), Rain
- Fire Indices: FFMC, DMC, DC, ISI, BUI
- Target: FWI (Fire Weather Index)

## 🔐 API Endpoints

The Flask application provides the following endpoints:

- `GET /` - **Home Page**
  - Returns the project overview and model performance metrics
  - Displays R² Score (~97.5%) and MSE (~1.10) for all models
  
- `GET /predict` - **Prediction Form** (GET request)
  - Returns the prediction input form with all required fields
  
- `POST /predict` - **Make Fire Prediction**
  - Accepts form data with the following parameters:
    - `day`, `month`, `year`
    - `Temperature`, `RH`, `Ws`, `Rain`
    - `FFMC`, `DMC`, `DC`, `ISI`, `BUI`
  - Returns predictions from all 4 models:
    - Linear Regression Model
    - Ridge Regression Model
    - Lasso Regression Model
    - ElasticNet Regression Model
  
- `GET /eda` - **EDA Report**
  - Returns the interactive exploratory data analysis report in HTML format

## 📖 Quick Start Guide

### 1. Clone and Setup
```bash
git clone <repository-url>
cd Algerian_forest_fires
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Locally
```bash
python application.py
# Open browser to http://localhost:5000
```

### 3. Make Predictions
- Visit `http://localhost:5000/predict`
- Fill in the 12 required features
- Click "Predict FWI" to get results from all 4 models

### 4. View Analysis
- Visit `http://localhost:5000/eda` to see the exploratory data analysis report

### 5. Deploy to AWS (Optional)
```bash
pip install awsebcli
eb init -p python-3.10 algerian-forest-fires
eb create algerian-forest-fires-env
eb deploy
eb open
```

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Clone your fork locally
3. Create a feature branch (`git checkout -b feature/improvement`)
4. Make your changes and test locally
5. Ensure models are properly trained and serialized
6. Update dependencies in `requirements.txt` if needed
7. Test the Flask application with new changes
8. Commit your changes (`git commit -m 'Add improvement'`)
9. Push to the branch (`git push origin feature/improvement`)
10. Open a Pull Request

**Development Workflow:**
- Test Flask app locally with `python application.py`
- Run Jupyter notebook analysis for model validation
- Update trained models in `models/` folder
- Ensure all dependencies are in `requirements.txt`
- Test all HTML templates in browser before committing
- AWS deployment is optional - can be done separately


## 👤 Author

**Sambhav Surthi**
- Machine Learning Engineer
- Email: 2300031622cseelge@gmail.com
- LinkedIn: [linkedin.com/in/sambhavsurthi](https://linkedin.com/in/sambhavsurthi)
- GitHub: [@SambhavSurthi](https://github.com/SambhavSurthi)
- Portfolio: [sambhavsurthi.in](https://sambhavsurthi.in)

## 🙏 Acknowledgments

- Algerian Forest Fires Dataset - source of the data
- scikit-learn documentation and community
- Python data science community

## ❓ FAQ

**Q: How do I run the application locally?**
A: Execute `python application.py` in the project directory. The app will run on `http://localhost:5000`.

**Q: What models are used for prediction?**
A: Four regression models are used: Linear Regression, Ridge Regression, Lasso Regression, and ElasticNet Regression. All predictions are returned for comparison.

**Q: How do I make predictions?**
A: Navigate to `/predict` page and fill in the 12 required features (day, month, year, Temperature, RH, Ws, Rain, FFMC, DMC, DC, ISI, BUI). Submit the form to get FWI predictions from all models.

**Q: What's the accuracy of the models?**
A: All models achieve R² Score of ~97.5% and MSE of ~1.10 on the test dataset.

**Q: How do I view the EDA report?**
A: Visit the `/eda` endpoint to view an interactive exploratory data analysis report.

**Q: Can I deploy this to AWS?**
A: Yes! Use Elastic Beanstalk with the provided setup instructions. Requires AWS account and EB CLI.

**Q: How do I add new models?**
A: Train models in the Jupyter notebook, serialize with pickle, save to `models/` folder, and update `application.py` to load and use them.

**Q: What if the deployed application goes down?**
A: Check Elastic Beanstalk dashboard for health status, view logs with `eb logs`, and check CloudWatch for error details.

**Q: Can I use this for real-time wildfire prediction?**
A: Yes! The Flask API can be integrated with real-time data sources. Ensure proper validation and testing before production use.

## 📧 Support

For questions or issues, please open an issue in the repository.

---

**Last Updated**: January 2026
