# Pain is imminent


import math


n, k = map(int, input().split())
qr, qc = map(int, input().split())


def calc_distance(x1, x2, y1, y2):
    return int(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))


directions = {"l": -1, "r": -1, "u": -1, "d": -
              1, "ul": -1, "ur": -1, "dl": -1, "dr": -1}

for i in range(k):
    kr, kc = map(int, input().split())

    if abs(kr - qr) == abs(kc - qc):
        if kc > qc:
            if kr < qr:
                if directions["dr"] != -1:
                    if min([qr - kr, kc - qc]) - 1 < directions["dr"]:
                        directions["dr"] = min([qr - kr, kc - qc]) - 1
                else:
                    directions["dr"] = min([qr - kr, kc - qc]) - 1
            elif kr > qr:
                if directions["ur"] != -1:
                    if min([kr - qr, kc - qc]) - 1 < directions["ur"]:
                        directions["ur"] = min([kr - qr, kc - qc]) - 1
                else:
                    directions["ur"] = min([kr - qr, kc - qc]) - 1
        elif kc < qc:
            if kr < qr:
                if directions["dl"] != -1:
                    if min([qr - kr, qc - kc]) - 1 < directions["dl"]:
                        directions["dl"] = min([qr - kr, qc - kc]) - 1
                else:
                    directions["dl"] = min([qr - kr, qc - kc]) - 1
            elif kr > qr:
                if directions["ul"] != -1:
                    if min([kr - qr, qc - kc]) - 1 < directions["ul"]:
                        directions["ul"] = min([kr - qr, qc - kc]) - 1
                else:
                    directions["ul"] = min([kr - qr, qc - kc]) - 1

    if kr == qr:
        if kc < qc:
            if directions["l"] != -1:
                if qc - kc - 1 < directions["l"]:
                    directions["l"] = qc - kc - 1
            else:
                directions["l"] = qc - kc - 1
        elif kc > qc:
            if directions["r"] != -1:
                if kc - qc - 1 < directions["r"]:
                    directions["r"] = kc - qc - 1
            else:
                directions["r"] = kc - qc - 1

    if kc == qc:
        if kr < qr:
            if directions["d"] != -1:
                if qr - kr - 1 < directions["d"]:
                    directions["d"] = qr - kr - 1
            else:
                directions["d"] = qr - kr - 1
        elif kr > qr:
            if directions["u"] != -1:
                if kr - qr - 1 < directions["u"]:
                    directions["u"] = kr - qr - 1
            else:
                directions["u"] = kr - qr - 1


total = 0

for key in directions:
    # print("Before:", total)
    # print(key)
    if directions[key] != -1:
        total += directions[key]
    else:
        if key == 'l':
            total += qc - 1
        if key == 'r':
            total += n - qc
        if key == 'u':
            total += n - qr
        if key == 'd':
            total += qr - 1
        
        if key == 'ul':
            maxDist = min([n - qr, qc - 1])
            # print("Distance from (%s %s) to (%s %s): %s" % (qc, qr, qc - maxDist,
            #                                                 qr + maxDist, calc_distance(qc, qc - maxDist, qr, qr + maxDist)))
            # print("Max distance:", maxDist)
            total += maxDist

        if key == 'ur':
            maxDist = min([n - qr, n - qc])
            # print("Distance from (%s %s) to (%s %s): %s" % (qc, qr, qc + maxDist,
            #                                                 qr + maxDist, calc_distance(qc, qc + maxDist, qr, qr + maxDist)))
            # print("Max distance:", maxDist)
            total += maxDist

        if key == 'dr':
            maxDist = min([qr - 1, n - qc])
            # print("Distance from (%s %s) to (%s %s): %s" % (qc, qr, qc + maxDist,
            #                                                 qr - maxDist, calc_distance(qc, qc + maxDist, qr, qr - maxDist)))
            # print("Max distance:", maxDist)
            total += maxDist

        if key == 'dl':
            maxDist = min([qr - 1, qc - 1])
            # print("Distance from (%s %s) to (%s %s): %s" % (qc, qr, qc - maxDist,
            #                                                 qr - maxDist, calc_distance(qc, qc - maxDist, qr, qr - maxDist)))
            # print("Max distance:", maxDist)
            total += maxDist

        # print("After:", total)

print(total)
