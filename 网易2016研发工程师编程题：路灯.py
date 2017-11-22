'''
[编程题] 路灯
时间限制：1秒
空间限制：32768K
一条长l的笔直的街道上有n个路灯，若这条街的起点为0，终点为l，第i个路灯坐标为ai ，
每盏灯可以覆盖到的最远距离为d，为了照明需求，所有灯的灯光必须覆盖整条街，但是为了省电，要是这个d最小，请找到这个最小的d。

输入描述:
每组数据第一行两个整数n和l（n大于0小于等于1000，l小于等于1000000000大于0）。
第二行有n个整数(均大于等于0小于等于l)，为每盏灯的坐标，多个路灯可以在同一点。


输出描述:
输出答案，保留两位小数。

输入例子1:
7 15
15 5 3 7 9 14 0

输出例子1:
2.50
'''

'''
解题思路：排序
  先把路灯位置放入列表lights中，然后按从小到大的顺序排序。
  计算出相邻路灯距离的一半放到列表dis中（两个路灯之间的距离可以平摊给两个路灯）。
  计算出第一个路灯和街道开始点0的距离，放入dis中
  计算出第最后一个路灯和街道末尾点l的距离，放入dis中
  输出dis中的最大值
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

while True:
    try:
        n, l = [int(each) for each in input().split()]
        street = [0]
        lights = sorted([int(each) for each in input().split()])
        dis = [(lights[i + 1] - lights[i])/2 for i in range(n - 1)]
        dis.append(lights[0] - 0)
        dis.append(l - lights[n-1])
        result = max(dis)
        print('%.2f' % result)
    except:
        break

