# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:17:59 2018

@author: tetsuomiyoshi
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import tkinter as tk

def plot():
    #x = np.arange(0, 3 * np.pi, 0.1)
    #y = np.sin(x)
    #plt.title("sine wave form")
    #plt.plot(x, y)
    #plt.show()
    value = v.get()
    if value > 1:
        value1 = value - 1
    elif value == 1:
        value1 = 3
    elif value == 0:
        value1=4
    value2 = vv.get()

    def circle(a, b, r):
        # 点(a,b)を中心とする半径rの円
        T = 100
        x, y = [0]*T, [0]*T
        for i,theta in enumerate(np.linspace(0,2*np.pi,T)):
            x[i] = a + r*np.cos(theta)
            y[i] = b + r*np.sin(theta)
        return x, y

    R = 1

    def plt_show():
        try:
            plt.show()
        except UnicodeDecodeError:
            plt_show()
            
    def gen():
        if value == 4:
            n=6
        elif value == 3:
            n=4
        else:
            n=2
        #for theta in np.linspace(0,n*np.pi,100):
        for theta in np.linspace(0, n * np.pi, 200):
            if value > 1:
                yield (value1+1)*R*np.cos(theta), (value1+1)*R*np.sin(theta), ((value1+1)/value1)*theta
            else:
                yield value1*R*np.cos(theta), value1*R*np.sin(theta), value1*theta

    fig = plt.figure()
    plt.axes().set_aspect('equal', 'datalim')
    ax = fig.add_subplot(111)
    if value==4:
        ax.set_ylim(-10, 10)
        ax.set_xlim(-10, 10)
    elif value==3 or value==1 or value==0:
        ax.set_ylim(-7, 7)
        ax.set_xlim(-7, 7)
    else:
        ax.set_ylim(-5, 5)
        ax.set_xlim(-5, 5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid()
    time_text1 = ax.text(0.05, 0.9, '', transform=ax.transAxes)
    time_text2 = ax.text(0.05, 0.8, '', transform=ax.transAxes)

    cycloid, = ax.plot([], [], 'r-', lw=2)
    line, = ax.plot([], [], 'y-', lw=2)
    f_circle_line, = ax.plot([], [], 'b', lw=2)
    circle_line, = ax.plot([], [], 'g', lw=2)
    point, = ax.plot([], [], 'bo', ms=4)

    xx, yy = [], []
    def func(data):
        x, y, Rt = data
        time_text1.set_text('theta = %.2f pi' % (Rt/np.pi))
        time_text2.set_text('%d times' % int(Rt/(2*np.pi)))
        #
        if value > 1:
            fcx, fcy = circle(0, 0, R)
            xx.append(x - value1 * np.cos(Rt))
            yy.append(y - value1 * np.sin(Rt))
            cx, cy = circle(x, y, value1*R)
            line.set_data((x, x - value1 * np.cos(Rt)), (y, y - value1 * np.sin(Rt)))
            point.set_data(x - value1 * np.cos(Rt), y - value1 * np.sin(Rt))
        else:
            fcx, fcy = circle(0, 0, (value1-1)*R)
            xx.append(x-np.cos(Rt))
            yy.append(y-np.sin(Rt))
            cx, cy = circle(x, y, R)
            line.set_data((x,x-np.cos(Rt)), (y,y-np.sin(Rt)))
            point.set_data(x-np.cos(Rt), y-np.sin(Rt))
        f_circle_line.set_data(fcx, fcy)
        cycloid.set_data(xx, yy)
        circle_line.set_data(cx, cy)

    ani = animation.FuncAnimation(fig, func, gen, blit=False, interval=value2, repeat=False)

    #ani.save("cycloid.mp4")
    plt_show()

root = tk.Tk()
root.title('外サイクロイド')

v = tk.IntVar()
v.set(2)

f0 = tk.LabelFrame(root, text = 'Rc=1')
#f1 = tk.LabelFrame(root, text = 'Group2')
for x in (0, 1, 2, 3, 4):
    if x > 1:
        tk.Radiobutton(f0, text = 'Rm = %d' % (x-1), value = x, variable = v).pack()
    elif x==1:
        tk.Radiobutton(f0, text='Rm = 1/%d' % (x+1), value=x, variable=v).pack()
    else:
        tk.Radiobutton(f0, text='Rm = 1/%d' % (x + 3), value=x, variable=v).pack()
    #tk.Checkbutton(f1, text = 'checkbutton %d' % x).pack()
f0.pack(padx = 5, pady = 5, side = tk.LEFT)

vv = tk.IntVar()
vv.set(50)
s1 = tk.Scale(root, label = 'speed', orient = 'h', from_ = 10, to = 100, variable = vv)
# ウィジェットの配置
s1.pack()

b = tk.Button(root, text="Plot", padx=10, pady=10, command=plot)
b.pack()
c = tk.Button(root, text="Exit", padx=20, pady=10, command=exit)
c.pack()

root.mainloop()