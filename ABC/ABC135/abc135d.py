import re

s = input()
s_max = int(s.replace("?","9"))
s_min = int(s.replace("?","0"))
s_int = re.findall(r"[0-9]{1}", s)
s_int_index = s.find(r"[0-9]{1}")
flag = True
num = 1

print(s_max,s_min,s_int,s_int_index)
