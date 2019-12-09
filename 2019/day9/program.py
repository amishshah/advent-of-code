inp_file = open("input.txt")
original_memory = [int(x) for x in inp_file.read().split(",")] + ([0] * 10000)
inp_file.close()


def parse_instruction(n):
    s = str(n).zfill(5)
    return ([int(x) for x in s[0:3][::-1]], int(s[3:]))


def run(memory):
    pc = 0
    relative_base = 0

    def val(param, mode):
        if mode == 0:
            return memory[param]
        elif mode == 1:
            return param
        elif mode == 2:
            return memory[relative_base + param]

    def addr(param, mode):
        if mode == 2:
            return relative_base + param
        return param

    while memory[pc] != 99:
        modes, opcode = parse_instruction(memory[pc])
        pc += 1
        if opcode == 1:
            n1, n2, n3 = memory[pc:pc+3]
            pc += 3
            memory[addr(n3, modes[2])] = val(n1, modes[0]) + val(n2, modes[1])
        elif opcode == 2:
            n1, n2, n3 = memory[pc:pc+3]
            pc += 3
            memory[addr(n3, modes[2])] = val(n1, modes[0]) * val(n2, modes[1])
        elif opcode == 3:
            n = addr(memory[pc], modes[0])
            pc += 1
            memory[n] = int(input("Enter an input: "))
        elif opcode == 4:
            n = val(memory[pc], modes[0])
            pc += 1
            print(n)
        elif opcode == 5:
            n1, n2 = memory[pc:pc+2]
            pc += 2
            if val(n1, modes[0]) != 0:
                pc = val(n2, modes[1])
        elif opcode == 6:
            n1, n2 = memory[pc:pc+2]
            pc += 2
            if val(n1, modes[0]) == 0:
                pc = val(n2, modes[1])
        elif opcode == 7:
            n1, n2, n3 = memory[pc:pc+3]
            pc += 3
            if val(n1, modes[0]) < val(n2, modes[1]):
                memory[addr(n3, modes[2])] = 1
            else:
                memory[addr(n3, modes[2])] = 0
        elif opcode == 8:
            n1, n2, n3 = memory[pc:pc+3]
            pc += 3
            if val(n1, modes[0]) == val(n2, modes[1]):
                memory[addr(n3, modes[2])] = 1
            else:
                memory[addr(n3, modes[2])] = 0
        elif opcode == 9:
            n = val(memory[pc], modes[0])
            pc += 1
            relative_base += n


run(original_memory.copy())
