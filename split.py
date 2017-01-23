#########

#Name; Felipe Marujo Grabowsky
#UNI: fm2579


# This program contains a function that splits a numpy array into a
#test data array and train data array

#######

from create_data import *
import numpy as np
from integerize_labels import *


def split(integerized_data):
    '''function that returns the whole data into the test data and train data '''

    #To start, I will assign the variables that will be used to split the data.
    d = len(integerized_data)
    label_dict_2 ={}
    test_data_list =[]
    train_data_list =[]
    number = 0

    #This loop will be used to create a dictionary for the different number of
    #labels there are
    for i in range(d):
        new_row = integerized_data[i,-1]

        #For each new label encountered, I will add it as a key to the
        #dictionary.
        if new_row not in label_dict_2.keys():
            label_dict_2.update({new_row: number})
            number += 1

    #Then, i will count the number of keys in the dictionary
    k = len(label_dict_2)


    #This will sort the data according to the labels
    np.sort(integerized_data)

    #And then I will split it in the number of different labels, to have a
    #list with arrays corresponding to plants
    #of different labels
    separated_list = np.split(integerized_data,k,)


    #Then, I will shuffle each separated array, mixing all the data
    for i in range(k):
        np.random.shuffle(separated_list[i])


    number = 0

    #Then, after shuffling each array, this loop will run from 0 to the
    #number of data divided by the number of different
    #plants. In this case (150/50), 50 times.
    while number <(d/k):

        #Then this loop will run so that I can get a data input from each of
        #the separated lists each loop
        for i in range(k):

            #For the first 15 cases, I will add the data to the test data.
            #This will run 3 times so there will be 45
            #data inputs in the test data
            if number <15:
                test_data_list.append(separated_list[i][number])

            #And for the rest of the loops, the data will be added to the train data
            else:
                train_data_list.append(separated_list[i][number])
        number+=1


    #After creating the lists for the test data and train data, I will
        #convert them into numpy arrays
    test_data = np.array(test_data_list, dtype=object)
    train_data = np.array(train_data_list, dtype=object)


        #use shuffle to shuffle each list, then add to one list for i<= 15
    #and to another list until 50



    return (train_data, test_data)



