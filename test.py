s = input().split()
my_list = []
my_list.append([])
n=1
for i in range(len(s)):
    my_list.append([s[i]])
for i in range(0,len(s),n):
    my_list.append(s[i:n])
    n += 1
my_list.append(s)
print(my_list)



# n = int(input())
# my_list = []
# for i in range(n):
#     elem = [i+1 for i in range(n)]
#     my_list.append(elem)
# for i in my_list:
#     print(i)