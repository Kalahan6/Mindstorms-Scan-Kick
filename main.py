import random

movement_interval = 3.5
number_of_scans = 6
scans = {}
movement_modifier = 1.2


def scan_room():
    for i in range(0, number_of_scans):
        print("moving the amount of movement_interval"
              )  # replace with motor turn equal
        random_test_scan = random.randint(
            0, 10)  #replace with current distance sensor measurement
        scans[i] = random_test_scan


scan_room()
sorted_scans = dict(sorted(scans.items(), key=lambda item: item[1]))

print("All scans: %s" % (scans))
print("Scans sorted by distance: %s" % sorted_scans)

# turn back to default position
turn_back = number_of_scans * movement_interval
print("turning back to default position by moving %s" % turn_back)

for x in sorted_scans:
    turn_angle = sorted_scans[x] * movement_interval
    print(turn_angle)
