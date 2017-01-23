#########

#Name; Felipe Marujo Grabowsky
#UNI: fm2579


# This program contains a function that returns the weighted k
#nearest neighbors predicted labels for all test points
#in test data

#######

from create_data import *
import numpy as np
from integerize_labels import *
from split import *
from find_k_nearest_neighbors import*
from statistics import mode
import operator
from weighted_majority_vote import *





def weighted_knn(train_data, test_data, k):
    '''Function that returns a matrix of 45x1 with all the predicted nearest neighbours labels for all of test data'''

    #for each data in test data:
    #find k_nearest neighbours and majority vote
    #add the label to the list
    #calling a function inside function is not working



    #First, I will create a list to which I will add the predicted labels
    list_of_predicted_labels = []

    #This list should have the same number of rows as the test data
    for row in test_data:
        list_of_predicted_labels.append([])

    i=0

    #The variable i will control this loop, that will be used to find the
    #nearest neighbors of each case, and its
    #predicted label
    while i < (len(test_data)):

        #To get each predicted label, I will have to use the previous
        #functions to find the k nearest neighbours
        #of each case, and then find the majority vote for each case.
        neighbor = find_k_nearest_neighbors(test_data[i],train_data,k)
        label = weighted_majority_vote(test_data[i],neighbor)

        #Then, I will append the predicted label to the correct row in
        #the list
        list_of_predicted_labels[i].append(label)
        i+=1

    #The final predicted array will be a numpy array of the list of predicted
        #labels.
    weighted_predicted_labels = np.array(list_of_predicted_labels)


    return weighted_predicted_labels

