import pandas as ppd ### Imports the pandas library as variable name ppd
import csv ### Imports the csv library
import matplotlib.pyplot as plt ### Imports the matplotlib library as variable name plt

### Starts the main menu
### Keeps the menu looping until valid input is entered
### Asks for the user to select an option from the menu system
### Checks that the user input is a valid number in the menu, and takes the user to the next menu
### If the user input is not a valid number in the menu, it loops back
def main_menu():

    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. Total by region")
        print("### 3. Total resolved type ")
        print("### 4. Total num of parcels ")
        print("### 5. Total num of days it took to reslove ")
        print("### 6. Graphs ")
        
        choice = int(input('Enter your number selection here: '))
        
        while choice > 6:
            
            if choice > 6:
                print(" Invalid Choice, please select an option from 1 - 6")
                choice = int(input('Enter your number selection here: '))
            else:
                break
            
        try:
            int(choice)
                
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
            main_menu()

        else:    
            print('Choice accepted!')
            flag = False
        
            
    choice = str(choice)
    return choice

### Menu for total issue by type
### Keeps the menu looping until valid input is entered
### Checks that the user input is a valid number in the menu, and takes the user to the next menu
### If the user input is not a valid number in the menu, it loops back
def total_menu():

    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            choice = int(choice)    
            if choice > 0 and choice < 5:
                print('Choice accepted!')
                flag = False
            else:
                print("Sorry, you did not enter a valid option")
                flag = True
                

    ### List contaning all issue type
    issue_type_list = ["Customer Account Issue", 
                       "Delivery Issue", 
                       "Collection Issue", 
                       "Service Complaint"]
    
    ### Usues user choice to select correct issue from the list
    issue_type = issue_type_list[choice-1]

    ### Returns selected issue type
    return issue_type     

