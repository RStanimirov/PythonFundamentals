trip_stops = input()

command = input()
is_stop = False
while command != "Travel":
    data = command.split(':')
    action = data[0]

    if action == "Add Stop":
        idx = int(data[1])
        added_stop = data[2]
        if idx >= 0 and idx < len(trip_stops):
            first_part = trip_stops[:idx]
            second_part = trip_stops[idx:]
            trip_stops = first_part + added_stop + second_part
            is_stop = True
        if is_stop:
            print(trip_stops)

    elif action == "Remove Stop":
        start_idx = int(data[1])
        end_idx = int(data[2])
        if start_idx >= 0 and start_idx < len(trip_stops) and end_idx >= 0 and end_idx < len(trip_stops):
            first_part = trip_stops[:start_idx]
            part_to_remove = trip_stops[start_idx:end_idx + 1]
            last_part = trip_stops[end_idx + 1:]
            trip_stops = first_part + last_part
            is_stop = True
        if is_stop:
            print(trip_stops)

    elif action == "Switch":
        old_stop = data[1]
        new_stop = data[2]
        if old_stop in trip_stops:
            trip_stops = trip_stops.replace(old_stop, new_stop)
            is_stop = True
        if is_stop:
            print(trip_stops)

    command = input()

print(f"Ready for world tour! Planned stops: {trip_stops}")