#William Cai, Feb 14 
#total_infection.py
from user import User
from total_infection import total_infection
from partial_infection import compute_groups as compute_groups
from partial_infection import partial_infection as partial_infection

def exact_infection(users, version_num, num_to_infect):
    """
    In the graph given by users, infect exactly num_to_infect people with version version_num, either
    infecting whole groups or not touching them at all.  

    The method does this by 
    1) partitioning users into groups, keeping track of how many users are in each group
    2) Now that we have a set of numbers, we are looking for a subset s.t. the sum is exactly num_to_infect
       This is called the subset-sum problem, which is NP hard, so we will have do some tricks to get it to
       run in reasonable time.  
       
       We will solve the problem in "pseudo-polynomial" time - this works pretty well if num_to_infect is
       small, but will otherwise take a long time (A/B testing starts with only a few people right?)
       
       The idea is that we can use a dynamic programming algorithm, solving subproblems of the form
       ex(i, j) = true if there is a subset of set[0, 1, ..., j-1] with sum = i and building up to solve
       ex(num_to_infect, num_groups).  We can pretty easily keep track of the actual group numbers that do this,
       if there is such a solution.  

    Keyword arguments:
    users - a dicitonary of Users from user.py
    version_num - the version of the Khan Academy website we want to set the infected user to see
    num_to_infect - the target number of users to infect
    """

    #define return_status, which will change if we encounter various conditions
    return_status = 0

    #compute the groups of the graph
    (group_counts, group_users) = compute_groups(users)
    dyn_table = [ [0] * (len(group_counts) + 1) for ii in range(num_to_infect + 1)]
    track_subsets = [   [ [] for i in range(len(group_counts) + 1)] for ii in range(num_to_infect + 1)]

    #build edges of table
    for i in range(1, num_to_infect + 1):
        dyn_table[i][0] = 0
        track_subsets[i][0] = []

    for i in range(0, len(group_counts) + 1):
        dyn_table[0][i] = 1
        track_subsets[0][i] = []

    for i in range(1, num_to_infect + 1):
        for ii in range(1, len(group_counts) + 1):
            if (i >= group_counts[ii-1]):  #then it's possible that a sum adding to i uses group_counts[j-1]
                dyn_table[i][ii] = (dyn_table[i][ii-1] or dyn_table[i - group_counts[ii-1]][ii-1])
                if (dyn_table[i][ii] == 1 and dyn_table[i][ii-1] == 1):
                    track_subsets[i][ii] = track_subsets[i][ii-1][:]
                elif (dyn_table[i][ii] == 1):
                    track_subsets[i][ii] = track_subsets[i - group_counts[ii-1]][ii-1][:]+[ii-1]
            else: #just take whatever we got for using the smaller subset
                dyn_table[i][ii] = dyn_table[i][ii-1]
                track_subsets[i][ii] = track_subsets[i][ii-1]

    if (dyn_table[num_to_infect][len(group_counts)] == 0):
        return -1 #not possible
    else:
        for i in range(len(track_subsets[num_to_infect][len(group_counts)] )):
            #infect the users that correspond to the elements of the subset
            total_infection(group_users[track_subsets[num_to_infect][len(group_counts)][i]], 1)
        return 1
    
