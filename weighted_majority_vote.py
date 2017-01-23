#########

# Name; Felipe Marujo Grabowsky
# UNI: fm2579


# This program contains a function that count the weighted most frequent
#label in the k nearest neighbors of a test point

#######
from create_data import *
import numpy as np
from integerize_labels import *
from split import *
from find_k_nearest_neighbors import*
from statistics import mode
import operator




def weighted_majority_vote(test_point, neighbors):
    '''Function that returns the weighted most frequent neighbor of a test point'''


    #Firstly, I have to create values corresponding to the number of
    #rows and columns in the neighbors data
    l = len(neighbors)
    d = len(neighbors[0])


    number = 0

    #These variables will correspond to the total euclidean distance of
    #each label and the frequency of each label
    #in the neighbors data
    distance_0=0
    distance_1=1
    distance_2=2
    distance_0_times = 0
    distance_1_times = 0
    distance_2_times = 0


    #For every row in the neighbors data, this loop will run and calculate
    #the euclidean distance between the row
    #and the test point
    for row in range(l):

        label = int(neighbors[row, (d - 1)])

        for i in range (d-1):
            number += (((test_point[i])-(neighbors[row,i]))**2)

    #Then, the euclidean distance is the square root of all the differences
            #squared added together
        distance = ((number)**(1/2))

    #But also, in each row, the loop will check what is the label of the
        #data and add each distance to the number
    #corresponding to each label.It will also count the frequence of each
        #label
        if label == 0:
            distance_0 +=distance
            distance_0_times += 1
        elif label ==1:
            distance_1 += distance
            distance_1_times += 1
        elif label ==2:
            distance_2+= distance
            distance_2_times += 1

    #Then, if the label has appeared at least once, I will calculate the
    #mean distance of each label, to then
    #compare when breaking ties
    if distance_1_times !=0:
        distance_1 = distance_1 / distance_1_times
    if distance_2_times != 0:
        distance_2 = distance_2/distance_2_times
    if distance_0_times != 0:
        distance_0 = distance_0/distance_0_times


    #Then, I will assign a maximum frequence to the most appearing label
    maximum_label = max(distance_0_times,distance_1_times,distance_2_times)



    #However, this control will check if the maximum frequency is the frequency
    #of more than one label. If so,
    # the function should check the minimum mean distance of the labels in
    #which the maximum frequency is the same
    if (maximum_label == distance_0_times and maximum_label == distance_1_times):
        weighted_majority_label = min(distance_0,distance_1)
    elif (maximum_label == distance_0_times and maximum_label == distance_2_times):
        weighted_majority_label = min(distance_0, distance_2)
    elif (maximum_label == distance_1_times and maximum_label == distance_2_times ):
        weighted_majority_label = min(distance_2, distance_1)
    elif (maximum_label == distance_0_times and maximum_label == distance_1_times and maximum_label == distance_2_times):
        weighted_majority_label = min(distance_0, distance_1
                                      , distance_2)



    #But if there is only one mode, the function will return the mode as
    #the one with the maximum frequency.
    elif maximum_label == distance_0_times:
        weighted_majority_label = 0
    elif maximum_label == distance_1_times:
        weighted_majority_label = 1
    elif maximum_label == distance_2_times:
        weighted_majority_label = 2





    return weighted_majority_label



