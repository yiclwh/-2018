'''
电面两道题
merge两个list， list里面有很多key pair value, 如果两个list的element有相同的key, 就用第二个list里面的pair去替代第一个，如果第二个里面有重复的key，随便选一个，保证结果一致就可以
还有一道 里口 屋柳灵

昂赛 全是里口题
第一轮
设计微信

第二轮
BQ 刘尔易

第三轮. 
其耳妖

第四轮
酒吧 耳武期
'''
def findMostFrequent(s):
    import collections
    record = collections.defaultdict(int)
    res = ''
    count = 0
    for c in s:
        if c.isalnum():
            c = c.lower()
            record[c] += 1
            if record[c] > count:
                count = record[c]
                res = c
    return res
    
print(findMostFrequent('apple'))