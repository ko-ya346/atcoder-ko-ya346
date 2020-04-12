import requests
from bs4 import BeautifulSoup

#問題ページのURL
problem_url = "https://atcoder.jp/contests/abc147/tasks/abc147_a"

#問題ページの情報を取得
problem_html = requests.get(problem_url)
problem_soup = BeautifulSoup(problem_html.content, "html.parser")

path = "ABC147A.txt" #あらかじめ作った
s = problem_soup.prettify().replace("\xa9", "")
'''
↑実行時に
UnicodeEncodeError: 'cp932' codec can't 
encode character '\xa9' in position 21731: 
illegal multibyte sequence
が発生するので、原因箇所(\xa9)を消しちゃう
'''

with open(path, mode="w") as f:　#modeをwを指定すると書き込み可能に
    f.write(s)
