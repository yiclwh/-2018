'''
给定一个矩形的长宽，用多少种方法可以从左上角走到右上角 （每一步，只能向正右、右上 或 右下走）
'''
def totalPath(m, n):
    if not m or not n:
        return 0
    mid = m//2 + m % 2
    dp = [1]
    for i in range(1, mid):
        temp = []
        for j in range(i+1):
            temp[j] = 0
            if 0 <= j - 1 <= i:
                temp[j] += dp[j - 1]
            if 0 <= j <= i:
                temp[j] += dp[j]
            if 0 <= j + 1 <= i:
                temp[j] += dp[j + 1]
        dp = temp
    if m % 2 == 0:
        dp = dp[1:-1]
    rest = m // 2
    for i in range(rest)[::-1]:
        temp = []
        for j in range(i):
            if 0 <= j - 1 <= i + 1:
                temp[j] += dp[j - 1]
            if 0 <= j <= i + 1:
                temp[j] += dp[j]
            if 0 <= j + 1 <= i + 1:
                temp[j] += dp[j + 1]
        dp = temp
    return dp[0]



