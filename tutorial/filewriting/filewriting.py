import random as r

def print_to_file(data):
    x=input('Give filename:')
    y=open(x,'w')
    for k in data:
        y.write(str(k)+'\n')
    y.close()
    print('file created:%s' % (x))

def print_to_csv(data):
    x=input('Give filename:')
    x+='.csv'
    y=open(x,'w')
    y.write('Code;Number\n')
    i=1
    for k in data:
        y.write(str(i)+';'+str(k)+'\n')
        i+=1
    y.close()
    print('file created:%s' % (x))

def main():
    data=[]
    size=r.randint(20,30)
    i=1
    while int(i)<=int(size):
        data.append(r.randint(1000,2000))
        i+=1
    print_to_file(data)
    print_to_csv(data)

if __name__=='__main__':
    main()