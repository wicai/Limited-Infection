#William Cai, Febraury 14
#user.py 
class User:
    def __init__(self, user_id, username, students, coaches, version):
        self.user_id = user_id
        self.username = username
        #list of users that this user teaches
        self.students = students
        #list of users that this user is taught by
        self.coaches = coaches
        #version of khan academy website this user is on
        self.version = version
        #group number assigned in partial_infection
        self.group = 0

    def dump_user_info(self):
        print self.user_id
        print self.username
        print "students:"
        for i in range(len(self.students)):
            print self.students[i].user_id
        print "coaches:"
        for i in range(len(self.coaches)):
            print self.coaches[i].user_id
        print
        print "version: " + str(self.version)
        print
        print "group number: " + str(self.group)
        print
