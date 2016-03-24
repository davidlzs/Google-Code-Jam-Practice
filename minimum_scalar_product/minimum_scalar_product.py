import functools
sizes = ['sample','small', 'large']
for size in sizes:

    f = open('A-%s-practice.in' % size)
    o = open('A-%s-practice.out' % size, 'w')
    n = int(f.readline())
    for i in range(0,n):
        no_items = f.readline()
        v1 = sorted(list( map(lambda x:int(x), f.readline().split())))
        v2 = sorted(list( map(lambda x:int(x), f.readline().split())))
        v1.reverse()
        product = functools.reduce(lambda x, y: x+y,list(map(lambda x, y: x*y, v1, v2)))
        o.write("Case #%d: %d\n" % (i+1, product))
    f.close()
    o.close()
