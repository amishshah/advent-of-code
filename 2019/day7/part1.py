import itertools

inp_file = open("input.txt")
original_memory = [int(x) for x in inp_file.read().split(",")]
inp_file.close()


def run(inputs):
    pc = 0

    def load_operands(n, modes, pc):
        operands = []
        for i in range(n):
            operand = memory[pc + i]
            if modes[i] == "0":
                operand = memory[operand]
            operands.append(operand)
        return operands

    memory = original_memory.copy()
    while memory[pc] != 99:
        instruction = str(memory[pc]).rjust(5, "0")

        operand_modes = list(instruction[:3][::-1])
        opcode = int(instruction[3:])

        pc += 1

        if opcode == 1:
            operand_modes[-1] = 1
            (op1, op2, op3) = load_operands(3, operand_modes, pc)
            pc += 3
            memory[op3] = op1 + op2
        elif opcode == 2:
            operand_modes[-1] = 1
            (op1, op2, op3) = load_operands(3, operand_modes, pc)
            pc += 3
            memory[op3] = op1 * op2
        elif opcode == 3:
            op1 = load_operands(1, [0], pc)[0]
            pc += 1
            memory[op1] = inputs.pop(0)
        elif opcode == 4:
            op1 = load_operands(1, operand_modes, pc)[0]
            pc += 1
            return op1
        elif opcode == 5:
            (op1, op2) = load_operands(2, operand_modes, pc)
            pc += 2
            if op1 != 0:
                pc = op2
        elif opcode == 6:
            (op1, op2) = load_operands(2, operand_modes, pc)
            pc += 2
            if op1 == 0:
                pc = op2
        elif opcode == 7:
            operand_modes[-1] = 1
            (op1, op2, op3) = load_operands(3, operand_modes, pc)
            pc += 3
            memory[op3] = int(op1 < op2)
        elif opcode == 8:
            operand_modes[-1] = 1
            (op1, op2, op3) = load_operands(3, operand_modes, pc)
            pc += 3
            memory[op3] = int(op1 == op2)
        else:
            print("Unknown opcode", opcode)


def output_for_sequence(sequence):
    prev = 0
    for i in sequence:
        prev = run([int(i), prev])
    return prev


highest = 0
for sequence in itertools.permutations('01234', 5):
    output = output_for_sequence(sequence)
    if output > highest:
        highest = output

print(highest)