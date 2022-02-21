s = input().split()
my_list = []
my_list.append([])
n=1
if len(s) == 1:
    my_list.append(s)
elif len(s) == 2:
    for i in range(len(s)):
        my_list.append([s[i]])
    my_list.append(s)
else:
    for i in range(len(s)):
        my_list.append([s[i]])
    n += 1
    k = n
    for j in range(0, len(s)):
        my_list.append(s[j:k])
        k += n

    my_list.append(s)
# my_list.append(s)
print(set(my_list))



# n = int(input())
# my_list = []
# for i in range(n):
#     elem = [i+1 for i in range(n)]
#     my_list.append(elem)
# for i in my_list:
#     print(i)