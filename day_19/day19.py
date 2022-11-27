def b_matches(b_set1, b_set2):
    offsets = []
    used = []
    found_pairs = set()
    for j in range(3):
        for c in [1,-1]:
            for i in range(3):
                if i in used:
                    continue

                counts = {}

                dim_i_1 = [c*x[i] for x in b_set1]
                dim_2 = [x[j] for x in b_set2]
                for n in dim_i_1:
                    for m in dim_2:
                        diff = m-n
                        if diff in counts:
                            counts[diff] += 1
                            if counts[diff] == 12:
                                adjusted_1 = [x+diff for x in dim_i_1]
                                for x in dim_2:
                                    if x in adjusted_1:
                                        adjusted_1.remove(x)
                                if len(dim_i_1) - len(adjusted_1) >= 12:
                                    offsets.append((i,c,diff))
                                    used.append(i)
                        else:
                            counts[diff] = 1
    if len(offsets) == 3:
        return offsets
    else:
        return None

def calc_offset(offset1, offset2):
    # 1 to 0 [(2, -1, 1220), (1, 1, 23), (0, 1, 100)]
    # 2 to 1 [(0, 1, -18), (2, -1, 1194), (1, 1, 140)]    
    # 2 to 0 [(1,-1,1220-140),(2,-1,23+1194),(0,1,82)]

    return [
        (offset2[offset1[0][0]][0],
         offset2[offset1[0][0]][1]*offset1[0][1],
         offset1[0][2]+offset2[offset1[0][0]][2]*offset1[0][1]),
        (offset2[offset1[1][0]][0],
         offset2[offset1[1][0]][1]*offset1[1][1],
         offset1[1][2]+offset2[offset1[1][0]][2]*offset1[1][1]),
        (offset2[offset1[2][0]][0],
         offset2[offset1[2][0]][1]*offset1[2][1],
         offset1[2][2]+offset2[offset1[2][0]][2]*offset1[2][1])
    ]

def rotate_data(data,offsets):
    # 1 to 0 [(2, -1, 1220), (1, 1, 23), (0, 1, 100)]
    # [100,200,-300]
    # output: [1520,223,200]
    rot_data = []
    for datum in data:
        rot_datum = [
            datum[offsets[0][0]]*offsets[0][1]+offsets[0][2],
            datum[offsets[1][0]]*offsets[1][1]+offsets[1][2],
            datum[offsets[2][0]]*offsets[2][1]+offsets[2][2]]
        rot_data.append(rot_datum)
    
    return rot_data

if __name__ == "__main__":
    with open('input.txt') as f:
        rdata = [x.strip() for x in f.read().split('\n\n')]

    data = [[[int(z) for z in y.split(',')] for y in x.split('\n')[1:]] for x in rdata]

    used = set()
    rel_offsets = {}
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
            else:
                result = b_matches(data[j],data[i])
                if result:
                    if i not in rel_offsets:
                        rel_offsets[i] = {j:result}
                    else:
                        rel_offsets[i][j] = result

    true_offsets = {}
    for sensor in rel_offsets[0]:
        true_offsets[sensor] = rel_offsets[0][sensor]

    while len(true_offsets) < len(data):
        new_true_offsets = {}
        for sensor in true_offsets:
            new_rel_offsets = rel_offsets[sensor]
            for new_sensor in new_rel_offsets:
                if new_sensor in true_offsets or new_sensor in new_true_offsets:
                    continue
                else:
                    new_true_offsets[new_sensor] = calc_offset(true_offsets[sensor],rel_offsets[sensor][new_sensor])
        for sensor in new_true_offsets:
            true_offsets[sensor] = new_true_offsets[sensor]

    beacons = data[0]
    for i in range(1,len(data)):
        new_beacons = rotate_data(data[i],true_offsets[i])
        for new_beacon in new_beacons:
            if new_beacon not in beacons:
                beacons.append(new_beacon)

                
    print(len(beacons))

    scanners = []
    for true_offset in true_offsets:
        s_x = true_offsets[true_offset][0][2]
        s_y = true_offsets[true_offset][1][2]
        s_z = true_offsets[true_offset][2][2]
        scanners.append((s_x,s_y,s_z))
        
    max_distance = 0
    for i in range(len(scanners)):
        for j in range(len(scanners)):
            if i == j:
                continue
            x_d = abs(scanners[i][0] - scanners[j][0])
            y_d = abs(scanners[i][1] - scanners[j][1])
            z_d = abs(scanners[i][2] - scanners[j][2])
            man_distance = x_d + y_d + z_d
            if man_distance > max_distance:
                max_distance = man_distance
    print(max_distance)
