

f = open("../data/office/amazon_31_list.txt", "r")
my_path = "/home/ureca/chn/office31"
r = f.readlines()
for i in range(0, len(r)):
    print(r[i])
    pre_path, rest = r[i].split('office', 1)
    r[i] = my_path + rest
    print("new: " + r[i])
    f = open("../data/office/chn_amazon_31_list.txt", "a+")
    f.write(r[i])
    f.close()

