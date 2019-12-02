with open("input.txt") as inp_file:
    data = [int(x) for x in inp_file.read().split(",")]

    # patch
    data[1] = 12
    data[2] = 2

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

    print(data)
