# import requests
#
#
# url_base = 'https://stepik.org/media/attachments/course67/3.6.3/'
#
#
# with open("D:\\Download\\dataset_3378_3 (1).txt", 'r') as file:
#     first_url = file.readline().strip()
#
# filename = requests.get(first_url).text
#
# while filename.count('We') <1:
#     filename = requests.get(url_base + filename).text
#     print(filename)


# def modify_list(l):
#     for i in range(len(l) - 1, -1, -1):
#         if l[i] % 2 != 0:
#             l.pop(i)
#     a = len(l)
#     for i in range(a):
#         l.append(l[i] // 2)
#     for i in range(a):
#         l.pop(0)
#
#
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#
#     elif 2 * key in d:
#         d[2 * key].append(value)
#
#     else:
#         d[2 * key] = [value]


# st = str(input()).lower().split(' ')
# res = {}
#
# for items in st:
#
#     res[items] = st.count(items)
#
#
# for item in res:
#     print("{} {}".format(item, res[item]))


# n = int(input())
# args = []
# d = {}
# for i in range(n):
#     m = int(input())
#     args.append(m)
#
# sets = set(args)
#
# for each in sets:
#     d[each] = f(each)
#
# for items in range(len(args)):
#     print(d[args[items]])

# # Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
# a=[int(input()) for i in range(int(input()))]
# b={x:f(x) for x in set(a)}
# for i in a:
#     print(b[i])

# def anagrams(word, words):
#     for i in range(len(words) - 1, -1, -1):
#         if len(word) != len(words[i]):
#             words.remove(words[i])
#
#     for i in range(len(words) - 1, -1, -1):
#         for letters in words[i]:
#             if word.count(letters) != words[i].count(letters):
#                 words.remove(words[i])

#  reading from file
# f = open('D:\\Python\\Projects\\Stepik\\annual2010.txt', 'r')
# cot = f.readline()
# f.close()


#  reading from file #2
# with open('D:\\Python\\Projects\\Stepik\\annual2010.txt') as file:
#     for lines in file:
#         s.append(lines.strip())

# for lines in range(len(s)):
#     print(s[lines], end="\n")


# writing in file
# out = open('D:\\Python\\Projects\\Stepik\\test.txt', 'w')
# for lines in range(len(s)):
#     out.write(s[lines] + "\n")
# out.close()

# writing in file #2
# with open('D:\\Python\\Projects\\Stepik\\test.txt', 'w') as ff:
#     for lines in range(len(s)):
#         ff.write(s[lines] + '\n')


# with open('D:\\Python\\Projects\\Stepik\\dataset_3363_2.txt') as file:
#     code = file.readline().strip()
#
#
#
#
# leng = len(code)
# code += "  "
# result = ""
# for chars in range(leng):
#     if code[chars].isalnum():
#         if not code[chars].isnumeric():
#             result += code[chars]
#             if code[chars + 1].isnumeric() and not code[chars + 2].isnumeric():
#                 result += code[chars] * (int(code[chars + 1]) - 1)
#
#
#
#         elif code[chars].isnumeric() and code[chars + 1].isnumeric():
#             result += result[-1] * (int(code[chars]) * 10 + int(code[chars + 1]) - 1)
#
#
# with open('D:\\Python\\Projects\\Stepik\\result.txt', 'w') as res:
#     res.write(result)


# with open(r'D:\\Python\\Projects\\Stepik\\dataset_3363_3.txt') as f:
#    lst = f.read().lower().translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~—')).split()
# # составляем словарь подсчёта (падежи, к слову, также не учитываются)
# res = {x:lst.count(x) for x in lst}
# print(max(res, key=res.get)) # первое из наиболее часто встречающихся
# print(res[max(res, key=res.get)])
# function order(words){
#     s.append(words.split(" "))
#     sort(s)
#     for i in range(len(s)):
#         si += s[i]
#     return si
# }

# lst = [[]]
# with open(r'D:\\Python\\Projects\\Stepik\\dataset_3363_4.txt', encoding='utf-8') as f:
#     for lines in f:
#         lst.append(lines.strip().split(";"))
#
# lst.pop(0)
#
# a = 0
# b = 0
# c = 0
# print(len(lst))
# with open('D:\\Python\\Projects\\Stepik\\New.txt', 'w') as ff:
#     for students in range(len(lst)):
#         ff.write(str((int(lst[students][1]) + int(lst[students][2]) + int(lst[students][3])) / 3) + " " + '\n')
#         a += int(lst[students][1])
#         b += int(lst[students][2])
#         c += int(lst[students][3])
#
#     ff.write(str(a/len(lst)) + " " + str(b/len(lst)) + " " + str(a/len(lst)))
#     #     ff.write(str(int(lst[students][3])) + '\n')