### A menu for the total num of issuses, based on what the issue type selected
### Reads the csv file and stores them into the variable dataframe
### Counts how many times the selected issue type apprears 
### Tells the user the total number of times their selected issue appears
def get_total_data(total_menu_choice):

    dataframe = ppd.read_csv("Task4a_data.csv")

    total = dataframe['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg

### Graph menu for issue type
### Reads the csv file and stores them into the variable dataframe
### Counts how many times all the issue type apprears
### Makes the bar chart
### Shows the user the graph
def data_menu():
    dataframe = ppd.read_csv("task4a_data.csv")
    total_issues = dataframe["Issue Type"].value_counts()
    ### X-axis label
    issue_type = ["Customer Account", 
                  "Delivery", 
                  "Collection", 
                  "Service"]

    plt.bar(issue_type, total_issues, color = "red", )
    plt.title("Total issue by type")
    plt.xlabel("Issue Type")
    plt.ylabel("Total issues")
    plt.show()

### Menu for total region by type
### Keeps the menu looping until valid input is entered
### Checks that the user input is a valid number in the menu, and takes the user to the next menu
### If the user input is not a valid number in the menu, it loops back
def region_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total by region ################")
        print("####################################################")
        print("")
        print("########## Please select a region ##########")
        print("### 1.South West ")   
        print("### 2. West Midlands") 
        print("### 3. London")  
        print("### 4. North Wales")
        print("### 5.South East ")   
        print("### 6. East of England") 
        print("### 7. North East ")  
        print("### 8. East Midlands")
        print("### 9. Scotland")   
        print("### 10. Yorkshire and The Humber") 
        print("### 11. South Wales")  
        print("### 12. North West")
        print("### 13. Northern Ireland")

        choice = int(input('Enter your number selection here: '))
        
        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            choice = int(choice)    
            if choice > 0 and choice < 14:
                print('Choice accepted!')
                flag = False
            else:
                print("Sorry, you did not enter a valid option")
                flag = True
        

    ### List contaning all region type
    region_list = ["South West", 
                  "West Midlands", 
                  "London", 
                  "North Wales", 
                  "South East", 
                  "East of England", 
                  "North East", 
                  "East Midlands", 
                  "Scotland", 
                  "Yorkshire and The Humber", 
                  "South Wales", 
                  "North West", 
                  "Northern Ireland"]
    
    ### Usues user choice to select correct region from the list
    region_type = region_list[choice-1]
    
    ### Returns selected region type
    return region_type   

### A menu for the total num of issuses, based on what the region type selected
### Reads the csv file and stores them into the variable dataframe
### Counts how many times the selected region type apprears 
### Tells the user the total number of times their selected region appears
def get_region_data(region_menu_choice):
    
    dataframe = ppd.read_csv("Task4a_data.csv")
    
    region = dataframe['Region'].value_counts()[region_menu_choice]
    
    msg = "The total number of issues logged in {} was: {}".format(region_menu_choice, region)

    return msg

### Graph menu for region type
### Reads the csv file and stores them into the variable dataframe
### Counts how many times all the region type apprears
### makes the bar chart
### shows the user the graph
def region_data_menu():
    dataframe = ppd.read_csv("task4a_data.csv")
    total_region = dataframe["Region"].value_counts()
    ### X-axis label
    region_type = ["South West", 
                   "West Midlands", 
                   "London", 
                   "North Wales", 
                   "South East", 
                   "East of England", 
                   "North East", 
                   "East Midlands", 
                   "Scotland", 
                   "Yorkshire and The Humber", 
                   "South Wales", "North West", 
                   "Northern Ireland"]
    
    plt.bar(region_type, total_region ,color = "green")
    plt.title("Total region by type")
    plt.xlabel("Region Type")
    plt.ylabel("Total issues")
    plt.show()
    
### Menu for total resloved by type
### Keeps the menu looping until valid input is entered
### Checks that the user input is a valid number in the menu, and takes the user to the next menu
### If the user input is not a valid number in the menu, it loops back
def resolved_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total resolved type ################")
        print("####################################################")
        print("")
        print("########## Please select a resolved type ##########")
        print("### 1. Full Refund Issued")   
        print("### 2. Partial Refund Issued") 
        print("### 3. Automated Password/Username Reset")  
        print("### 4. Manual Password/Username Reset")
        print("### 5. Account Updated")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            choice = int(choice)    
            if choice > 0 and choice < 5:
                print('Choice accepted!')
                flag = False
            else:
                print("Sorry, you did not enter a valid option")
                flag = True

    ### List contaning all resolved type
    resolved_type_list = ["Full Refund Issued", 
                        "Partial Refund Issued", 
                        "Automated Password/Username Reset", 
                        "Manual Password/Username Reset", 
                        "Account Updated"]
    
    ### Usues user choice to select correct resolved type from the list
    resolved_type = resolved_type_list[choice-1]
    
    ### Returns selected resolved type
    return resolved_type     

### A menu for the total num of issuses, based on what the resolved type selected
### Reads the csv file and stores them into the variable dataframe
### Counts how many times the selected resolved type apprears 
### Tells the user the total number of times their selected resolved type appears
def get_resolved_data(resolved_menu_choice):

    dataframe = ppd.read_csv("Task4a_data.csv")

    resolved = dataframe['How Resolved'].value_counts()[resolved_menu_choice]

    msg = "The total number of issues logged in {} was: {}".format(resolved_menu_choice, resolved)

    return msg

### Graph menu for resolved type
### Reads the csv file and stores them into the variable dataframe
### Counts how many times all the region type apprears
### Makes the bar chart
### Shows the user the graph
def resolved_data_menu():
    dataframe = ppd.read_csv("task4a_data.csv")
    total_resolved = dataframe["How Resolved"].value_counts()
    ### X-axis label
    resolved_type = ["Full Refund Issued", 
                     "Partial Refund Issued", 
                     "Automated Password/Username Reset", 
                     "Manual Password/Username Reset", 
                     "Account Updated"]
    
    plt.bar(resolved_type, total_resolved, color = "red")
    plt.title("Total resolved by type")
    plt.xlabel("Resolved Type")
    plt.ylabel("Total issues")
    plt.show()

### Menu for total num of parcels by type
### Keeps the menu looping until valid input is entered
### Checks that the user input is a valid number in the menu, and takes the user to the next menu
### If the user input is not a valid number in the menu, it loops back
def total_num_of_parcels_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total num of parcels ################")
        print("####################################################")
        print("")
        print("########## Please select a parcel type ##########")
        print("### 1. One")   
        print("### 2. Two") 
        print("### 3. Three")  
        print("### 4. Four")
        print("### 5. Five")
        print("### 6. Six")
        print("### 7. Seven")
        print("### 8. Eight")
        print("### 9. Nine")
        print("### 10. Ten")
        

        choice = input('Enter your number selection here:')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            choice = int(choice)    
            if choice > 0 and choice < 10:
                print('Choice accepted!')
                flag = False
            else:
                print("Sorry, you did not enter a valid option")
                flag = True
    ### List contaning all parcel type
    num_of_parcel_list = [1,
                       2,
                       3,
                       4,
                       5,
                       6,
                       7,
                       8,
                       9,
                       10,]
    
    ### Usues user choice to select correct parcel type from the list
    parcel_type = num_of_parcel_list[choice-1]
    ### Returns selected parcel type
    return parcel_type

### A menu for the total num of issuses, based on what the num of parcel type selected
### Reads the csv file and stores them into the variable dataframe
### Counts how many times the selected parcel type apprears 
### Tells the user the total number of times their selected parcel type appears
def get_parcel_data(total_num_of_parcel_menu_choice):
    
    dataframe = ppd.read_csv("Task4a_data.csv")
    
    parcel = dataframe['No Of Parcels'].value_counts()[total_num_of_parcel_menu_choice]

    msg = "The total number of parcels logged in {} was: {}".format(total_num_of_parcel_menu_choice, parcel)

    return msg

### Graph menu for parcel type
### Reads the csv file and stores them into the variable dataframe
### Counts how many times all the region type apprears
### Makes the bar chart
### Shows the user the graph
def parcel_data_menu():
    dataframe = ppd.read_csv("task4a_data.csv")
    total_parcel = dataframe["No Of Parcels"].value_counts().sort_index()
    ### X-axis label
    parcel_type = ["1","2","3","4","5",
                    "6","7","8","9","10",]
    
    plt.bar(parcel_type, total_parcel,color = "green")
    plt.title("Total parcel by type")
    plt.xlabel("Parcel Type")
    plt.ylabel("Total issues")
    plt.show()

### Menu for total num of days by type
### Keeps the menu looping until valid input is entered
### Checks that the user input is a valid number in the menu, and takes the user to the next menu
### If the user input is not a valid number in the menu, it loops back
def total_num_of_resolved_days_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total resolved days type ################")
        print("####################################################")
        print("")
        print("########## Please select a day type ##########")
        print("### 1. One")   
        print("### 2. Two") 
        print("### 3. Three")  
        print("### 4. Four")
        

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            choice = int(choice)    
            if choice > 0 and choice < 4:
                print('Choice accepted!')
                flag = False
            else:
                print("Sorry, you did not enter a valid option")
                flag = True
            
    ### List contaning all day type
    days_type_list = [1,2,3,4,]
    ### Usues user choice to select correct day type from the list
    days_type = days_type_list[choice-1]
    ### Returns selected day type
    return days_type     

### A menu for the total num of issuses, based on what the num of day type selected
### Reads the csv file and stores them into the variable dataframe
### Counts how many times the selected day type apprears 
### Tells the user the total number of times their selected day type appears
def get_days_data(total_num_of_resolved_days_menu_choice):
    
    dataframe = ppd.read_csv("Task4a_data.csv")
    
    days = dataframe['Days To Resolve'].value_counts()[total_num_of_resolved_days_menu_choice]

    msg = "The total number of issues logged in {} was: {}".format(total_num_of_resolved_days_menu_choice, days)

    return msg

### Graph menu for day type
### Reads the csv file and stores them into the variable dataframe
### Counts how many times all the day type apprears
###  Makes the bar chart
### Shows the user the graph
def days_data_menu():
    dataframe = ppd.read_csv("task4a_data.csv")
    total_days = dataframe["Days To Resolve"].value_counts().sort_index()
    ### X-axis label
    days_type = ["1","2","3","4",]
    
    plt.bar(days_type, total_days, color = "red")
    plt.title("Total days by type")
    plt.xlabel("Days Type")
    plt.ylabel("Total issues")
    plt.show()
    
### Menu for graphs   
### Keeps the menu looping until valid input is entered
### checks that the user input is a valid number in the menu, and takes the user to the selected graph    
def graphs_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Different graph type ################")
        print("####################################################")
        print("")
        print("########## Please select a graph type ##########")
        print("### 1. Issue by type graph")   
        print("### 2. Issue by region graph") 
        print("### 3. Issues by resolved graph")
        print("### 4. issues by parcels graph")  
        print("### 5. Issues by days graph")
        
        choice = input('Enter your number selection here: ')
        if choice == "1":
            data_menu()
        elif choice == "2":
            region_data_menu()
        elif choice == "3":
            resolved_data_menu()
        elif choice == "4":
            parcel_data_menu()
        elif choice == "5":
            days_data_menu()
        else:
            break
            

### Runs option from main menu
### Gets issue type choice
main_menu_choice = main_menu()

if main_menu_choice ==  "1":
    total_menu_choice = total_menu()
    
    ### Prints total issues
    print(get_total_data(total_menu_choice))
    ans = input("Do you want a graph of the data, yes/no:")
    if ans == "yes":
        ### Shows graph
        data_menu()
    elif ans == "no":
        print("see you next time")
    else:
         print("Sorry, you did not enter a valid option")
         
         
### Gets region type choice
if main_menu_choice ==  "2":
    region_menu_choice = region_menu()
    ### Prints total issues
    print(get_region_data(region_menu_choice))

    ans = input("Do you want a graph of the data, yes/no:")
    if ans == "yes":
        ### Shows graph
        region_data_menu()
    elif ans == "no":
        print("see you next time")
    else:
        print("Sorry, you did not enter a valid option")
        
### Gets resolved type choice
if main_menu_choice ==  "3":
    resolved_menu_choice = resolved_menu()
    ### Prints total issues
    print(get_resolved_data(resolved_menu_choice))
    
    ans = input("do you want a graph of the data, yes/no:")
    if ans == "yes":
        ### Shows graph
        resolved_data_menu()
    elif ans == "no":
        print("see you next time")
    else:
        print("Sorry, you did not enter a valid option")
        
### Gets parcel type choice
if main_menu_choice ==  "4":
    total_num_of_parcel_menu_choice = total_num_of_parcels_menu()
    ### Prints total issues
    print(get_parcel_data(total_num_of_parcel_menu_choice))

    ans = input("do you want a graph of the data, yes/no:")
    if ans == "yes":
        ### Shows graph
        parcel_data_menu()
    elif ans == "no":
        print("see you next time")
    else:
        print("Sorry, you did not enter a valid option")
        
### Gets resolved type choice
if main_menu_choice ==  "5":
    total_num_of_resolved_days_menu_choice = total_num_of_resolved_days_menu()
    ### Prints total issues
    print(get_days_data(total_num_of_resolved_days_menu_choice))
    
    ans = input("do you want a graph of the data, yes/no:")
    if ans == "yes":
        ### Shows graph
        days_data_menu()
    elif ans == "no":
        print("see you next time")
    else:
        print("Sorry, you did not enter a valid option")
        
if main_menu_choice ==  "6":
    ### Calls the graph menu
    graphs_menu()