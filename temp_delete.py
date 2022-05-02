import csv

a = [[1, 2], [3, 4], [5, 6]]


yourList = [["a", "b"], ["c", "d"], ["e", "f"]]
print(yourList)
yourList2 = zip(*yourList)
print(yourList2)

with open('yourNewFileName.csv', 'w', ) as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for word in yourList2:
        # print(word)
        wr.writerow([word])

with open('yourNewFileName1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(yourList2)
