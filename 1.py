class Pcb(object):
    __slots__ = \
        (
            'name',
            'need_time',
            'finish_time',
            'arrive_time',
            'wait_time',
            'turn_time',
            'w_turn_time'
        )

    def __init__(self):
        self.name = []
        self.need_time = 0
        self.finish_time = 0
        self.arrive_time = 0
        self.wait_time = 0
        self.turn_time = 0
        self.w_turn_time = 0

    def __str__(self):
        return 'name : {} , arrive_time : {} , need_time : {} , finish_time : {} , turn_time : {}\n' \
            .format(self.name, self.arrive_time, self.need_time, self.finish_time, self.turn_time)

    __repr__ = __str__


pcb_list = []


def read():
    with open('work.txt', 'r') as f:
        for line in f:
            line = line.strip()
            L = line.split()
            PCB = Pcb()
            PCB.name = L[0]
            PCB.arrive_time = int(L[1])
            PCB.need_time = int(L[-1])
            pcb_list.append(PCB)


def arrive_time_compare(p):
    return p.arrive_time


def need_time_compare(p):
    return p.need_time


def response_ratio_compare(p):
    return p.wait_time / p.need_time + 1


def display(result):
    print('{:<20}{:<20}{:<20}{:<20}'.format('进程', '结束时间', '周转时间', '带权周转时间'))
    clock1 = 0
    clock2 = 0
    total_turn_time = 0
    total_weight_turn_time = 0
    for i in range(0, 10):
        if clock1 < clock2:
            if result[i].arrive_time < clock1:
                result[i].finish_time = clock1 + result[i].need_time
                result[i].turn_time = result[i].finish_time - result[i].arrive_time
                result[i].w_turn_time = result[i].turn_time / result[i].need_time
                clock1 = result[i].finish_time
                total_turn_time += result[i].turn_time
                total_weight_turn_time += result[i].w_turn_time
            else:
                result[i].finish_time = result[i].arrive_time + result[i].need_time
                result[i].turn_time = result[i].need_time
                result[i].w_turn_time = result[i].turn_time / result[i].need_time
                clock1 = result[i].finish_time
                total_turn_time += result[i].turn_time
                total_weight_turn_time += result[i].w_turn_time
        else:
            if result[i].arrive_time < clock2:
                result[i].finish_time = clock2 + result[i].need_time
                result[i].turn_time = result[i].finish_time - result[i].arrive_time
                result[i].w_turn_time = result[i].turn_time / result[i].need_time
                clock2 = result[i].finish_time
                total_turn_time += result[i].turn_time
                total_weight_turn_time += result[i].w_turn_time
            else:
                result[i].finish_time = result[i].arrive_time + result[i].need_time
                result[i].turn_time = result[i].need_time
                result[i].w_turn_time = result[i].turn_time / result[i].need_time
                clock2 = result[i].finish_time
                total_turn_time += result[i].turn_time
                total_weight_turn_time += result[i].w_turn_time
        print('{:<22}{:<22}{:<24}{:<22}'.format(result[i].name, result[i].finish_time, result[i].turn_time,
                                                result[i].w_turn_time))
    print('平均周转时间：', total_turn_time / 10)
    print('平均带权周转时间：', total_weight_turn_time / 10)


def first_go():
    result = sorted(pcb_list, key=arrive_time_compare)

    display(result)


