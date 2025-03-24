def save_analysis(dataset):
    #save the dataset and analysis result to a file

    file_path= input("Enter the path to save the analysis (e.g. analysis.csv):")
    dataset.to_csv(file_path,index=False)
    print(f" analysis saved to {file_path}.")

