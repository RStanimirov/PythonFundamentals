quantity = int(input())
days_remaining = int(input())

ornament_per_piece = 2
tree_skirt_per_piece = 5
garlands_per_piece = 3
tree_lights_per_piece = 15

total_cost = 0
christmas_spirit = 0

# COMMENTS:
# We have days in a row, so obviously the problem can be solved by means of a for loop.
# The loop should start with 1 not 0 because the problem says "every second day".
# The problem can be solved by means of if statements, but NOT elif,
# because a given day might be simultaneously Nth,
#   this is due to the modulus division; a given day might be devisible by 3 for example,\
# and in this way could be either 3rd day or 6th day or ninth day?

for i in range(1, days_remaining + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total_cost += ornament_per_piece * quantity
        christmas_spirit += 5
    if i % 3 == 0:
        total_cost += tree_skirt_per_piece * quantity + garlands_per_piece * quantity
        christmas_spirit += 13
    if i % 5 == 0:
        total_cost += tree_lights_per_piece * quantity
        christmas_spirit += 17
        if i % 3 == 0:
            christmas_spirit += 30
    if i % 10 == 0:
        christmas_spirit -= 20
        total_cost += tree_skirt_per_piece + tree_lights_per_piece + garlands_per_piece
if i % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")
