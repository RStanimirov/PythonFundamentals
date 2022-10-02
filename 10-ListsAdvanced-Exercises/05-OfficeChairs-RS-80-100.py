# Lists Advanced Exercises, 05-Office Chairs, RS Jun 2021
rooms_count = int(input())

total_free_chairs = 0
is_enough_chairs = False
chairs_counter = 0
visitors_counter = 0

for i in range(rooms_count):
    next_room = input().split()
    chairs_data = next_room[0]
    visitors_data = next_room[1]
    chairs_counter = int(len(chairs_data))
    visitors_counter = int(visitors_data)

    if chairs_counter < visitors_counter:
        is_enough_chairs = False
        needed_chairs = visitors_counter - chairs_counter
        room = i + 1
        print(f"{needed_chairs} more chairs needed in room {room}")

    elif chairs_counter >= visitors_counter:
        is_enough_chairs = True
        free_chairs = chairs_counter - visitors_counter
        total_free_chairs += free_chairs

if is_enough_chairs and chairs_counter >= visitors_counter:
    print(f"Game On, {total_free_chairs} free chairs left")





