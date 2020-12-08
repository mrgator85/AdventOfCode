
class CPU(object):
    def __init__(self):
        self.program = []
        self.accumulator = 0
        self.instruction = 0


    def loadProgram(self, input):
        '''Program is stored as an array of tuples. Tuples contain instructcion, param, 
           and boolean for whether or not its been executed'''
        for l in input:
            instr, param = l.split(' ')
            self.program.append([instr.strip(), int(param), False ])
    
    def run(self):
        status = 0
        while(self.instruction < len(self.program)):
            if(self.program[self.instruction][2]):
                print(f"Forever loop - Accumulator: {self.accumulator}")
                status = 1
                break
            if(self.instruction == len(self.program)):
                print(f"Terminate Successfully")
                status = 0
                break
            if(self.program[self.instruction][0]== 'acc'):
                self.accumulator = self.accumulator + self.program[self.instruction][1]
                self.program[self.instruction][2] = True
                self.instruction = self.instruction + 1
            elif(self.program[self.instruction][0] == 'jmp'):
                self.program[self.instruction][2] = True
                self.instruction = self.instruction + self.program[self.instruction][1]
            else:
                self.program[self.instruction][2] = True
                self.instruction = self.instruction + 1
        print('Program Done')
        return status
    def reset(self):
        self.accumulator = 0
        self.instruction = 0
        for i in self.program:
            i[2] = False
    def debug(self):
        for i in range(len(self.program)):
            self.reset()
            #switch an instruction
            if(self.program[i][0] == 'jmp'):
                self.program[i][0] = 'nop'
            elif(self.program[i][0] == 'nop'):
                self.program[i][0] = 'jmp'
            if(self.run() == 0):
                #all done, print accumulator
                print(f"Finished: {self.accumulator}")
                break
            else:
                # that didn't work, lets set it back
                if(self.program[i][0] == 'jmp'):
                    self.program[i][0] = 'nop'
                elif(self.program[i][0] == 'nop'):
                    self.program[i][0] = 'jmp'


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        cpu = CPU()
        cpu.loadProgram(f.readlines())
        cpu.run()  
        cpu.debug()




