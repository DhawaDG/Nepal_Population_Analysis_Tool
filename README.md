
# Nepal Population Analysis Tool

![Population Demography](logo/Population_Demography.jpg)

## 📌 Overview  
The **Nepal Population Analysis Tool** is a CLI-based program designed to analyze population data from Nepalese provinces. It provides statistical insights and visualizations for predefined datasets stored as CSV files.

## ✨ Features & Functionalities  
- ✅ **Load Population Data** – Read predefined datasets from CSV files  
- 📊 **Calculate Statistics** – Compute mean, median, mode, variance, standard deviation, IQR, and MAD  
- 📈 **Generate Visualizations** – Display histograms and distribution plots  
- 💾 **Save Analysis** – Store results for further reference  
- 🔄 **User-Friendly CLI** – Interactive menu for easy navigation  

## 🏗️ Project Structure  
population_analysis/
│
├── main.py # Main CLI interface
├── data_operations.py # Dataset handling
├── statistics.py # Statistical calculations
├── visualization.py # Data visualization
├── save_analysis.py # Result saving
└── data/ # Dataset files
├── province1.csv
├── province2.csv
├── province3.csv
├── province4.csv
├── province5.csv
├── province6.csv
└── province7.csv


## ⚙️ Technologies Used  
- **Python**: `pandas`, `numpy`, `scipy.stats`, `matplotlib`, `seaborn`  
- **Data Formats**: CSV processing  
- **Statistics**: Mean, Median, Mode, Variance, Standard Deviation  
- **Visualization**: Histograms, KDE plots  

## 🚀 Installation & Usage  

### 1. Clone the Repository  
```bash
git clone https://github.com/DhawaDG/Nepal_Population_Analysis_Tool.git
cd Nepal_Population_Analysis_Tool

2. Install Dependencies

pip install -r requirements.txt

3. Run the Application

python main.py

4. Follow On-Screen Instructions
Select a province

Choose analysis options

📊 Sample Output

Basic Statistics:
1. Mean: 123,456.78
2. Median: 100,000.00
3. Mode: 98,000.00
4. Variance: 1,234,567,890.00
5. Standard Deviation: 35,678.90
6. IQR: 45,678.90
7. MAD: 22,345.67

🔥 Challenges & Solutions
✔️ Data Integrity – Implemented missing data checks
✔️ Performance – Optimized mode calculation using pandas.mode()
✔️ Visualization – Enhanced plots with seaborn

🔮 Future Roadmap
🔹 Custom dataset upload support
🔹 Advanced statistics (Skewness, Kurtosis)
🔹 Trend analysis & geographical visualization
🔹 Interactive GUI/Web dashboard

👤 Author
Dhawa Dorje Ghising (DhawaDG)

📜 License
MIT License - See LICENSE for details



Key improvements made:
1. Fixed image path syntax (now properly references `logo/Population_Demography.jpg`)
2. Corrected code block formatting (fixed triple backticks)
3. Fixed installation commands (corrected `requirement.txt` to `requirements.txt` and `pyhton` to `python`)
4. Organized sections more logically
5. Made the structure more scannable with emoji markers
6. Added proper spacing between sections
7. Standardized heading levels
8. Improved consistency in formatting

Make sure:
- Your image file exists at `logo/Population_Demography.jpg`
- You have a `requirements.txt` file in your repo
- The directory name matches (`Nepal_Population_Analysis_Tool`)
