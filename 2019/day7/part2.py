import itertools

inp_file = open("input.txt")
original_memory = [int(x) for x in inp_file.read().split(",")]
inp_file.close()


class Program:
    def __init__(self, memory, inputs):
        self.memory = memory
        self.pc = 0
        self.inputs = inputs
        self.last_output = None

    def load_operands(self, n, modes):
        operands = []
        for i in range(n):
            operand = self.memory[self.pc + i]
            if modes[i] == "0":
                operand = self.memory[operand]
            operands.append(operand)
        self.pc += n
        return operands

    def clock(self):
        instruction = str(self.memory[self.pc]).rjust(5, "0")

        if instruction == "00099":
            return (True, self.last_output)

        operand_modes = list(instruction[:3][::-1])
        opcode = int(instruction[3:])

        self.pc += 1

        if opcode == 1:
            operand_modes[-1] = 1
            (op1, op2, op3) = self.load_operands(3, operand_modes)
            self.memory[op3] = op1 + op2
        elif opcode == 2:
            operand_modes[-1] = 1
            (op1, op2, op3) = self.load_operands(3, operand_modes)
            self.memory[op3] = op1 * op2
        elif opcode == 3:
            op1 = self.load_operands(1, [0])[0]
            self.memory[op1] = self.inputs.pop(0)
        elif opcode == 4:
            op1 = self.load_operands(1, operand_modes)[0]
            self.last_output = op1
            return (False, op1)
        elif opcode == 5:
            (op1, op2) = self.load_operands(2, operand_modes)
            if op1 != 0:
                self.pc = op2
        elif opcode == 6:
            (op1, op2) = self.load_operands(2, operand_modes)
            if op1 == 0:
                self.pc = op2
        elif opcode == 7:
            operand_modes[-1] = 1
            (op1, op2, op3) = self.load_operands(3, operand_modes)
            self.memory[op3] = int(op1 < op2)
        elif opcode == 8:
            operand_modes[-1] = 1
            (op1, op2, op3) = self.load_operands(3, operand_modes)
            self.memory[op3] = int(op1 == op2)
        else:
            print("Unknown opcode", opcode)
        return (False, None)


def run(sequence):
    programs = [Program(original_memory.copy(), [int(i)]) for i in sequence]
    programs[0].inputs.append(0)
    i = 0
    prev = None
    while True:
        return_value = None
        while return_value is None:
            finished, return_value = programs[i % 5].clock()
            if finished:
                if i % 5 == 4:
                    return return_value
                break
        prev = return_value
        i += 1
        programs[i % 5].inputs.append(prev)


highest = 0
for sequence in itertools.permutations('56789', 5):
    output = run(sequence)
    if output > highest:
        highest = output

print(highest)
