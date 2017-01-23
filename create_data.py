#########

#Name; Felipe Marujo Grabowsky
#UNI: fm2579


# This program contains a function that reads a csv file and returns a numpy matrix with the data

#######


import csv
import numpy as np

def create_data(input_data_file):
    ''' function that returns a numpy matrix with the data in a csv file'''



    #i will create a list to which I will add each row of the csv file before creating the numpy matrix
    new_matrix=[]

    #In order to work with the csv file, I will open it
    workbook_file = open(input_data_file,"r")
    workbook_reader = csv.reader(workbook_file)


    #for each row in the csv file, I will append the row to the list
    for row in workbook_reader:
        new_matrix.append(row)

    #this variable corresponds to the number of columns in the csv file,
    d = len(new_matrix[0])


    #This loop will convert all string values up to the labels columns in the list into float values
    for row in new_matrix:
        for i in range(d-1):
            row[i]= float(row[i])



    #I will then create the numpy array
    data = np.array(new_matrix,dtype=object)

    data = data



    workbook_file.close()

    return data






