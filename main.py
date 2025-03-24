import sys 
from data_operations import load_province_data,view_dataset
from statistics_1 import calculate_statistics
from visualizations import visualize_data
from save_analysis import save_analysis


def show_menu():
    #displays the CLI menu options
    print("\n *** Nepal Population Analysis Tool*** ")
    print(" Namaste. Select a province to analyze:")
    print("Province 1(Koshi Pradesh) =1")
    print("Province 2(Madhesh Pradesh) =2")
    print("Province 3(Bagmati Pradesh) =3")
    print("Province 4(Gandaki Pradesh) =4")
    print("Province 5(Lumbini Pradesh)=5")
    print("Province 6(Karnali Pradesh) =6")
    print("Province 7(Sudurpaschim Pradesh) =7")
    print("Exit =8")

def show_analysis_menu():
    #displays the analysis menu options
    print("\n Analysis Options:")
    print("View Dataset = 1")
    print("Perform Basic Statitics= 2")
    print("Generate Data Visualization= 3")
    print("Save analysis to File= 4")
    print("Go Back to Province Selections= 5")


#global variable to hold the dataset

dataset = None

while True:
    show_menu()
    province_choice=input("Enter your Choice (1-8):")

    try:
        if province_choice =="8":
            print("Exiting Nepal Analysis Tool. Namaste!")
            sys.exit()
        elif province_choice in ["1","2","3","4","5","6","7"]:
            dataset = load_province_data(province_choice)
            while True:
                show_analysis_menu()
                try:
                    analysis_choice = input("Enter Your choice (1-5):")

                    if analysis_choice == "1":
                        view_dataset(dataset)
                    elif analysis_choice == "2":
                        calculate_statistics(dataset)

                    elif analysis_choice == "3":
                        visualize_data(dataset)
                
                    elif analysis_choice == "4":
                        save_analysis(dataset)

                    elif analysis_choice == "5":break

                    else:
                        print("Invalid option.Please enter a number between 1 and 5.")
                except Exception as e:
                    print(f"Inner Error: {e}. Please try again.")
        else:
            print("Invalid option.Please enter a number between 1 and 8.")

    except Exception as e:
        print(f"Error: {e}. Please try again")
                



            