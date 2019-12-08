inp_file = open("input.txt")
file_data = inp_file.read().strip()
inp_file.close()

width = 25
height = 6

layer_size = width * height

layers = [
    file_data[i*layer_size:(i+1)*layer_size]
    for i in range(len(file_data) // layer_size)
]

lowest = (None, layer_size)
for layer in layers:
    num_zeroes = layer.count("0")
    if num_zeroes < lowest[1]:
        lowest = (layer, num_zeroes)

layer = lowest[0]
print(layer.count("1") * layer.count("2"))
