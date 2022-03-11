import re
s = re.sub(r'[.,;:-?-!]', '', input()).lower().split()
result = {}
for i in s:
    if i not in result:
        result[i] = result.get(i, s.count(i))
minvalue = min(result.values())
minkey = min(result)
for key, value in sorted(result.items(), reverse=True):
    if value == minvalue:
        minvalue = value
        minkey = key
print(minkey)



# result = {value: key for key, value in result.items()}




# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# a = sorted([i for i in text])
# result = {}
# letters = []
# counts = []
# prez = 0
# for i in range(len(a)):
#     prez += 1
#     if i + 1 != len(a) and a[i] != a[i + 1]:
#         letters.append(a[i])
#         counts.append(prez)
#         prez = 0
# result = dict(zip(letters, counts))


# for i in s.split():
#     if i not in result:
#         result[i] = result.get(i, s.split().count(i))
# result = {value: key for key, value in result.items()}
# print(result[max(result)])