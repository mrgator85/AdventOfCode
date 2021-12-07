

#fish = [3,4,3,1,2]
fish = [5,4,3,5,1,1,2,1,2,1,3,2,3,4,5,1,2,4,3,2,5,1,4,2,1,1,2,5,4,4,4,1,5,4,5,2,1,2,5,5,4,1,3,1,4,2,4,2,5,1,3,5,3,2,3,1,1,4,5,2,4,3,1,5,5,1,3,1,3,2,2,4,1,3,4,3,3,4,1,3,4,3,4,5,2,1,1,1,4,5,5,1,1,3,2,4,1,2,2,2,4,1,2,5,5,1,4,5,2,4,2,1,5,4,1,3,4,1,2,3,1,5,1,3,4,5,4,1,4,3,3,3,5,5,1,1,5,1,5,5,1,5,2,1,5,1,2,3,5,5,1,3,3,1,5,3,4,3,4,3,2,5,2,1,2,5,1,1,1,1,5,1,1,4,3,3,5,1,1,1,4,4,1,3,3,5,5,4,3,2,1,2,2,3,4,1,5,4,3,1,1,5,1,4,2,3,2,2,3,4,1,3,4,1,4,3,4,3,1,3,3,1,1,4,1,1,1,4,5,3,1,1,2,5,2,5,1,5,3,3,1,3,5,5,1,5,4,3,1,5,1,1,5,5,1,1,2,5,5,5,1,1,3,2,2,3,4,5,5,2,5,4,2,1,5,1,4,4,5,4,4,1,2,1,1,2,3,5,5,1,3,1,4,2,3,3,1,4,1,1]
# for d in range(1, 257, 1):
#     newfish = 0
#     for f in range(len(fish)):
#         if(fish[f] == 0):
#             newfish = newfish + 1
#             fish[f] = 6
#         else:
#             fish[f] = fish[f] - 1
#     for i in range(newfish):
#         fish.append(8)

print(len(fish))

counts = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for f in fish:
    counts[f] = counts[f] + 1

for d in range(1, 257, 1):
    #handle the new fish
    ncounts = {}
    ncounts[8] = counts[0]
    ncounts[0] = counts[1]
    ncounts[1] = counts[2]
    ncounts[2] = counts[3]
    ncounts[3] = counts[4]
    ncounts[4] = counts[5]
    ncounts[5] = counts[6]
    ncounts[6] = counts[7] + counts[0]
    ncounts[7] = counts[8]
    counts = ncounts
print(counts)
total = 0
for i in range(9):
    total = total + counts[i]
print(total)