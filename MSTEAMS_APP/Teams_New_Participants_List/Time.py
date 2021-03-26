import re

dataconverter={'ώρ.':3600,'λ.':60}

def ToSeconds(formatedtime):
    data=formatedtime.split(' ')
    seconds=0
    for x in range(len(data)):
        if data[int(x)]=='ώρ.':
           seconds+=int(data[int(x)-1])*int(dataconverter['ώρ.'])
        elif data[int(x)]=='λ.':
            seconds+=int(data[int(x)-1])*int(dataconverter['λ.'])
        elif data[int(x)]=='δευτ.':
            seconds+=int(data[int(x)-1])
        else:
            continue
    return seconds

def ToTime(seconds):
    time=''
    h=int(seconds)/3600
    time+=str(h)+':'
    m=(int(seconds)%3600)/60
    time+=str(m)+':'
    s=(int(seconds)%3600)%60
    time+=str(s)
    return time   