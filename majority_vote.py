#########

#Name; Felipe Marujo Grabowsky
#UNI: fm2579


# This program contains a function that count the most frequent label in the
#k nearest neighbors of a test point

#######

from create_data import *
import numpy as np
from integerize_labels import *
from split import *
from find_k_nearest_neighbors import*
from statistics import mode


def majority_vote(neighbors):
    ''' function that returns the majority vore of the k nearest neighbors '''


    #First, I will create variables corresponding to the number of columns and
    #rows in neighbors, and to the
    #dictionary that will be used to remember the number of votes
    l = len(neighbors)
    d = len(neighbors[0])
    label_dict ={}
    list_of_numbers =[]


    #For each row in neighbors, I will append the label to the list with all
    #the labels
    for i in range(l):
        number =int(neighbors[i,(d-1)])
        list_of_numbers.append(number)

    #I will then sort the list, so that the labels are sorted
    list_of_numbers.sort()



    #For each number in the list, I will change the dictionary, by updating
    #the item as the count of the number on the
    #list of numbers
    for i in list_of_numbers:
        label_dict.update({i:list_of_numbers.count(i)})


    #Then, I will create 2 variables, one with all the keys, and one with all
        #the items
    v = list(label_dict.values())
    k = list(label_dict.keys())
    #And this function will count the key with maximum value. If there are two
    #modes, this function returns the smaller
    #mode.
    majority_label = k[v.index(max(v))]









    return majority_label





