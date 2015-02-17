# Limited-Infection
Tool for facilitating A/B testing.  Written for a project-based interview for khan academy.

The actual assignment is split into the tree different infection files, 

exact_infection.py
total_infection.py
partial_infection.py

which does the three respective infections, and

user.py

which contains the user class and pertinent data.  

test.py 

contains the code for running tests, and 

create_graphs.py

allows us to create different graphs for the algorithm to work on.  

To run the tests, type

python test.py

and it will run tests on the three infections and explain what is going on.

Explanation of algorithms:

total_infection is done by a depth first search.  We keep track of users we have already infected
and do not try to traverse through them in order to protect against cycles.  Otherwise, it's pretty
straightforward.

partial_infection is done in the following manner:                                                                                                                        

1) partitioning users into groups, keeping track of how many users are in each group                                         
2) Now that we have a set of numbers, we are looking for a subset s.t. the sum is close to the amount of users to infect                    

We first sort the set and ignore all values that are greater than our target interval (i.e. (.95 -> 1.05) * num_to_infect)         
Call this <t1, t2>

We will basically use a greedy algorithm - add the largest element that is less than t2 and then                          
the largest element less than (t2 - largest_element), etc.  If adding all of these actually takes us in the interval,               
we're done.  If we finish this not in the interval, it means we're under the interval and the smallest group              
left will take us over the interval.  In this case, we will have to give the people in that group mixed A/B versions,
but we will only infect just enough people to get in our interval.  

Exact infection is done in the following manner:
1) partitioning users into groups, keeping track of how many users are in each group, just like in the previous infection
2) Solve the subset-sum problem for the set of numbers corresponding the number of users in each group using a dynamic programming
algorithm.

The idea is that we can use a dynamic programming algorithm, solving subproblems of the form                              
ex(i, j) = true if there is a subset of set[0, 1, ..., j-1] with sum = i and building up to solve                         
ex(num_to_infect, num_groups).  We can pretty easily keep track of the actual group numbers that do this,                 
if there is such a solution.   

This algorithm will run in pretty good time if the num_to_infect is not big compared to the number of groups.



