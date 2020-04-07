class MazeMaker:
    def longestPath(self, maze, startRow, startCol, moveRow, moveCol):
        width = len(maze[0])
        height = len(maze)
        
        #ボードの初期化
        board = [[-1 for i in range(width)] for j in range(height)]

        #スタート地点のマーク
        board[startRow][startCol] = 0

        #キューの宣言
        queueX = []
        queueY = []
        queueX.append(startCol)
        queueY.append(startRow)

        while len(queueX) > 0:
            #キューが空になるまで、一つずつ取り出す
            x = queueX.pop(0)
            y = queueY.pop(0)

            for i in range(len(moveRow)):
                nextX = x + moveCol[i]
                nextY = y + moveRow[i]
            
                if 0 <= nextX < width and 0 <= nextY < height and board[nextY][nextX] == -1 and \
                        maze[nextY][nextX] == ".":
                    #ボードに移動量を更新する
                    board[nextY][nextX] = board[y][x] +1
                    #末尾に次ぎの移動点を挿入
                    queueX.append(nextX)
                    queueY.append(nextY)
        #最大移動量の計算
        ret = 0 
        for i in range(height):
            for j in range(width):
                #移動できない点があったら-1を返す
                if maze[i][j] == "." and board[i][j] == -1:
                    return -1
                ret = max(ret, board[i][j])
        return ret

maze1 = ["X.X", "...", "XXX", "X.X"]
startRow1 = 0
startCol1 = 1
moveRow1 = [1, 0, -1, 0]
moveCol1 = [0, 1, 0, -1]

MazeMaker = MazeMaker()
print(MazeMaker.longestPath(maze1, startRow1, startCol1, moveRow1, moveCol1))