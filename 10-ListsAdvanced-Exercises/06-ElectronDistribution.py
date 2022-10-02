total_electrons = int(input())

electron_config = []
current_electron_layer = 1

while total_electrons > 0:
    electrons_per_layer = 2 * pow(current_electron_layer, 2)

    if total_electrons >= electrons_per_layer:
        electron_config.append(electrons_per_layer)
    else:
        electron_config.append(total_electrons) # Add the remaining electrons.

    total_electrons -= electrons_per_layer

    current_electron_layer += 1 # After each iteration, increase the number of layers !

print(electron_config)


