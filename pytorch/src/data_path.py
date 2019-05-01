

f = open("../data/office/webcam_10_list.txt", "r")
my_path = "/Users/hannancao/desktop/office31"
r = f.readlines()
for i in range(0, len(r)):
    print(r[i])
    pre_path, rest = r[i].split('office', 1)
    r[i] = my_path + rest
    print("new: " + r[i])
    f = open("../data/office/chn_webcam_10_list.txt", "a+")
    f.write(r[i])
    f.close()

