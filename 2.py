l = [30, 50, 100, 180, 20, 90, 150, 70, 80, 10, 160, 120, 40, 110]


def fcfs():
    sum = abs(90 - l[0])
    print(l)
    for i in range(0, 13):
        sum += abs(l[i] - l[i + 1])
    print('平均移动磁道数 ：', sum / 14)


def sstf():
    num = 90  # 当前磁道
    result = []
    l1 = l[:]
    sum = 0

    def compare(p):
        return abs(num - p)

    while len(l1) != 0:
        l2 = sorted(l1, key=compare)
        sum += abs(num - l2[0])
        result.append(l2[0])
        l1.remove(l2[0])
        num = l2[0]
    print(result)
    print('平均移动磁道数 ：', sum / 14)


def scan():
    l1 = l[:]
    result = []
    for i in l:
        if i > 90:
            result.append(i)
            l1.remove(i)
    result.sort()
    l1.sort(reverse=True)
    result.extend(l1)
    sum = abs(result[0] - 90)
    print(result)
    for i in range(0, 13):
        sum += abs(result[i] - result[i + 1])
    print('平均移动磁道数 ：', sum / 14)


if __name__ == '__main__':
    print('请选择 ：1、先进先出算法 2、最短寻道优先算法 3、电梯调度算法')
    ipt = int(input())
    if ipt == 1:
        fcfs()
    elif ipt == 2:
        sstf()
    elif ipt == 3:
        scan()
