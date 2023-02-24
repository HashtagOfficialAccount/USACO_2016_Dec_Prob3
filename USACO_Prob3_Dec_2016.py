x = open("cowsignal.in")
y = open("cowsignal.out","w")
info = x.readline()
info_list = [int(x) for x in info.split()]
m = []
for i in range(info_list[0]):
    line = x.readline()
    text = ""
    for k in line:
        z = k * info_list[2]
        text += z
    for z in range(info_list[2]):
        y.write(text.strip()+"\n")
x.close()
y.close()

