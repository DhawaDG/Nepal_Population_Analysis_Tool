import numpy as np
from scipy.stats import iqr, median_abs_deviation,mode

def calculate_statistics(dataset):
    #calculate and display Basic statitics in simple term

    print("\n Basic Statistics")
    population_data= dataset['Population']

    #calculate statistics
    mean = np.mean(population_data)
    median= np.median(population_data)
    mode_value=mode(population_data,keepdims=True).mode[0] if not population_data.mode().empty else "No mode found"
    variance= np.var(population_data,ddof=1)
    std_dev=np.std(population_data,ddof=1)
    iqr_value= iqr(population_data)
    mad= median_abs_deviation(population_data.to_numpy(),scale='normal')


    

    print(f"1. **Mean**: The average population of all districts in the province is {mean:.2f}.")
    print(f"   - Think of it as the 'typical' population size if all districts were equally populated.")

    print(f"\n 2. **Median**: The middle population value is {median:.2f}.")
    print(f"   - If you lined up all districts by population, this is the population of the district in the middle.")

    print(f"\n 3. **Mode**: The most common population value is {mode_value:.2f}.")
    print(f"   - This is the population size that appears most frequently in the dataset.")

    print(f"\n 4. **Variance**: The spread of population sizes is {variance:.2f}.")
    print(f"   - It tells you how much the population sizes vary from the average.")

    print(f"\n 5. **Standard Deviation**: The typical difference between a district's population and the average is {std_dev:.2f}.")
    print(f"   - A smaller number means most districts have populations close to the average.")

    print(f"\n 6. **Interquartile Range (IQR)**: The range of the middle 50% of population sizes is {iqr_value:.2f}.")
    print(f"   - It shows how spread out the middle half of the districts are.")

    print(f"\n 7. **Median Absolute Deviation (MAD)**: The typical difference between a district's population and the middle population is {mad:.2f}.")
    print(f"   - It's a robust way to measure how spread out the populations are, ignoring extreme values.")