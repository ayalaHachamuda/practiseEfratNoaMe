import matplotlib.pyplot as mplt
import math
y=[1,10,20,15,50,30]
x=[8,10,13,15,17,20]
mplt.plot(x,y,"r")
mplt.yticks(y,["tierd","aware","hungry","satiedsfy","happy","sleeply"])
mplt.xticks(x,["8:00","10:00","13:00","15:00","17:00","20:00"])
mplt.annotate("I feel good",(17,50))
mplt.figure()
a=[5,6,10,7,2,6]
b=[2,4,6,8,10,12]
mplt.bar(b,a)
mplt.xticks(b,["milk","beard","cheese","choclate","candy","apple"])
acount=sum(a)
mplt.title(f"sum: {acount}")
mplt.show()
