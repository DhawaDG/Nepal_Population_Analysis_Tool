import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(dataset):
    #generate visualization for the dataset
    if 'Population' not in dataset.columns:
        print("Error:'Population' column not found in the dataset.")
        return
    
    print("\n Data Visualizations ")

    population_data= dataset['Population']

    #histogram

    plt.figure(figsize=(10,6))
    sns.histplot(population_data,kde=True)
    plt.title("Population Distribution")
    plt.xlabel("Popualtion")
    plt.ylabel("Frequency")
    plt.show()


    
