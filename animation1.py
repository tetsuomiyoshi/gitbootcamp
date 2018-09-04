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
        for theta in np.linspace(0,2*np.pi,100):
            yield R*(theta-np.sin(theta)), R*(1-np.cos(theta)), R*theta

    fig = plt.figure()
    plt.axes().set_aspect('equal', 'datalim')
    ax = fig.add_subplot(111)
    ax.set_ylim(-5, 5)
    ax.set_xlim(-2, 8)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid()
    time_text1 = ax.text(0.05, 0.9, '', transform=ax.transAxes)
    time_text2 = ax.text(0.05, 0.8, '', transform=ax.transAxes)

    cycloid, = ax.plot([], [], 'r-', lw=2)
    line, = ax.plot([], [], 'y-', lw=2)
    circle_line, = ax.plot([], [], 'g', lw=2)
    point, = ax.plot([], [], 'bo', ms=4)

    xx, yy = [], []
    def func(data):
        x, y, Rt = data
        time_text1.set_text('theta = %.2f pi' % (Rt/np.pi))
        time_text2.set_text('%d times' % int(Rt / (2 * np.pi)))
        xx.append(x)
        yy.append(y)
        cx, cy = circle(Rt, R, R)

        cycloid.set_data(xx, yy)
        line.set_data((x,Rt), (y,R))
        circle_line.set_data(cx, cy)
        point.set_data(x, y)

    ani = animation.FuncAnimation(fig, func, gen, blit=False, interval=value, repeat=False)

    #ani.save("cycloid.mp4")
    plt_show()

root = tk.Tk()
root.title('サイクロイド')
root.geometry("150x150")

v = tk.IntVar()
v.set(50)
s1 = tk.Scale(root, label = 'speed', orient = 'h', from_ = 10, to = 100, variable = v)
# ウィジェットの配置
s1.pack()

b = tk.Button(root, text="Plot", padx=10, pady=10, command=plot)
b.pack()
c = tk.Button(root, text="Exit", padx=20, pady=10, command=exit)
c.pack()

root.mainloop()