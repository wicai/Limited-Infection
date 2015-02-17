#!/usr/bin/env python

#William Cai, Feb 14 
#full_infection.py
from user import User
from full_infection import full_infection
from partial_infection import compute_groups as compute_groups
from partial_infection import partial_infection as partial_infection

def exact_infection():

    #define return_status, which will change if we encounter various conditions
    return_status = 0

    #compute the groups of the graph
    #(group_counts, group_users) = compute_groups(users)
    group_counts = [1, 4, 7, 11, 9]
    num_to_infect = 33

    #sorted group_counts
    
    dyn_table = [ [0] * (len(group_counts) + 1) for ii in range(num_to_infect + 1)]
    track_subsets = [   [ [] for i in range(len(group_counts) + 1)] for ii in range(num_to_infect + 1)]

    #build edges of table
    for i in range(1, num_to_infect + 1):
        #obviously we cannot get a nonzero sum with no elements being added
        dyn_table[i][0] = 0
        track_subsets[i][0] = []
    #getting a sum of 0 is easy, just don't use any elements
    for i in range(0, len(group_counts) + 1):
        dyn_table[0][i] = 1
        track_subsets[i][0] = []

    for i in range(1, num_to_infect + 1):
        for ii in range(1, len(group_counts) + 1):
            if (i >= group_counts[ii-1]): #then it's possible that a sum adding to i uses group_counts[j-1]
                dyn_table[i][ii] = (dyn_table[i][ii-1] or dyn_table[i - group_counts[ii-1]][ii-1])
                if (dyn_table[i][ii] == 1 and dyn_table[i][ii-1] == 1):
                    track_subsets[i][ii] = track_subsets[i][ii-1][:]
                elif (dyn_table[i][ii] == 1):
                    track_subsets[i][ii] = track_subsets[i - group_counts[ii-1]][ii-1][:]+[ii-1]
            else:
                dyn_table[i][ii] = dyn_table[i][ii-1]
                track_subsets[i][ii] = track_subsets[i][ii-1]
    print dyn_table[i][ii]
    print track_subsets[i][ii]


    return return_status

if __name__ == "__main__":
    exact_infection()
