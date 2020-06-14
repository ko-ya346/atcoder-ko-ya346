import sys

def main():
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines

    S = readline().decode().strip()
    Q = int(readline())

    cnt = 0

    #空の文字列にqueryで追加する文字を加えていく
    ss = " "
    for _ in range(Q):
        query = list(input().split())
        if query[0] == "1":
            cnt += 1
        else:
            if (query[1] == "1" and cnt%2==0) or (query[1] == "2" and cnt%2==1):
                ss = "".join([query[2],ss])
            else:
                ss = "".join([ss,query[2]])

    #反転回数が奇数の場合、元の文字列とqueryにより作成した文字列を反転
    if cnt%2 == 1:
        S = S[::-1]
        ss = ss[::-1]

    #スペースに元の文字列を追加
    print(ss.replace(" ", S))

if __name__=="__main__":
    main()