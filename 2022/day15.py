
def add_vector(*vectors):
    if len(vectors) == 0:
        raise Exception

    final_vector = vectors[0]

    for vector in vectors[1:]:

        if len(final_vector) != len(vector):
            raise Exception

        for i in range(len(vector)):
            final_vector[i] += vector[i]
    
    return final_vector

def dist(p, q):
    return abs(p[0]-q[0])+abs(p[1]-q[1])

def max_x_distances(sensor_and_beacons):
    if len(sensor_and_beacons) == 0:
        return 0, 0
    x_min, x_max = float("+inf"), float("-inf")
    for sensor, beacon in sensor_and_beacons:
        if x_min > sensor[0]-dist(sensor, beacon):
            x_min = sensor[0]-dist(sensor, beacon)
        
        if x_max < sensor[0]+dist(sensor, beacon):
            x_max = sensor[0]+dist(sensor, beacon)
    

    return x_min, x_max

if __name__ == "__main__":

    fp = open("day15_input.txt", "r")

    sensor_and_beacons = []
    sensors = []
    beacons = []

    s_b_couple = fp.readline()
    while s_b_couple != "":
        s_b_couple = s_b_couple.split()

        sensor = tuple(map(int, (s_b_couple[2][2:-1], s_b_couple[3][2:-1])))
        beacon = tuple(map(int, (s_b_couple[8][2:-1], s_b_couple[9][2:])))

        sensors.append(sensor)
        beacons.append(beacon)

        s_b_couple = fp.readline()
    
    x_min, x_max = max_x_distances(list(zip(sensors, beacons)))

    y = 2000000


    intervals = []
    for sensor, beacon in zip(sensors, beacons):
        sensor_x, sensor_y = sensor
        distance = dist(sensor, beacon) - abs(sensor_y-y)
        if distance >= 0:
            intervals.append((sensor_x-distance, sensor_x+distance))
    
    total_covered = []
    for start, finish in intervals:
        total_covered += list(range(start, finish+1))
    total_covered = list(set(total_covered))
    
    total_pos = len(total_covered)

    for beacon_x, beacon_y in set(beacons):
        if beacon_y == y and beacon_x in total_covered:
            total_pos -= 1

    print(f"The total number of points at y={y} where a beacon is not present is: {total_pos}")

    square_bound = 4000000

    pos_coefficients = []
    neg_coefficients = []

    for sensor, beacon in zip(sensors, beacons):
        s_x, s_y = sensor
        pos_coefficients.append(s_y-s_x+dist(sensor, beacon)+1)
        pos_coefficients.append(s_y-s_x-dist(sensor, beacon)-1)
        
        neg_coefficients.append(s_y+s_x+dist(sensor, beacon)+1)
        neg_coefficients.append(s_y+s_x-dist(sensor, beacon)-1)
    
    found = False
    for pos in pos_coefficients:
        for neg in neg_coefficients:
            point = ((neg-pos)//2, (neg+pos)//2)
            if not (point[0] > 0 and point[0] < square_bound and point[1] > 0 and point[1] < 4000000):
                continue
            check = True
            for sensor, beacon in zip(sensors, beacons):
                if not (dist(sensor, beacon) < dist(sensor, point)):
                    check = False
                    break
            if check:
                freq = point[0]*4000000+point[1]
                print(f"The tuning frequency of this distress beacon is: {freq}")
                found = True
                break
        if found:
            break


    fp.close()