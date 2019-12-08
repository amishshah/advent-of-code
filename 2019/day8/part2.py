inp_file = open("input.txt")
file_data = inp_file.read().strip()
inp_file.close()

width = 25
height = 6

layer_size = width * height

computed_image = ["2"] * layer_size

layers = [
    file_data[i*layer_size:(i+1)*layer_size]
    for i in range(len(file_data) // layer_size)
]

lowest = (None, layer_size)
for layer in layers:
    for i, pixel in enumerate(layer):
        current = computed_image[i]
        if current == "2":
            computed_image[i] = pixel

image_rows = [
    computed_image[i*width:(i+1)*width]
    for i in range(height)
]

for row in image_rows:
    print("".join(row).replace("0", "2").replace("2", " "))
