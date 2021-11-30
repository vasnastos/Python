def high_complexity(array:list):
    maxval=0
    low_index=-1
    high_index=-1
    for i in range(len(array)):
        for j in range(i,len(array)):
            subsum=sum([array[x] for x in range(i,j+1)])
            if subsum>maxval:
                maxval=subsum
                low_index=i
                high_index=j
    return low_index,high_index,maxval

def prefix(array:list):
    prefixb=[0]
    for i in range(len(array)):
        prefixb.append(prefixb[i]+array[i])
    return prefixb

def complexitN_2(array:list):
    prf=prefix(array)
    maxsum=0
    high_index=-1
    low_index=-1
    for i in range(len(prf)):
        for j in range(i,len(prf)):
            sm=prf[j]-prf[i]
            if sm>maxsum:
                maxsum=sm
                low_index=i
                high_index=j-1
    return low_index,high_index,maxsum

# Kadanes
def complexityN(array:list):
    postfix=[0]
    for i in range(len(array)):
        postfix.append(max(0,postfix[i]+array[i]))
    print(postfix)
    maxs=0
    low_index=-1
    high_index=-1
    import sys
    minelem=sys.maxsize
    s=0
    for i in range(len(postfix)):
        if postfix[i]>maxs:
            maxs=postfix[i]
            high_index=i-1
            low_index=s
        if postfix[i]==0:
            s=i
    return low_index,high_index,maxs


def main():
    array=[9000,1,2000,4,-1,-7000,-10000,-500,-4000]
    print(high_complexity(array))
    print(complexityn_2(array))
    print(complexityn_3(array))


if __name__=='__main__':
    main()
