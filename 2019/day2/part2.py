inp_file = open("input.txt")
original_data = [int(x) for x in inp_file.read().split(",")]
inp_file.close()


def run(noun, verb):
    data = original_data.copy()
    # patch
    data[1] = noun
    data[2] = verb

    pc = 0
    while data[pc] != 99:
        opcode = data[pc]
        op1, op2, op3 = [data[pc+1], data[pc+2], data[pc+3]]
        pc += 4
        if opcode == 1:
            data[op3] = data[op1] + data[op2]
        elif opcode == 2:
            data[op3] = data[op1] * data[op2]
        else:
            print(f"Unknown opcode {opcode}")
            break

    return data[0]


for i in range(100):
    for j in range(100):
        if run(i, j) == 19690720:
            print(i, j)
            exit(0)
