lookup =  { 'a':'2', 'b': '22', 'c':'222', 'd':'3', 'e':'33', 'f':'333', 'g':'4','h':'44', 'i':'444', 'j':'5', 'k':'55', 'l':'555', 'm':'6', 'n':'66', 'o':'666', 'p':'7', 'q':'77', 'r':'777', 's':'7777', 't':'8', 'u':'88', 'v':'888','w':'9','x':'99', 'y':'999', 'z':'9999',  ' ':'0'}

sizes = ['small', 'large']
for size in sizes:

    f = open('C-%s-practice.in' % size)
    o = open('C-%s-practice.out' % size, 'w')
    n = int(f.readline())
    for i in range(0,n):
        messages = f.readline()
        last_key = 'Z'
        o.write("Case #%d: " % (i+1))
        for j in range(0, len(messages)):
            ch = messages[j]
            if ch == '\n':
                break
            code = lookup[ch]
            key = code[-1]
            if last_key == key:
                o.write(' ')
            o.write(code)
            last_key = key
        o.write("\n")
    f.close()
    o.close()
