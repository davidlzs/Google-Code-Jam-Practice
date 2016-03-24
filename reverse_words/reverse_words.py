sizes = ['small', 'large']
for size in sizes:

    f = open('B-%s-practice.in' % size)
    o = open('B-%s-practice.out' % size, 'w')
    n = int(f.readline())
    for i in range(0,n):
        words = f.readline().split()
        words.reverse()
        o.write("Case #%d: %s\n" % (i+1, ' '.join(words)))
    f.close()
    o.close()
