import abc

class Worker(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def work(self):
        pass


class Employee(Worker):
    __metaclass__ = abc.ABCMeta

    def work(self):
        print("employ {} start to work".format(self.name))


class Leader(Worker):
    def __init__(self, name):
        self.members = []
        super(Worker, self).__init__(name)

    def add_member(self, employee):
        if employee not in self.members:
            self.members.append(employee)

    def remove_member(self, employee):
        if employee in self.members:
            self.members.remove(employee)

    def work(self):
        print("leader {} start to work".format(self.name))
        for employee in self.members:
            employee.work()


if __name__ == '__main__':
    employe_1 = Employe("employe_1")
    employe_2 = Employe("employe_2")
    leader_1 = Leader("leader_1")
    leader_1.add_member(employe_1)
    leader_1.add_member(employe_2)

    employe_3 = Employe("employe_3")
    leader_2 = Leader("leader_2")
    leader_2.add_member(employe_3)
    leader_2.add_member(leader_1)

    leader_2.work()