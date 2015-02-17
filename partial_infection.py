#William Cai, Feb 14 
#full_infection.py
from user import User
from full_infection import full_infection

def compute_groups(users):
    """     in the graph given by users, groups the connected components, and returns 
    (num_groups, group_counts) where

    group_counts is the number of users in each group
    group_users is a list of users s.t. group_users[i] is in group i
    Keyword arguments:
    users - a list of Users from user.py.  
    """
    group_num = 0
    group_counts = []
    group_users = []
    while (1 == 1):
        #find a point that has not yet been touched
        for i in range(len(users)):
            if (users[i].group == 0):
                break

        #all points were touched
        if (i == len(users) - 1 and users[i].group > 0):
            break

        #we have another group
        group_num += 1
        #we want to keep track of how many users are in the group
        group_counts.append(0)
        #starting node of search
        u_0 = users[i]
        #keep track of starting nodes for later
        group_users.append(u_0)
        #do a depth-first search starting at u_0
        #list of users to visit on our traversal
        to_visit = []
        to_visit.append(u_0)
        #set of users which have already been added to our to_visit, avoid cycles
        already_found = set([u_0])
        while (to_visit):
            cur_user = to_visit.pop()
            #set the group number to our current group
            cur_user.group = group_num
            #increment the count of this group
            group_counts[group_num - 1] += 1
            #make a list of neighbors
            connected = cur_user.students + cur_user.coaches
            for a_user in connected:
                if a_user not in already_found:
                    to_visit.append(a_user)
                    already_found.add(a_user)
    return(group_counts, group_users)


def partial_infection(users, version_num, num_to_infect):
    """
    In the graph given by users, infect num_to_infect people with version version_num.  
    The method does this by 
    1) partitioning users into groups, keeping track of how many users are in each group
    2) Now that we have a set of numbers, we are looking for a subset s.t. the sum is close to num_to_infect
       This is actually a variation of the subset-sum problem (which is NP hard, so we won't solve it here, but
       exact_infect will make a stronger stab at it)

       We first sort the set and ignore all values that are greater than our target interval (i.e. 1.05 * num_to_infect)
       Call this <t1, t2>

       We will basically use a greedy algorithm - add the largest element that is less than t2 and then 
       the largest element less than (t2 - largest_element), etc.  If adding it actually takes us in the interval,
       we're done.  If we finish this not in the interval, it means we're under the interval and the smallest group
       left will take us over the interval.  Note that for the actual Khan Academy graphs there are 
       tons of users who aren't affiliated with any other users, meaning the size of their group is 1, so this probably
       wouldn't happen.  However, if it does happen, we will just split up the last group.

    Keyword arguments:
    users - a dicitonary of Users from user.py
    version_num - the version of the Khan Academy website we want to set the infected user to see
    num_to_infect - the target number of users to infect
    """
    #define return_status, which will change if we encounter various conditions
    return_status = 0


    #call the target interval t1, t2.  We are satisifed if we can get in this interval, which is flexible
    t1 = .95 * num_to_infect
    t2 = 1.05 * num_to_infect
    (group_counts, group_users) = compute_groups(users)
    #sorted group_counts
    ordered = [i for i in sorted(enumerate(group_counts), key=lambda x:x[1])]
    #ordered is a list of tuples of form (a,b) where b is a groupcount which was originally at index a
    #in the group_counts list
    for i in reversed(range(len(ordered))):
        if (ordered[i][1] <= t2):
            break

    largest_possible = i
    #at this point, largest_possible is the index of the largest group count not bigger than t2
    running_sum = 0
    #list of groups to add
    to_add = []
    #keep track of smallest group not added (in case of partial_add)
    not_added = -1
    for i in reversed(range(largest_possible + 1)):
        if (running_sum + ordered[i][1] < t2):
            running_sum += ordered[i][1]
            to_add.append(ordered[i][0])
            if (running_sum >= t1):
                break
        else:
            not_added = ordered[i][0]

    #Do we need to add part of a group to reach the interval?
    partial_add = 0
    #if we didn't reach the interval
    if (running_sum < t1): 
        # we do need to add part of a group
        partial_add = 1
    
    #do we want to infect the groups we've designated
    normal_infect = 1

    #partially infect?
    if (partial_add == 1):
        if (not_added != -1):
            """
            We know we're going to split the one of index not_added in ordered. 
            We deem it not worth the computing power to do an intelligent addition (like adding
            in the user in the group with the least degree) beacuse it's only one group and 
            they're getting a mixing of versions anyways we will just add them in order of depth
            first search
            """
            num_to_add = t1 - running_sum
            
            u_0 = group_users[not_added]
            #list of users to visit on our traversal
            u_0.dump_user_info()
            #the following is just depth first search which terminates when we've added enough
            to_visit = []
            to_visit.append(u_0)
            #set of users which have already been added to our to_visit                                                                 
            already_found = set([u_0])
            while (to_visit and (num_to_add > 0)):
                cur_user = to_visit.pop()
                #infect
                cur_user.version = version_num
                num_to_add -= 1
                connected = cur_user.students + cur_user.coaches
                for a_user in connected:
                    if a_user not in already_found:
                        to_visit.append(a_user)
                        already_found.add(a_user)
        else:
            #annoying case - we added everything less than or equal to the group indexed at largest_possible 
            #but it's not enough. two options - either use largest_possible + 1, or use everything else
            if (largest_possible == len(group_counts) - 1):
                #we actually just added everything, so it's the most we can do
                normal_infect = 1
                #reflect in return_status
                return_status = 2
            else:
                large_distance = ordered[largest_possible + 1][1] - num_to_infect
                small_distance = num_to_infect - running_sum
                if (large_distance < small_distance):
                    #infect group 
                    full_infection(group_users[ordered[largest_possible + 1][0]], version_num)
                    normal_infect = 0
                    #reflect in return_status
                    return_status = 3

    if (normal_infect == 1):
        #infect the chosen groups
        for i in range(len(group_counts)):
            if (i in to_add):
                full_infection(group_users[i], version_num)

    return return_status
