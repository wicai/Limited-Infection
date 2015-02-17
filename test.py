#!/usr/bin/env python 

#William Cai, February 14
#test.py

import sys
import random

from user import User
from total_infection import total_infection as total_infection
from partial_infection import partial_infection as partial_infection
from exact_infection import exact_infection as exact_infection
import create_graphs as cg

def check_graph(user_graph):
    """Prints number of users infected, total number of users
    username and ids of infected users 

    Keyword arguments:
    user_graph - list of users
    """

    num_infected = 0
    for i in range(0, len(user_graph)):
        if (user_graph[i].version == 1):
            print("uid: " + str(user_graph[i].user_id) + ", username: " + \
                str(user_graph[i].username))
            num_infected += 1
    
    print "total number of users: " + str(len(user_graph))
    print "number of infected users: " + str(num_infected)

def full_infect_test():
    """Tests total_infection module on a variety of graphs.
    
    """
    print "total_infection + graph of 100 nodes where each edge has ~10% of appearing"
    num_users = 100
    rand = cg.random_graph(num_users, .05)
    total_infection(rand[0], 1)
    check_graph(rand)
    print
    print "total_infection + empty graph with 100 nodes"
    empty_graph = cg.empty_graph(100)
    total_infection(empty_graph[0], 1)
    check_graph(empty_graph)
    print
    print "total_infection + class graph with 20 teachers, avg of 15 students" \
        + "std dev of 5"
    teach = cg.class_graph(20, 15, 5)
    total_infection(teach[0],1 )
    check_graph(teach)
    print
    print "total_infection + full graph with 1000 nodes"
    full = cg.full_graph(1000)
    total_infection(full[random.randint(0,999)], 1)
    check_graph(full)

def partial_infect_test():
    """ tests partial_infection module on a variety of graphs.

    """
    print "partial_infection + graph of 100 nodes where each edge has ~10% of appearing" \
        + "asking to infect 10 users"
    num_users = 100
    rand = cg.random_graph(num_users, .05)
    partial_infection(rand, 1, 10)
    check_graph(rand)
    print
    print "partial_infection + empty graph with 100 nodes, asking it to infect 10 users"
    empty_graph = cg.empty_graph(num_users)
    partial_infection(empty_graph, 1, 10)
    check_graph(empty_graph)
    print
    print "partial_infection + class graph with 20 teachers, avg of 15 students" \
        + "std dev of 5, asking it to infect 22 users"
    teach = cg.class_graph(20, 15, 5)
    partial_infection(teach, 1, 22)
    check_graph(teach)
    print
    print "partial_infection + full graph with 1000 nodes, asking it to infect 100 users"
    full = cg.full_graph(1000)
    partial_infection(full, 1, 100)
    check_graph(full)

def exact_infect_test():
    """ tests exact_infection module on a variety of graphs.

    """
    print "exact_infection + graph of 100 nodes where each edge has ~10% of appearing" \
        + " asking to infect 10 users"
    num_users = 100
    rand = cg.random_graph(num_users, .05)
    attempt = exact_infection(rand, 1, 10)
    if (attempt == -1):
        print "program deemed it could not be done"
    else:
        check_graph(rand)
    print
    print "exact_infection + empty graph with 100 nodes, asking it to infect 10 users"
    empty_graph = cg.empty_graph(num_users)
    attempt = exact_infection(empty_graph, 1, 10)
    if (attempt == -1):
        print "program deemed it could not be done"
    else:
        check_graph(empty_graph)
    print
    print "exact_infection + class graph with 20 teachers, avg of 15 students" \
        + " std dev of 5, asking it to infect 22 users"
    teach = cg.class_graph(20, 15, 5)
    attempt = exact_infection(teach, 1, 22)
    if (attempt == -1):
        print "program deemed it could not be done"
    else:
        check_graph(teach)
    print
    print "exact_infection + full graph with 100 nodes, asking it to infect 10 users"
    full = cg.full_graph(100)
    attempt = exact_infection(full, 1, 10)
    if (attempt == -1):
        print "program deemed it could not be done"
    else:
        check_graph(full)

if __name__ == "__main__":
    full_infect_test()
    print
    partial_infect_test()
    print
    exact_infect_test()
