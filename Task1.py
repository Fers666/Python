import sys
def itobase (nd,base) :
    nd=int(nd)
    bs = len(base)
    result = []
    res = []
    while bs >= len(base):
        result.insert(0, nd % len(base))
        bs = nd // len(base)
        nd = bs
    result.insert(0, nd % len(base))

    for i in range(len(result)):
        for j in range(len(base)):
            if result[i] == j:
                res.append(base[j])
    print(res)

def main() :
    if len(sys.argv)==3:
        nb = sys.argv[1]
        base = sys.argv[2]
        try :
            int(nb)
            itobase(nb,base)
        except ValueError :
            sys.exit('Usage')
    else :
        sys.exit('Usage')

if __name__=='__main__':
    main()
