# scores = [34, 56, 64]

# avg = sum(scores) / len(scores)
# print("Avg: ", avg)

# * with input scores
scores = []
for i in  range(3):
    x = int(input("value: "))
    scores.append(x)

avg = sum(scores) / len(scores)
print("Avg: ", avg)