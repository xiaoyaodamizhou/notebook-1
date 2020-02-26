import abc

class VmReceiver(object):
    def start(self):
        print("virtual machine start")

    def stop(self):
        print("virtual machine stop")


class Command(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass


class StartCommand(Command):
    def __init__(self, reciver):
        self.reciver = reciver

    def execute(self):
        self.reciver.start()


class StopCommand(Command):
    def __init__(self, reciver):
        self.reciver = reciver

    def execute(self):
        self.reciver.stop()


class ClientInvoker(object):
    def __init__(self, command):
        self.command = command

    def do(self):
        self.command.execute()


if __name__ == '__main__':
    receiver = VmReceiver()
    start_command = StartCommand(receiver)
    stop_command = StopCommand(receiver)
    client = ClientInvoker(start_command)
    client.do()
    client.command = stop_command
    client.do()
