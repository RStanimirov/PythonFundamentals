snowballs_n = int(input())
max_snow = 0
max_time = 0
max_quality = 0
max_value = 0

for i in range(0, snowballs_n):
    snowballs_snow = int(input())
    snowballs_time = int(input())
    snowballs_quality = int(input())

    snowballs_value = (snowballs_snow / snowballs_time) ** snowballs_quality

    if snowballs_value >= max_value:
        max_value = snowballs_value
        max_snow = snowballs_snow
        max_time = snowballs_time
        max_quality = snowballs_quality

print(f"{max_snow} : {max_time} = {int(max_value)} ({max_quality})")

