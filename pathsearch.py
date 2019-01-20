with open('graph_2p.txt', 'r') as f:
    i = 0
    hrany = []
    for line in f:
        if i == 0:
            highest = int(line)
            i += 1
        elif i == 1:
            desired = list(map(int, line.split()))
            i += 1
        elif i == 2:
            what_to_do = str(line)
            what_to_do = what_to_do[:-1]
            i += 1
        else:
            hrany.append(list(map(int, line.split())))


zasobnik = []
now = desired[0]
cesta = {}
visited = []

while True:
    if now == desired[1]:
        i = 0
        back_now = desired[1]
        path = []
        while True:
            path.append(back_now)
            if back_now == desired[0]:

                break
            else:

                back_now = cesta[back_now]
                i += 1

        if what_to_do == "LEN":
            print(i)
        elif what_to_do == "PATH":
            for j in range(len(path) - 1, -1, -1):
                print(path[j], end=" ")
        break
    else:
        for hrana in hrany:
            if hrana[0] == now:
                if hrana[1] not in visited and hrana[1] not in zasobnik:
                    zasobnik.append(hrana[1])
                    cesta[hrana[1]] = now
            elif hrana[1] == now:
                if hrana[0] not in visited and hrana[0] not in zasobnik:
                    zasobnik.append(hrana[0])
                    cesta[hrana[0]] = now

        visited.append(now)
        if len(zasobnik) > 0:
            now = zasobnik.pop(0)
        else:
            print("None")
            break
