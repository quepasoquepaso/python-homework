# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#James Eifler
#9/24/20 10:59pm MDT (started)
#9/29/20 1:31am MDT (ended)
###########################################

#Actual instructions:
#Your task is to create a Python script that analyzes the records to calculate each of the following
#The total number of months included in the dataset.
#The net total amount of Profit/Losses over the entire period.
#The average of the changes in Profit/Losses over the entire period.
#The greatest increase in profits (date and amount) over the entire period.
#The greatest decrease in losses (date and amount) over the entire period.
#Your final script should print the analysis to the terminal and export a text file with the results.
###########################################

#Psuedo:
#. Get file
#. Read data
#. Manipulate data
#. Organize & address issues
#. Perform calculations, listed in instructions
#. Print analysis to terminal and export as text file with results (new file)
#####################################################################################################



# Import the pathlib and csv and numpy_financial libraries
from pathlib import Path
import csv
import numpy_financial as npf

# Set the file path
filepath = Path("Resources/budget_data.csv")

# Initialize list of records
records = []

# Initialize list of totpnl ##did not use, don't think I need this
#list_totpnl = []

# Initialize total profit and losses
tot_pnl = 0

# Open the csv file as an object
with open(filepath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    for row in csvreader:
        records.append(row)



#INSTRUCTIONS - The total number of months included in the dataset.

print(f'Total Months:{len(records)}')



#INSTRUCTIONS - The net total amount of Profit/Losses over the entire period.

records_dict = {x[0]: x[1:] for x in records}
print(values)

#I could not figure out how to work with the dictionary values as ints
print(f'Total Profit/Losses: {(tot_pnl)}')



####I CAN'T FIGURE OUT HOW TO TURN THE STRINGS INTO INTS. I'VE TRIED:
    #TYPE CASTING THE DICT
    #TYPE CASTING WHEN IMPORTING THE CSV
    #BREAKING OUT THE VALUE OF THE KEY AND CASTING IT TO AN INT

    #I'VE LOOKED ALL OVER THE DOCS AND OTHER SOURCES -- I JUST CAN'T FIGURE IT OUT. IF I CAN'T TURN THOSE INTO INTS THAT I CAN MANIPULATE; THEN I CAN'T FINISH THE REST OF THE EXERCISE.

    #TO ARRIVE AT THE ANSWER FOR THIS SECTION, I WOULD:
    #SUM THE VALUES IN THE DICTIONARY



#INSTRUCTIONS - The average of the changes in Profit/Losses over the entire period.

    #TO ARRIVE AT THE ANSWER FOR THIS SECTION, I WOULD:
    #SUM THE VALUES IN THE DICTIONARY; THEN PRINT THE SUM AMOUNT



#INSTRUCTIONS - The greatest increase in profits (date and amount) over the entire period.

    #TO ARRIVE AT THE ANSWER FOR THIS SECTION, I WOULD:
    #LOOK FOR THE MAX VALUE; THEN PRINT THE DATE AND AMOUNT



#INSTRUCTIONS - The greatest decrease in losses (date and amount) over the entire period.

    #TO ARRIVE AT THE ANSWER FOR THIS SECTION, I WOULD:
    # #LOOK FOR THE MIN VALUE; THEN PRINT THE DATE AND AMOUNT



#INSTRUCTIONS - Your final script should print the analysis to the terminal and export a text file with the results.

    #TO ARRIVE AT THE ANSWER FOR THIS SECTION, I WOULD:

    f = open("results_analysis.txt", "a")
    f.write('Financial Analysis')
    f.write('--------------------------------------')
    f.write('Total Months:{len(records)}')
    f.write('Total: {tot_pnl}')
    f.write('Average Change: _______')
    f.write('Greatest Increase in Profits: _____________')
    f.write('Greatest Decrease in Profits: _____________')
    f.close()


# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



