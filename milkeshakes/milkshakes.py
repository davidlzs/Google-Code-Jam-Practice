sizes =  ['sample', 'small',  'large']

def satisfied(likes, sol):
    for k in range(1, len(sol) + 1):
        for l in range(0, len(likes), 2):
            if sol[likes[l] - 1] == likes[l+1]:
                return True
    return False

def malted(likes):
    for l in range(0, len(likes), 2):
        if (likes[l+1] == 1):
            return (likes[l] - 1)
    return None

for size in sizes:

    f = open('B-%s-practice.in' % size)
    o = open('B-%s-practice.out' % size, 'w')
    n = int(f.readline())
    for i in range(0,n):
        no_flavors = int(f.readline())
        no_customers = int(f.readline())
        customer_likes = list()
        for j in range(0, no_customers):
            customer_info = f.readline().split()
            no_customer_likes = int(customer_info[0])
            l = [int(e) for e in customer_info[1:]]
            customer_likes.append(l)
        

        sol = [0] * no_flavors
        
        solved = False
        while not solved:
            for j in range(0, len(customer_likes)):
                likes = customer_likes[j]
                found = satisfied(likes, sol)
                if found:
                    continue
                if not found:
                    m = malted(likes)
                    if m is not None:
                        sol[m] = 1
                        del customer_likes[j]
                        break
                    else:
                        solved = True
                        o.write("Case #%d: %s\n" % ((i+1), "IMPOSSIBLE"))
                        break
            else:
                solved = True
                o.write("Case #%d: %s\n" % (i+ 1, " " .join(map(lambda x:  str(1 if x>0 else 0), sol))))
    f.close()
    o.close()
    

