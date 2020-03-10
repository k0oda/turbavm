class Machine:
    __ram = []
    __disk = []
    __runned = False

    def __init__(self, ram_size : int, disk_size : int,):
        self.ram = [None for i in range(0, ram_size)]
        self.disk = [None for i in range(0, disk_size)]
        self.__commands = {
            '0001': self.__store,
            '0010': self.__add,
            '0011': self.__sub,
            '0100': self.__mult,
            '0101': self.__div,
            '0110': self.__output,
            '0111': self.__wait,
        }
    
    def run(self,):
        self.__runned = True
        print('Machine running')

    def stop(self,):
        self.__runned = False
        print('Machine has been stopped')
    
    def send_command(self, code, *args):
        if self.__runned:
            command = self.__commands.get(code, self.__commands['0111'])
            command(*args)
    
    def __wait(self,):
        pass
    
    def __store(self, into, data,):
        into = int(into)
        self.ram[into] = data
    
    def __add(self, first, second,):
        first = int(first)
        if second[0] == '/':
            second_operand = int(self.ram[second[1:]])
        else:
            second_operand = int(second)
        self.ram[first] = int(self.ram[first]) + second_operand

    def __sub(self, first, second,):
        first = int(first)
        if second[0] == '/':
            second_operand = int(self.ram[second[1:]])
        else:
            second_operand = int(second)
        self.ram[first] = int(self.ram[first]) - second_operand

    def __mult(self, first, second,):
        first = int(first)
        if second[0] == '/':
            second_operand = int(self.ram[second[1:]])
        else:
            second_operand = int(second)
        self.ram[first] = int(self.ram[first]) * second_operand

    def __div(self, first, second,):
        first = int(first)
        if second[0] == '/':
            second_operand = int(self.ram[second[1:]])
        else:
            second_operand = int(second)
        self.ram[first] = int(self.ram[first]) / second_operand
    
    def __output(self, address):
        print(self.ram[int(address)])
