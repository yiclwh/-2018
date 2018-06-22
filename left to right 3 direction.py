'''
给定一个矩形的长宽，用多少种方法可以从左上角走到右上角 （每一步，只能向正右、右上 或 右下走）

可以先用一个2维数组在做一个workable solution
第一题：矩阵从左上角到右下角有多少种走法
给定一个矩形的长宽，用多少种方法可以从左上角走到右上角 （每一步，只能向正右、右上 或 右下走）
Follow up 1：如果给矩形里的三个点，要求解决上述问题的同时，经过这三个点
Follow up 2：如何判断这三个点一定是合理的，即存在路径
Follow up 3：如果给你一个H，要求你的路径必须向下越过H这个界，怎么做 
Follow up 4：要经过某些特定row怎么走？要先经过一个row再经过另一个row怎么走？

感觉可以第一问用two pass DP解决。Follow up 1和2可以纵向切割矩阵，一个矩阵一个矩阵做DP。
但是Followup 3&4我就不太会了，该咋做呢~
Follow up 3：可以再做一次 dp，但是只走 <= H 的路径，再用总数减一下
Follow up 4：也是矩阵切割的思想，但是要处理先后顺序
'''
# time O(m*n) space O(n)
def totalPath(m, n):
    h = min(n, (m-1)//2 + 1)
    flat = m - h
    res = [1]
    for i in range(1, h):
        res = addPath(res, 1)
    for i in range(flat):
        res = addPath(res, 0)
    # for i in range(h-1):
    #     res = addPath(res, -1)
    return res[0]

def addPath(prev, delta):
    prev_l = len(prev)
    l = prev_l + delta
    res = []
    for i in range(l):
        temp = 0
        if 0 <= i - 1 < prev_l:
            temp += prev[i-1]
        if 0 <= i < prev_l:
            temp += prev[i]
        if 0 <= i + 1 < prev_l:
            temp += prev[i+1]
        res.append(temp)
    return res

print('m=2, n =2, expected 1 -> got {}'.format(totalPath(2,2)))
print('m=5, n =2, expected 8 -> got {}'.format(totalPath(5,2)))
print('m=5, n =10, expected 9 -> got {}'.format(totalPath(5,10)))
print('m=2, n =5, expected 1 -> got {}'.format(totalPath(2,5)))
print('m=100, n =100, expected -> 249478578991224378680142561460010030467811580 got {}'.format(totalPath(100,100)))



