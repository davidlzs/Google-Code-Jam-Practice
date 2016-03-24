sizes = ['small', 'large']
for size in sizes:

    f = open('A-%s-practice.in' % size)
    o = open('A-%s-practice.out' % size, 'w')
    n = int(f.readline())
    for i in range(0,n):
        credit = int(f.readline())
        items = int(f.readline())
        prices = f.readline().split()
        for j in range(0, items-1):
            for k in range(j+1, items):
                total = int(prices[j]) + int(prices[k])
                if credit == total:
                    o.write("Case #%d: %d %d\n" % (i+1, j+1, k+1))
                    break
    f.close()
    o.close()
