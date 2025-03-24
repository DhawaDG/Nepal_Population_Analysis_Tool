import pandas as pd

def load_province_data(province_choice):
    #load the dataset for the selected province   # dataset = load_province_data(province_choice)

    province_files={
        "1":"data/province1.csv",
        "2":"data/province2.csv",
        "3":"data/province3.csv",
        "4":"data/province4.csv",
        "5":"data/province5.csv",
        "6":"data/province6.csv",
        "7":"data/province7.csv",
        }
    file_path= province_files.get(province_choice)
    if file_path :
        dataset =pd.read_csv(file_path)
        print(f" Dataset for Province {province_choice} loaded successfully ")
        return dataset
    else:
        raise ValueError("Invalid Province Selection.")
    
def view_dataset(dataset):
    #display the first few rows of the dataset

    print("\n First Few Rows of the Dataset:")
    print(dataset.head())

