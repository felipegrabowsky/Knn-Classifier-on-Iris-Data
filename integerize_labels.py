#########

#Name; Felipe Marujo Grabowsky
#UNI: fm2579


# This program contains a function that returns a numpy matrix in which the
#labels are replaced by integer values

#######
from create_data import *
import numpy as np

new_matrix = []


def integerize_labels(data):
    '''function that returns a numpy matrix with integer values on the place of the labels '''

    #First , I will create and empty dictionary to which keys and items will be added.
    #I will also make a copy of the data so that I can work with it
    label_dict = {}
    d = len(data)
    integerized_data = np.copy(data)


    number = 0

    #This loop will run for all rows in the data numpy array
    for i in range(d):

        #I will assign the new row value to the label in each row
        new_row = data[i,-1]

        #Then this control will check if this label has already been spotted.
        #If not, it will add it to the dictionary
        #with the item value of its order in the dictionary
        if new_row not in label_dict.keys():
            label_dict.update({new_row:number})
            #number has to change every time a key is added so that the items
            #change for each key
            number +=1

        #In each loop, I will also change the label in the copy of the data
        #numpy array to the integer corresponding
        #to the label in the dictionary
        new_row = data[i, -1]
        integerized_data[i,-1] = label_dict[new_row]






    return (integerized_data, label_dict)



