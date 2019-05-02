

f = open("../data/office-home/Real_World_shared.txt", "r")
my_path = "/work/xuweinan/OfficeHomeDataset"
r = f.readlines()
for i in range(0, len(r)):
    print(r[i])
    pre_path, rest = r[i].split('office-home', 1)
    r[i] = my_path + rest
    print("new: " + r[i])
    f = open("../data/office-home/chn_Real_World_shared.txt", "a+")
    f.write(r[i])
    f.close()

