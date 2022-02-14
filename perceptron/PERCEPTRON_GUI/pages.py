import webbrowser as wb
import os
import perc
import weight_class as wc


new=2
def htmlepochboard():
    htmlval="<html><style>body{background-image:url('https://github.com/ksakkas/ksakkas.github.io/blob/master/img/bg.png?raw=true'); background-repeat:no-repeat; background-size:cover;} marquee{color:red; background-color:white; font-size:21px; direction:right;} table{color:blue; background-color:gray; font-size:15px; font-family:callibri; font-weight:bold; width:75%} th{background-color:blue; color:gray; font-size:18px;}</style><body>"
    htmlval+="<marquee><u>Perceptron Algorithm-Total Weight Changes</u></marquee><hr><br><center><table border=\"1\"><tr><th>EPOCH</th><th>WEIGHT_0</th><th>WEIGHT_1</th><th>WEIGHT_2</th><th>WEIGHT_3</th></tr>"
    for x in perc.savedata:
        if x.get_Id()<0:
            htmlval+="<tr style=\"background-color:#357a32;\"><td></td><td></td><td></td><td></td><td></td></tr>"
            continue
        htmlval+="<tr><td>"+str(x.get_Id())+"</td>"
        for j in range(0,perc.n+1):
            htmlval+="<td>"+str(x.get(j))+"</td>"
        htmlval+="</tr>"
    htmlval+="</table></center></body></html>"
    y=open("weights.html","w")
    y.write(str(htmlval))
    y.close()
    currentDir=os.getcwd()
    htmlpath=currentDir+"//weights.html"
    wb.open_new(htmlpath)