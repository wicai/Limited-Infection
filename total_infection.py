#William Cai, Feb 14 
#full_infection.py
from user import User

def total_infection(u_0, version_num):
    """ Sets the version field of every User in users connected to an initial user to be version_num
    (fully infects the connected component)

    Keyword arguments:
    users - a dictionary of Users from user.py.  
            Key is user_id, and the value is the User whose user_id is the key
    u_0 - the user the infection starts from
    version_num - the version of the Khan Academy website we want to set the infected user to see
    """
    #list of users to visit on our traversal
    to_visit = []
    to_visit.append(u_0)
    #set of users which have already been added to our to_visit
    already_found = set([u_0])
    while (to_visit):
        cur_user = to_visit.pop()
        #set the version to our new version
        cur_user.version = version_num
        connected = cur_user.students + cur_user.coaches
        for a_user in connected:
            if a_user not in already_found:
                to_visit.append(a_user)
                already_found.add(a_user)

                
    

