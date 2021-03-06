#William Cai, February 14
#create_graphs.py, contains methods for creating graphs

import sys 
from user import User
from total_infection import total_infection as total_infection
import random
from partial_infection import partial_infection as partial_infection

def class_graph(num_classes, avg_class_size, std_dev):
    """ simulates what a graph made of mostly classes would look like:
    Each class consists of a teacher and students.  The number of students
    is given by a gaussian distribution given by the calling parameters.

    Returns the list of all users.    

    Keyword Arguments:
    num_classes - the number of classrooms in the graph
    avg_class_size - average class size, center of the gaussian distribution
    std_dev - std. dev of the gaussian distribution
    """
    users = []
    uid = 0
    for i in range(num_classes):
        #draw from the gaussian
        num_students = int(random.gauss(avg_class_size, std_dev))
        if (num_students < 0):
            num_students = 0
        cur_teacher = User(uid, "teacher" + str(i), [], [], 0)
        users.append(cur_teacher)
        uid += 1
        for ii in range(num_students):
            #create a new student
            cur_student = User(uid, "student" + str(ii), [], [cur_teacher], 0)
            uid += 1
            users[uid - ii - 2].students.append(cur_student)
            users.append(cur_student)
    return users

def full_graph(num_users):
    """ initializes num_users users. Everybody both teaches and is taught by everybody except themselves.

    Returns the list of all users.
    Keyword Arguments:
    num_users - the number of users the thing should have
    """
    users = []
    for i in range(num_users):
        users.append(User(i, 'user' + str(i), [], [], 0))

    for i in range(num_users):
        for ii in range(num_users):
            if (i != ii): 
                users[i].students.append(users[ii])
                users[ii].coaches.append(users[i])
    return users

def random_graph(num_users, prob):
    """ initializes num_users users, and randomly assigns student -> teacher relations between them by flipping a coin.
    Essentially, every edge in this graph has two rolls of prob chance, so an edge between user i and user j has a 
    (1 - prob)^2 chance of being there

    Returns the list of all users.

    Keyword Arguments:
    num_users - the number of users the thing should have
    prob - The chance that user i will teach user j for all i, j (it's a scalar)
    """
    #initialize the users
    users = []
    for i in range(num_users):
        users.append(User(i, 'user' + str(i), [], [], 0))
    #randomly assign teachers/students
    for i in range(num_users):
        for ii in range(num_users):
            if ((i != ii) and (random.random() < prob)):
                #if you win the coin flip, user i teaches user ii
                users[i].students.append(users[ii])
                users[ii].coaches.append(users[i])
    return users

def empty_graph(num_users):
    """ initializes num_users users, nobody teaches anybody. 

    Returns the list of all users.

    Keyword Arguments:
    num_users - the number of users the thing should have

    """
    #initialize the users
    users = []
    for i in range(num_users):
        users.append(User(i, 'user' + str(i), [], [], 0))
    return users
