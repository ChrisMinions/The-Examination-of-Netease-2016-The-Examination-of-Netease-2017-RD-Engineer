'''
[编程题] 奖学金
时间限制：1秒
空间限制：32768K
小v今年有n门课，每门都有考试，为了拿到奖学金，小v必须让自己的平均成绩至少为avg。
每门课由平时成绩和考试成绩组成，满分为r。现在他知道每门课的平时成绩为ai ,
若想让这门课的考试成绩多拿一分的话，小v要花bi 的时间复习，不复习的话当然就是0分。
同时我们显然可以发现复习得再多也不会拿到超过满分的分数。为了拿到奖学金，小v至少要花多少时间复习。

输入描述:
第一行三个整数n,r,avg(n大于等于1小于等于1e5，r大于等于1小于等于1e9,avg大于等于1小于等于1e6)，
接下来n行，每行两个整数ai和bi，均小于等于1e6大于等于1


输出描述:
一行输出答案。

输入例子1:
5 10 9
0 5
9 1
8 1
0 1
9 100

输出例子1:
43
'''

'''
解题思路：排序
  先把平均成绩ai和复习时间bi放入ab_i中，然后把ab_i按照bi从小到大的顺序排序
  然后1、求出所需要的总分（n*avg）  2、求出平均成绩的总和；如果平均成绩的总和已经大于了所需总分，则输出0，否则：
  按顺序访问ab_i，如果ab_i中当前科目的平均分已经到达总分，则访问下一个科目，否则的话给当前科目平均分加1，当前的总分加1，消耗时间加上该科目获取1分的复习时间。
  直至当前的总分等于目标总分后输出所耗费的时间。
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

while True:
    try:
        n, r, avg = [int(each) for each in input().split()]
        ab_i = []
        for i in range(n):
            ab_i.append([int(each) for each in input().split()])

        ab_i = sorted(ab_i, key=lambda x: x[1])

        target = n * avg
        current = sum([each[0] for each in ab_i])
        time_total = 0
        if current < target:
            index = 0
            while current < target:
                while ab_i[index][0] >= r:
                    index += 1
                time_total += ab_i[index][1]
                ab_i[index][0] += 1
                current += 1
            print(time_total)
        else:
            print(0)
    except:
        break

