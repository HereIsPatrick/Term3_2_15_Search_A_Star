import pprint
# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. Note that the 'v' should be
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

# Map
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

# 啟發矩陣(函數)
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']




def search(grid, init, goal, cost, heuristic):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h
    count = 0

    open = [[f, g, h, x, y]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand

    # Step 1. 搜尋
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            # Step. 排序找出g最小的，
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[3]
            y = next[4]
            g = next[1]
            expand[x][y] = count
            count +=1

            if x == goal[0] and y == goal[1]:
                # Step. 找到了
                found = True
            else:
                # Step. 從四個方向來做移動
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]

                    # Step. 確認在這個座標系統中的移動
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):

                        # Step. 確認是不是沒走過closed中會標為0，或是grid中是一個可以走的路，也是為0
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            # 算出新的g值
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            # 加到 open list中
                            open.append([f2, g2, h2, x2, y2])
                            # 標記已走過
                            closed[x2][y2] = 1
                            # 把運動方向也放進來
                            action[x2][y2] = i

    # Step 2. Show出整張矩陣的運動方向
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    x = goal[0]
    y = goal[1]
    # Step . mark the end
    policy[x][y] = '*'

    # Step. 從終點倒回來
    while x != init[0] or y != init[1]:
        # Step. 用減上一次的操作的x,y分量，就可以回到上個點
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]

        # Step. 把運動方向放進policy的表中
        policy[x2][y2] = delta_name[action[x][y]]

        # Step. 把倒回去的點，當作新的起點，從新運算
        x = x2
        y = y2

    return policy  # make sure you return the shortest path
    #return expand  # make sure you return the shortest path




pprint.pprint(search(grid,init, goal, cost, heuristic))

#print(search(grid,init, goal, cost), sep="\n")
