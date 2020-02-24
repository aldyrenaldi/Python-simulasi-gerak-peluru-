#import library untuk plot
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 

#inisialisasi plot

fig = plt.figure() 
ax = plt.axes(xlim=(0, 250), ylim=(0, 45)) 
line, = ax.plot([], []) 

#inisialisasi variabel

x = 0
y = 0
v = 50
deltaT = 0.01
t = 0
angleSin = 0.57
angleCos = 0.82
a = -9.8

#Kalkulasi kecepatan
vx = v * angleCos
vy = v * angleSin



#inisialisasi variabel list penyimpan jarak
X = [] #jarak horizontal
Y = [] #tinggi

#update and store
while True:
    t += deltaT
    vy = vy + (a * deltaT)
    y = y + (vy  * deltaT)
    x = x + (vx * deltaT)
    print("Waktu: ", end="")
    print(t)
    print("kecepatan y: ", end="")
    print(vy, end="")
    print(" m/s")
    print("tinggi: ", end="")
    print(y, end="")
    print(" m")
    print("jarak: ", end="")
    print(x, end="")
    print(" m")
    print("")
    X.append(x)
    Y.append(y)
    if (y <= 0):
        break

# initialization function 
def init(): 
	# creating an empty plot/frame 
	line.set_data([], []) 
	return line, 

# lists to store x and y axis points 
xdata, ydata = [], [] 

# animation function 
def animate(i): 
	# t is a parameter 
	
	
	# x, y values to be plotted 
	x = X[i] 
	y = Y[i] 
	
	# appending new points to x, y axes points list 
	xdata.append(x) 
	ydata.append(y) 
	line.set_data(xdata, ydata) 
	return line, 
	
# setting a title for the plot 
plt.title('Simulasi Gerak Peluru') 
 

# call the animator	 
anim = animation.FuncAnimation(fig, animate, init_func=init, 
							frames=1000, interval=1, blit=True)

plt.show()


    