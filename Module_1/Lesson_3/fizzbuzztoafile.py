with open("results.txt", "w") as w:
    with open("Numbers.txt") as f:
        for line in f.readlines():
            i = line.split()
            fizz = int(i[0])
            buzz = int(i[1])
            n = int(i[2])
            for i in range(1, n + 1):
                if not i % fizz and not i % buzz:
                    w.write("FB ")
                elif not i % buzz:
                    w.write("B ")
                elif not i % fizz:
                    w.write("F ")
                else:
                    w.write(str(i) + " ")
            w.write("\n")
