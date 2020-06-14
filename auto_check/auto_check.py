import requests
import os
import re
import subprocess
from bs4 import BeautifulSoup

current_dir = os.getcwd() + "/"
abc, prob = input().split()
# print(current_dir)
DIR = "./data/"

#問題ページのURL
problem_url = "https://atcoder.jp/contests/" + abc + "/tasks/" + abc + "_" + prob

#問題ページのhtmlを取得
problem_html = requests.get(problem_url)
#BeautifulSoupでパース処理
problem_soup = BeautifulSoup(problem_html.content, "html.parser")
# print(problem_soup)
#サンプルデータを取得。標準入力の形式、入力例、出力例を得る
testcase = problem_soup.find_all("pre")
#n%2 == 0であれば英語表記も含まれているので省く
n = len(testcase) if len(testcase)%2 != 0 else len(testcase)//2

#スクリプトがある絶対ファイルを取得
# script_path = os.path.dirname(os.path.abspath(__file__)) 

# path_sh = os.path.join(script_path, "./test.sh")
# subprocess.run(["sh", path_sh])

# #サンプル入出力をローカルに保存
for i in range(1, n, 2):
    '''
    testcase[1] -> Sample1の入力
    testcase[2] -> Sample1の出力
    '''
    case_num = (i+1)//2
    # print(testcase[i])
    in_path = DIR + prob + "in" + str(case_num) + ".txt"
    with open(in_path, "w") as f_in:
        f_in.write(testcase[i].get_text())
    
    out_path = DIR + prob + "out" + str(case_num) + ".txt"
    with open(out_path, "w") as f_out:
        f_out.write(testcase[i+1].get_text())

for i in range(1, n, 2):
    case_num = int((i + 1) / 2)

    # 標準入力を in?.txt, 標準出力を res?.txt に設定してプログラムを実行
    in_path = DIR + prob + "in" + str(case_num) + ".txt"
    res_path = DIR + prob + "res" + str(case_num) + ".txt"
    subprocess.run(["sh", "test.sh", current_dir + prob], stdin=open(in_path, "r"), stdout=open(res_path, "w"))

# サンプル出力と実行結果が合ってるか確認
is_correct = True
for i in range(1, n, 2):
    case_num = int((i + 1) / 2)

    out_path = DIR + prob + "out" + str(case_num) + ".txt"
    with open(out_path, "r") as f_out:
        out_str = "".join(f_out.read().splitlines())

    res_path = DIR + prob + "res" + str(case_num) + ".txt"
    with open(res_path, "r") as f_res:
        res_str = "".join(f_res.read().splitlines())

    if out_str != res_str:
        is_correct = False
        print("Sample " + str(case_num) + " WA...")
    else:
        print("Sample " + str(case_num) + " AC!")

if is_correct:
    print("Sample OK!")
else:
    print("Wrong Answer exist.")
'''


'''