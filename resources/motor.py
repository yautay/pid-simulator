class Motor:
    def __init__(self, kv):
        self.__kv = kv

    def rpm(self, command, voltage):
        if 1000 <= command <= 2000:
            command = (command/1000)-1
            return self.__kv * voltage * command
        else:
            print("command signal out of range 1000/2000")
            raise Exception
