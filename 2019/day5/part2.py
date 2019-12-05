inp_file = open("input.txt")
memory = [int(x) for x in inp_file.read().split(",")]
inp_file.close()

pc = 0


def load_operands(n, modes):
    global pc
    operands = []
    for i in range(n):
        operand = memory[pc + i]
        if modes[i] == "0":
            operand = memory[operand]
        operands.append(operand)
    pc += n
    return operands


while memory[pc] != 99:
    instruction = str(memory[pc]).rjust(5, "0")

    operand_modes = list(instruction[:3][::-1])
    opcode = int(instruction[3:])

    pc += 1

    if opcode == 1:
        operand_modes[-1] = 1
        (op1, op2, op3) = load_operands(3, operand_modes)
        memory[op3] = op1 + op2
    elif opcode == 2:
        operand_modes[-1] = 1
        (op1, op2, op3) = load_operands(3, operand_modes)
        memory[op3] = op1 * op2
    elif opcode == 3:
        op1 = load_operands(1, [0])[0]
        memory[op1] = int(input("Enter input: "))
    elif opcode == 4:
        op1 = load_operands(1, operand_modes)[0]
        print(op1)
    elif opcode == 5:
        (op1, op2) = load_operands(2, operand_modes)
        if op1 != 0:
            pc = op2
    elif opcode == 6:
        (op1, op2) = load_operands(2, operand_modes)
        if op1 == 0:
            pc = op2
    elif opcode == 7:
        operand_modes[-1] = 1
        (op1, op2, op3) = load_operands(3, operand_modes)
        memory[op3] = int(op1 < op2)
    elif opcode == 8:
        operand_modes[-1] = 1
        (op1, op2, op3) = load_operands(3, operand_modes)
        memory[op3] = int(op1 == op2)
    else:
        print("Unknown opcode", opcode)
