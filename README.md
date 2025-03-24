![Alt Text](logo/Population_Demography.jpg)
# Nepal_Population_Analysis_Tool

## Overview  
Nepal Population Analysis Tool is a CLI-based data analysis tool designed to process and analyze population datasets. It provides statistical insights and visualizations for predefined datasets stored as CSV files.

## Features & Functionalities  
- **Load Population Data** – Read predefined datasets from CSV files.  
- **Calculate Statistics** – Compute key statistical measures like mean, median, mode, variance, standard deviation, IQR, and MAD.  
- **Generate Visualizations** – Display histograms and other visual insights to analyze population distribution.  
- **Save Analysis** – Store analysis results for further reference.  

## Technologies & Concepts Used  
- **Python Libraries**: `pandas`, `numpy`, `scipy.stats`, `matplotlib`, `seaborn`  
- **Data Handling**: Efficient processing of structured population datasets  
- **Statistical Analysis**: Mean, median, mode, variance, standard deviation, IQR, MAD  
- **Data Visualization**: Graphical representation of population data using histograms  

## Project Structure  
population_analysis/
│
├── main.py # Main CLI interface
├── data_operations.py # Functions for handling datasets
├── statistics.py # Functions for calculating statistics
├── visualization.py # Functions for generating visualizations
├── save_analysis.py # Functions for saving analysis results
└── data/ # Folder for datasets (CSV files)
├── province1.csv
├── province2.csv
├── province3.csv
├── province4.csv
├── province5.csv
├── province6.csv
└── province7.csv


## ⚙️ Technologies & Concepts Used  
- **Python Libraries**: `pandas`, `numpy`, `scipy.stats`, `matplotlib`, `seaborn`  
- **Data Handling**: CSV processing with `pandas`  
- **Statistical Analysis**: Mean, Median, Mode, Variance, Standard Deviation, IQR, MAD  
- **Data Visualization**: Histograms and KDE plots  

## 🚀 Installation & Usage  

### 1. Clone the Repository  
```bash
git clone https://github.com/DhawaDG/Nepal_Population_Analysis_Tool.git
cd population_analysis

### 2. Install Dependencies
```bash
pip install -r requirement.txt

### 3.  Run the Application
```bash
pyhton main.py

### 4. Follow On-Screen Instructions

 Select a province

 Choose analysis options (view dataset, calculate statistics, visualize data, save results)

 ## 📊 Example Outputs
  Statistics Output
  Basic Statistics:
    1. Mean: The average population is 123,456.78
    2. Median: The middle population value is 100,000.00
    3. Mode: The most common population is 98,000.00
    4. Variance: Population spread is 1,234,567,890.00
    5. Standard Deviation: Typical difference from average is 35,678.90
    6. IQR: Middle 50% range is 45,678.90
    7. MAD: Typical difference from median is 22,345.67

 ##🔥 Challenges  & Learnings 
✔️ Handling Missing Data – Implemented data integrity checks
✔️ Optimized Mode Calculation – Used pandas.mode() for better performance
✔️ Improved Visualization – Utilized seaborn for professional plots

 ##🔮 Future Improvements
 🔹 Allow custom dataset uploads
 🔹 Advanced Statistic(Skewness and kurtosis),Trend Analysis,Geographical Visualization,Customizable Filters,Export Visualizatiom
 🔹 Add hypothesis testing and regression models
 🔹 Develop interactive GUI/web dashboard

 ## 👤 Author
Dhawa Dorje Ghising (DhawaDG)

 ## 📜 License
This project is licensed under the MIT License. See the file LICENSE for details.