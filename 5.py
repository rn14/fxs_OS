import random

ins__list = []


class Page:
    __slots__ = ('num', 'count')

    def __init__(self, num=99999, count=0):
        self.num = num
        self.count = count

    def __eq__(self, p):
        return self.num == p.num

    def __lt__(self, p):
        return self.count < p.count

    def __gt__(self, p):
        return self.count > p.count


def init():
    total = 0
    global ins__list
    while True:
        m = random.randint(1, 32766)
        ins__list.append(m)
        total += 1
        if total >= 320:
            break
        ins__list.append(m + 1)
        total += 1
        if total >= 320:
            break
        m1 = random.randint(0, m - 1)
        ins__list.append(m1)
        total += 1
        if total >= 320:
            break
        ins__list.append(m1 + 1)
        total += 1
        if total >= 320:
            break
        m2 = random.randint(m1 + 2, 32766)
        ins__list.append(m2)
        total += 1
        if total >= 320:
            break
        ins__list.append(m2 + 1)
        total += 1
        if total >= 320:
            break
    ins__list = [int(i / 1024) for i in ins__list]


def fifo(k):
    hit = 0
    page_list = [99999 for i in range(k)]
    for it in ins__list:
        if it in page_list:
            hit += 1
        else:
            page_list.pop(0)
            page_list.append(it)
    print('FIFO命中率 ：{:.2%} '.format(hit / 320), end='  ')


def lru(k):
    hit = 0
    page_list = [Page() for i in range(k)]
    for a in ins__list:
        for b in page_list:
            b.count += 1
        p = Page(a)
        if p in page_list:
            page_list[page_list.index(p)].count = 0
            hit += 1
        else:
            page_list.sort()
            page_list.pop()
            page_list.insert(0, p)
    print('LRU命中率 ：{:.2%} '.format(hit / 320), end='  ')


def opt(k):
    hit = 0
    page_list = []
    for it in ins__list:
        if it in page_list:
            hit += 1
        else:
            if len(page_list) < 29:
                page_list.append(it)
            else:
                part = ins__list[it:]
                part.pop(0)
                timeDist = []

                for tr in page_list:
                    if tr not in part:
                        n = Page(tr, 99999)
                        timeDist.append(n)
                        continue
                    i = 0
                    for fi in part:
                        if fi == tr:
                            m = Page(tr,i)
                            timeDist.append(m)
                            break
                        else:
                            i += 1
                timeDist.sort()
                page_list.remove(timeDist[-1].num)
                page_list.append(it)
    print('OPT命中率 ：{:.2%} '.format(hit / 320), end='  ')





if __name__ == '__main__':
    for k in range(1, 30):
        print(k, end='\t')
        init()
        fifo(k)
        lru(k)
        opt(k)
        ins__list = []
        print()