# with open('D:\\Python\\Projects\\Stepik\\dataset_3363_4.txt') as f:
#     strings = [s.rstrip() for s in f.readlines()]
# otsenki = [s.split(';')[1:] for s in strings]
# with open('D:\\Python\\Projects\\Stepik\\N.txt', 'w') as ff:
#     for x in otsenki:
#         ff.write(str(sum(map(int, x))/len(x)) + "\n")
#     sr_mat = sum([int(x[0]) for x in otsenki]) / len(otsenki)
#     sr_fiz = sum([int(x[1]) for x in otsenki]) / len(otsenki)
#     sr_rus = sum([int(x[2]) for x in otsenki]) / len(otsenki)
#     ff.write(str(sr_mat) +" "+ str(sr_fiz)+ " " + str(sr_rus))

# s = {""}
# for words in range(int(input())):
#     s.add(str(input()).strip().lower())
#
# check = ""
# #
# for words in range(int(input())):
#     check += (str(input()).strip().lower()) + ' '
# check = check.split(" ")
# result = {''}
# result.pop()
# for lines in check:
#     if lines not in s:
#         result.add(lines)
#
# print(*result)

# x, y = 0, 0
# s = []
# for i in range(int(input())):
#     s.append(str(input()).lower())
#
# for j in s:
#     if j.count("юг") == 1:
#         y -= int(j.split(" ")[1])
#     if j.count("север") == 1:
#         y += int(j.split(" ")[1])
#     if j.count("восток") == 1:
#         x += int(j.split(" ")[1])
#     if j.count("запад") == 1:
#         x -= int(j.split(" ")[1])

# print(x, " ", y)
#
# letters = str(input())
# subs = str(input())
#
# todo = str(input())
# to_reverse = str(input())
#
# r = ""
# r1 = ""
# for j in range(len(todo)):
#     r += subs[letters.find(todo[j])]
#
# for k in range(len(to_reverse)):
#     r1 += letters[subs.find(to_reverse[k])]
# print(r)
# print(r1)
#
# results =[]
# for match in range(int(input())):
#     results.append(input())
# dicti = {}
# temp =[]
# for match in results:
#     temp = match.split(";")
#     dicti[temp[0]] = [0, 0, 0, 0, 0]
#     dicti[temp[2]] = [0, 0, 0, 0, 0]
# for match in results:
#     temp = match.split(";")
#     if int(temp[1]) > int(temp[-1]):
#         dicti[temp[0]][0] += 1
#         dicti[temp[0]][1] += 1
#         dicti[temp[0]][4] += 3
#         dicti[temp[2]][0] += 1
#         dicti[temp[2]][3] += 1
#     elif int(temp[1]) == int(temp[-1]):
#         dicti[temp[0]][0] += 1
#         dicti[temp[0]][2] += 1
#         dicti[temp[0]][4] += 1
#         dicti[temp[2]][0] += 1
#         dicti[temp[2]][2] += 1
#         dicti[temp[2]][4] += 1
#     else:
#         dicti[temp[0]][0] += 1
#         dicti[temp[0]][3] += 1
#         dicti[temp[2]][0] += 1
#         dicti[temp[2]][1] += 1
#         dicti[temp[2]][4] += 3
# keys_number = dicti.keys()
# for k in keys_number:
#     print(str(k) + ":", dicti.get(str(k))[0], dicti.get(str(k))[1],
#           dicti.get(str(k))[2], dicti.get(str(k))[3], dicti.get(str(k))[4])
#

# data = []
# with open("D:\\Download\\dataset_3380_5.txt", 'r') as file:
#     for lines in file:
#         data.append(lines.replace("\t", ' ').replace('\n', ''))
#
#
# def form(array, cl):
#     count = 0
#     res = [0, 0]
#     for i in range(len(array)):
#         temp = str(array[i]).split(' ')
#         if int(temp[0]) == cl:
#             res[0] = cl
#             res[1] += int(temp[2])
#             count += 1
#     if res[1] != 0:
#         res[1] = res[1] / count
#         print(res[0], res[-1])
#     else:
#         print(res[0], '-')
#
#
# for i in range(1, 12):
#     form(data, i)


n, k = map(int, input().split())


def comb(n, k):
    if 1 <= n <= 10 and 0 <= k <= 10:
        if k > n:
            return 0
        elif k == 0:
            return 1
        elif k == n:
            return 1
        else:
            return comb(n-1, k) + comb(n-1, k-1)


print(comb(3, 2))