def short_go():
    lst1 = []
    lst2 = []
    L = pcb_list[:]
    result = []

    # total_turn_time = 0
    # total_weight_turn_time = 0
    clock1 = 0
    clock2 = 0
    while len(L) != 0:
        if clock1 < clock2:
            for p in L:
                if p.arrive_time <= clock1:
                    lst1.append(p)
            if len(lst1) != 0:
                lst1.sort(key=need_time_compare)
                result.append(lst1[0])
                L.remove(lst1[0])
                clock1 += lst1[0].need_time
                lst1 = []
            else:
                l = sorted(L, key=arrive_time_compare)
                result.append(l[0])
                L.remove(l[0])
                clock1 = l[0].need_time + l[0].arrive_time
            for p in L:
                if p.arrive_time < clock2:
                    lst2.append(p)
            if len(lst2) != 0:
                lst2.sort(key=need_time_compare)
                result.append(lst2[0])
                L.remove(lst2[0])
                clock2 += lst2[0].need_time
                lst2 = []
            else:
                l = sorted(L, key=arrive_time_compare)
                result.append(l[0])
                L.remove(l[0])
                clock2 = l[0].need_time + l[0].arrive_time
        else:
            for p in L:
                if 0 < p.arrive_time <= clock2:
                    lst2.append(p)
            if len(lst2) != 0:
                lst2.sort(key=need_time_compare)
                result.append(lst2[0])
                L.remove(lst2[0])
                clock2 += lst2[0].need_time
                lst2 = []
            else:
                l = sorted(L, key=arrive_time_compare)
                result.append(l[0])
                L.remove(l[0])
                clock2 = l[0].need_time + l[0].arrive_time
            for p in L:
                if p.arrive_time < clock1:
                    lst1.append(p)
            if len(lst1) != 0:
                lst1.sort(key=need_time_compare)
                result.append(lst1[0])
                L.remove(lst1[0])
                clock1 += lst1[0].need_time
                lst1 = []
            else:
                l = sorted(L, key=arrive_time_compare)
                result.append(l[0])
                L.remove(l[0])
                clock1 = l[0].need_time + l[0].arrive_time
    display(result)


def response_ratio_go():
    lst1 = []
    lst2 = []
    L = pcb_list[:]
    result = []

    # total_turn_time = 0
    # total_weight_turn_time = 0
    clock1 = 0
    clock2 = 0
    while len(L) != 0:
        if clock1 < clock2:
            for p in L:
                if p.arrive_time <= clock1:
                    p.wait_time = clock1 - p.arrive_time
                    lst1.append(p)
            if len(lst1) != 0:
                lst1.sort(key=response_ratio_compare)
                result.append(lst1[-1])
                L.remove(lst1[-1])
                clock1 += lst1[-1].need_time
                lst1 = []
            else:
                l = sorted(L, key=arrive_time_compare)
                result.append(l[0])
                L.remove(l[0])
                clock1 = l[0].need_time + l[0].arrive_time
            for p in L:
                if p.arrive_time < clock2:
                    p.wait_time = clock2 - p.arrive_time
                    lst2.append(p)
            if len(lst2) != 0:
                lst2.sort(key=response_ratio_compare)
                result.append(lst2[-1])
                L.remove(lst2[-1])
                clock2 += lst2[-1].need_time
                lst2 = []
            else:
                l = sorted(L, key=arrive_time_compare)
                result.append(l[0])
                L.remove(l[0])
                clock2 = l[0].need_time + l[0].arrive_time
        else:
            for p in L:
                if 0 < p.arrive_time <= clock2:
                    p.wait_time = clock2 - p.arrive_time
                    lst2.append(p)
            if len(lst2) != 0:
                lst2.sort(key=response_ratio_compare)
                result.append(lst2[-1])
                L.remove(lst2[-1])
                clock2 += lst2[-1].need_time
                lst2 = []
            else:
                l = sorted(L, key=arrive_time_compare)
                result.append(l[0])
                L.remove(l[0])
                clock2 = l[0].need_time + l[0].arrive_time
            for p in L:
                if p.arrive_time < clock1:
                    p.wait_time = clock1 - p.arrive_time
                    lst1.append(p)
            if len(lst1) != 0:
                lst1.sort(key=response_ratio_compare)
                result.append(lst1[-1])
                L.remove(lst1[-1])
                clock1 += lst1[-1].need_time
                lst1 = []
            else:
                l = sorted(L, key=arrive_time_compare)
                result.append(l[0])
                L.remove(l[0])
                clock1 = l[0].need_time + l[0].arrive_time
    display(result)


if __name__ == '__main__':
    read()
    print('请选择 ：1、先进先出算法 2、短作业优先算法 3、高响应比优先算法')
    ipt = int(input())
    if ipt == 1:
        first_go()
    elif ipt == 2:
        short_go()
    elif ipt == 3:
        response_ratio_go()
