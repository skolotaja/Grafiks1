import matplotlib
import matplotlib.pyplot as plt
#plt.style.use('bmh')
x_ass_koord=[2015,2016,2017,2018,2019]
y_ass_koord=[2.50,3.15,3.50,4.05,5.70]
y_ass_koord2=[7.50,8.00,8.50,8.70,9.00]
plt.xlabel("Gadi")
plt.ylabel("Cenas Eiro")
plt.axis([2014,2020,0,10])
plt.title("Cenu izmaiņas pa gadiem")
plt.bar(x_ass_koord,y_ass_koord,label="Siera cena",linewidth=3,linestyle="dotted", color='red')
plt.plot(x_ass_koord,y_ass_koord2,label="Desas cena")
plt.legend(loc="lower right")
plt.show()