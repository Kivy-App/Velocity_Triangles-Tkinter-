from tkinter import *
import tkinter as tk
import math as m
import numpy as np
from scipy.optimize import fsolve

#k = np.empty(7)
def systemsolver(z):
    if psi.get() != '':
       psie = float(psi.get())
    else:
        psie = ''

    if phi.get() != '':
        phie = float(phi.get())
    else:
        phie = ''

    if Rn.get() != '':
        Rne = float(Rn.get())
    else:
        Rne = ''

    if a1ent.get() != '':
        av1 = float(a1ent.get())
    else:
        av1 = ''

    if a2ent.get() != '':
         av2= float(a2ent.get())
    else:
        av2 = ''

    if b1ent.get() != '':
        bv1 = float(b1ent.get())
    else:
        bv1 = ''

    if b2ent.get() != '':
        bv2 = float(b2ent.get())
    else:
        bv2 = ''



    i = 0
    if psie == '':
        psie = z[i]
        i = i + 1
    else:
        pass

    if phie == '':
        phie = z[i]
        i = i + 1
    else:
        pass

    if Rne == '':
        Rne = z[i]
        i = i + 1
    else:
        pass

    if av1 == '':
        av1 = z[i]
        i = i + 1
    else:
        pass

    if av2 == '':
        av2 = z[i]
        i = i + 1
    else:

        pass

    if bv1 == '':
        bv1 = z[i]
        i = i + 1
    else:
        pass

    if bv2 == '':
        bv2 = z[i]
        i = i + 1
    else:
        pass

    F = np.zeros((4))

    F[0] = -av1 - np.degrees(np.arctan(-((psie / 2) - 1 + Rne) / phie))
    F[1] = -av2 + np.degrees(np.arctan(((psie / 2)+1-Rne) / (phie)))
    F[2] = -bv1 + np.degrees(np.arctan(((psie / 2) + Rne) / phie))
    F[3] = -bv2 - np.degrees(np.arctan(-((psie / 2) - Rne) / phie))
    global k
    k = np.array([psie, phie, Rne, av1, av2, bv1, bv2])
    return F

def sol():
    zGuess = np.array([1, 1, 1, 1])
    z = fsolve(systemsolver,zGuess)
    print(k)

def results():
    sol()
    psie = k[0]
    phie = k[1]
    Rne = k[2]
    a1 = k[3]
    a2 = k[4]
    b1 = k[5]
    b2 = k[6]

    xtxt = 40
    xang = 90
    psitext = str(round(psie, 3))
    phitext = str(round(phie, 3))
    Rntext = str(round(Rne, 3))
    a1text = str(round(a1, 3))
    a2text = str(round(a2, 3))
    b1text = str(round(b1, 3))
    b2text = str(round(b2, 3))
    first_canvas.create_text(60, 30, font=('Purisa', 12), text=('Results'))

    first_canvas.create_text(xtxt, 60, font=('Purisa', 12), text=('ψ ='))
    first_canvas.create_text(xtxt, 80, font=('Purisa', 12), text=('φ ='))
    first_canvas.create_text(xtxt, 100, font=('Purisa', 12), text=('Rn ='))
    first_canvas.create_text(xtxt, 120, font=('Purisa', 12), text=('a1 ='))
    first_canvas.create_text(xtxt, 140, font=('Purisa', 12), text=('a2 ='))
    first_canvas.create_text(xtxt, 160, font=('Purisa', 12), text=('b1 ='))
    first_canvas.create_text(xtxt, 180, font=('Purisa', 12), text=('b2 ='))

    first_canvas.create_text(xang, 60, font=('Purisa', 12), text=(psitext))
    first_canvas.create_text(xang, 80, font=('Purisa', 12), text=(phitext))
    first_canvas.create_text(xang, 100, font=('Purisa', 12), text=(Rntext))
    first_canvas.create_text(xang, 120, font=('Purisa', 12), text=(a1text))
    first_canvas.create_text(xang, 140, font=('Purisa', 12), text=(a2text))
    first_canvas.create_text(xang, 160, font=('Purisa', 12), text=(b1text))
    first_canvas.create_text(xang, 180, font=('Purisa', 12), text=(b2text))

def turbine():
    try:
        psie = float(psi.get())
        phie = float(phi.get())
        Rne = float(Rn.get())
        # av1 = float(a1ent.get())
        # av2 = float(a2ent.get())
        # bv1 = float(b1ent.get())
        # bv2 = float(b2ent.get())

        a2 = m.degrees(np.arctan(((psie / 2)+1-Rne) / (phie)))
        a1 = -m.degrees(np.arctan(-((psie / 2) - 1 + Rne) / phie))
        b2 = -m.degrees(np.arctan(-((psie / 2) - Rne) / phie))
        b1 = m.degrees(np.arctan(((psie / 2) + Rne) / phie))


        # tk.Label(my_window, text="a1=").grid(row=0, column=3)
        # tk.Label(my_window, text="a2=").grid(row=1, column=3)
        # tk.Label(my_window, text="b1=").grid(row=2, column=3)
        # tk.Label(my_window, text="b2=").grid(row=3, column=3)


        # tk.Label(my_window, text=str(round(a1,3))).grid(row=0, column=4)
        # tk.Label(my_window, text=str(round(a2,3))).grid(row=1, column=4)
        # tk.Label(my_window, text=str(round(b1,3))).grid(row=2, column=4)
        # tk.Label(my_window, text=str(round(b2,3))).grid(row=3, column=4)
        xtxt = 40
        xang = 90
        a1text = str(round(a1, 3))
        a2text = str(round(a2, 3))
        b1text = str(round(b1, 3))
        b2text = str(round(b2, 3))
        first_canvas.create_text(60, 30, font=('Purisa', 12), text=('Angles'))
        first_canvas.create_text(xtxt, 60, font=('Purisa', 12), text=('a1 ='))
        first_canvas.create_text(xtxt, 80, font=('Purisa', 12), text=('a2 ='))
        first_canvas.create_text(xtxt, 100, font=('Purisa', 12), text=('b1 ='))
        first_canvas.create_text(xtxt, 120, font=('Purisa', 12), text=('b2 ='))

        first_canvas.create_text(xang, 60, font=('Purisa', 12), text=(a1text))
        first_canvas.create_text(xang, 80, font=('Purisa', 12), text=(a2text))
        first_canvas.create_text(xang, 100, font=('Purisa', 12), text=(b1text))
        first_canvas.create_text(xang, 120, font=('Purisa', 12), text=(b2text))

    except:
        tk.Label(my_window, text='Angles not found',fg = 'red').grid(row=8, column=0)

#Function of creating a new window with triangles
def create_window():
    sol()
    try:
       psie = k[0]
       phie = k[1]
       Rne = k[2]
       a1 = k[3]
       a2 = k[4]
       b1= k[5]
       b2= k[6]
       # a2 = m.degrees(np.arctan(((psie / 2) + 1 - Rne) / (phie)))
       # a1 = -m.degrees(np.arctan(-((psie / 2) - 1 + Rne) / phie))
       # b2 = -m.degrees(np.arctan(-((psie / 2) - Rne) / phie))
       # b1 = m.degrees(np.arctan(((psie / 2) + Rne) / phie))

       new_window = tk.Tk()
       new_window.geometry('1000x1000')
       #Creating the new canvas
       my_canvas = Canvas(new_window, width=900, height=900)
       my_canvas.grid(row=1, column=1)

       #Arrows
       x0,y0 = 300,600
       x1,y1 = 600,600
       U = x1-x0
       xL,yL = x0-np.tan(m.radians(a1))*phie*U,y0-phie*U
       xR,yR = xL+psie*U,yL

       #Main Lines
       my_canvas.create_line(x0, y0, x1, y1, fill='black', arrow='first',arrowshape = (18, 25, 4)) #U
       my_canvas.create_line(x0, y0, xL, yL, fill='black', arrow='first',arrowshape = (18, 25, 4)) #V1
       my_canvas.create_line(x1, y1, xL, yL, fill='black', arrow='first',arrowshape = (18, 25, 4)) #W1
       my_canvas.create_line(x0, y0, xR, yR, fill='black', arrow='first',arrowshape = (18, 25, 4)) #V2
       my_canvas.create_line(x1, y1, xR, yR, fill='black', arrow='first',arrowshape = (18, 25, 4)) #W2
       #Meassurements
       my_canvas.create_line(x0, y0+40, x1, y1+40, fill='black', arrow='both',arrowshape = (13,20,4))     #U messurement
       my_canvas.create_line(xL, yL - 40, xR, yR - 40, fill='black', arrow='both',arrowshape = (13,20,4)) #ΔVθ
       if xL<x0 : # Vx
         my_canvas.create_line(xL-40, y0 , xL-40, yL , fill='black', arrow='first',arrowshape = (13,20,4))
         #Dash Lines Vx
         my_canvas.create_line(xL, yL, xL-60, yL , fill='black', dash=(8, 2))
         my_canvas.create_line(x0, y0, xL-60, y0 , fill='black', dash=(8, 2))
         #Text Vx
         my_canvas.create_text(xL - 55, y0 - phie*U/2,font=('Purisa',15), text=('Vx'))
       else :
         my_canvas.create_line(x0 - 40, y0, x0 - 40, yL, fill='black', arrow='first',arrowshape = (13,20,4))
         # Dash Lines Vx
         my_canvas.create_line(x0, y0, x0 - 60, y0, fill='black', dash=(8, 2))
         my_canvas.create_line(xL, yL, x0 - 60, yL, fill='black', dash=(8, 2))
         # Text Vx
         my_canvas.create_text(x0 - 55, y0 - phie * U / 2,font=('Purisa',15), text=('Vx'))
       #Dash lines
       my_canvas.create_line(xL, yL, xL, yL - 60, fill='black', dash=(8, 2))
       my_canvas.create_line(xR, yR, xR, yR - 60, fill='black', dash=(8, 2))
       my_canvas.create_line(x0, y0, x0, y0 + 60, fill='black', dash=(8, 2))
       my_canvas.create_line(x1, y1, x1, y1 + 60, fill='black', dash=(8, 2))
       my_canvas.create_line(xL, yL, xR, yR, fill='black', dash=( 1, 2))
       #Text
       my_canvas.create_text(x0 + 150,y0 + 55,font=('Purisa',15),text=('U'))
       my_canvas.create_text(xL + psie*U/2, yL - 55,font=('Purisa',15), text=('ΔVθ'))

       xtxt = 40
       xang = 90
       a1text = str(round(a1, 3))
       a2text = str(round(a2, 3))
       b1text = str(round(b1, 3))
       b2text = str(round(b2, 3))
       my_canvas.create_text(60, 30, font=('Purisa', 12), text=('Angles'))
       my_canvas.create_text(xtxt, 60, font=('Purisa', 12), text=('a1 ='))
       my_canvas.create_text(xtxt, 80, font=('Purisa', 12), text=('a2 ='))
       my_canvas.create_text(xtxt, 100, font=('Purisa', 12), text=('b1 ='))
       my_canvas.create_text(xtxt, 120, font=('Purisa', 12), text=('b2 ='))

       my_canvas.create_text(xang, 60, font=('Purisa', 12), text=(a1text))
       my_canvas.create_text(xang, 80, font=('Purisa', 12), text=(a2text))
       my_canvas.create_text(xang, 100, font=('Purisa', 12), text=(b1text))
       my_canvas.create_text(xang, 120, font=('Purisa', 12), text=(b2text))
    except:
        tk.Label(my_window, text='Triangles not found', fg='red').grid(row=8, column=1)

#Function of creating the diamensional units
def dml_measurements():
    sol()
    try:
        #getting input variables (N,rt/rh,D)
        w = 0.01666666*float(N.get())
        rhtg = float(rht.get())
        Dg = float(D.get())
        deng = float(den.get())

        psie = k[0]
        phie = k[1]
        Rne = k[2]
        a1 = k[3]
        a2 = k[4]
        b1 = k[5]
        b2 = k[6]

        #calculations
        rm = (rhtg+1)*(Dg/4)
        rt = Dg/2
        rh = rhtg*rt
        Um = w*rm
        Ut = w*rt
        Uh = w*rh
        Vx = phie*Um
        v1 = Vx/m.cos(a1)
        v2 = Vx/m.cos(a2)
        w1 = Vx/m.cos(b1)
        w2 = Vx/m.cos(b2)
        A = m.pi*(rt**2) - m.pi*(rh**2)
        mdot = deng*A*(Vx**2)

        xtxt = 40
        xang = 90
        second_canvas.create_text(90, 30, font=('Purisa', 12), text=('Measurements'))
        second_canvas.create_text(xtxt, 60, font=('Purisa', 12), text=('rm ='))
        second_canvas.create_text(xtxt, 80, font=('Purisa', 12), text=('rh ='))
        second_canvas.create_text(xtxt, 100, font=('Purisa', 12), text=('rt ='))
        second_canvas.create_text(xtxt, 120, font=('Purisa', 12), text=('Um ='))
        second_canvas.create_text(xtxt, 140, font=('Purisa', 12), text=('Uh ='))
        second_canvas.create_text(xtxt, 160, font=('Purisa', 12), text=('Ut ='))
        second_canvas.create_text(xtxt, 180, font=('Purisa', 12), text=('Vx ='))
        second_canvas.create_text(xtxt, 200, font=('Purisa', 12), text=('V1 ='))
        second_canvas.create_text(xtxt, 220, font=('Purisa', 12), text=('V2 ='))
        second_canvas.create_text(xtxt, 240, font=('Purisa', 12), text=('W1 ='))
        second_canvas.create_text(xtxt, 260, font=('Purisa', 12), text=('W2 ='))
        second_canvas.create_text(xtxt, 280, font=('Purisa', 12), text=('A ='))
        second_canvas.create_text(xtxt, 300, font=('Purisa', 12), text=('mdot ='))

        rm_text = str(round(rm, 3))
        rh_text = str(round(rh, 3))
        rt_text = str(round(rt, 3))
        Um_text = str(round(Um, 3))
        Uh_text = str(round(Uh, 3))
        Ut_text = str(round(Ut, 3))
        Vx_text = str(round(Vx, 3))
        V1_text = str(round(v1, 3))
        V2_text = str(round(v2, 3))
        W1_text = str(round(w1, 3))
        W2_text = str(round(w2, 3))
        A_text = str(round(A, 3))
        mdot_text = str(round(mdot, 2))


        second_canvas.create_text(xang, 60, font=('Purisa', 12), text=(rm_text ))
        second_canvas.create_text(xang, 80, font=('Purisa', 12), text=(rh_text ))
        second_canvas.create_text(xang, 100, font=('Purisa', 12), text=(rt_text ))
        second_canvas.create_text(xang, 120, font=('Purisa', 12), text=(Um_text ))
        second_canvas.create_text(xang, 140, font=('Purisa', 12), text=(Uh_text ))
        second_canvas.create_text(xang, 160, font=('Purisa', 12), text=(Ut_text ))
        second_canvas.create_text(xang, 180, font=('Purisa', 12), text=(Vx_text ))
        second_canvas.create_text(xang, 200, font=('Purisa', 12), text=(V1_text ))
        second_canvas.create_text(xang, 220, font=('Purisa', 12), text=(V2_text ))
        second_canvas.create_text(xang, 240, font=('Purisa', 12), text=(W1_text ))
        second_canvas.create_text(xang, 260, font=('Purisa', 12), text=(W2_text ))
        second_canvas.create_text(xang, 280, font=('Purisa', 12), text=(A_text))
        second_canvas.create_text(xtxt+70, 300, font=('Purisa', 12), text=(mdot_text))
    except:
        tk.Label(my_window, text='Not enough inputs', fg='red').grid(row=14, column=0)


#Loop function of creating the main window
my_window = tk.Tk()
my_window.title('Velocity triangles')
my_window.geometry('400x700')
first_canvas = Canvas(my_window,width=150,height=340)
first_canvas.grid(row= 25,column=1, columnspan = 2, sticky = W)

second_canvas = Canvas(my_window,width=150,height=340)
second_canvas.grid(row= 25,column=0, columnspan = 2, sticky = W)

#psi,phi,Rn labels
tk.Label(my_window, text="Load ratio ψ").grid(row=0,column=0, sticky = W)
tk.Label(my_window, text="Flow ratio φ").grid(row=1,column = 0, sticky = W)
tk.Label(my_window, text="Resistance ratio Rn").grid(row=2,column = 0, sticky = W)
tk.Label(my_window, text="Entry angle of stator a1=a3").grid(row=3,column = 0, sticky = W)
tk.Label(my_window, text="Exit angle of stator a2").grid(row=4,column = 0, sticky = W)
tk.Label(my_window, text="Entry angle of rotor b1=b3").grid(row=5,column = 0, sticky = W)
tk.Label(my_window, text="Exit angle of rotor b2").grid(row=6,column = 0, sticky = W)

#diamensional size labels
tk.Label(my_window, text="").grid(row=8,column=0)
tk.Label(my_window, text="Revolution per minutes [N]").grid(row=9,column=0,sticky = W)
tk.Label(my_window, text="Diamater  [D]").grid(row=10,column=0,sticky = W)
tk.Label(my_window, text="Hub to tip ratio [rh/rt]").grid(row=11,column=0,sticky = W)
tk.Label(my_window, text="Fluid density [ρ]").grid(row=12,column=0,sticky = W)

#meassurement units
tk.Label(my_window, text="[rpm]").grid(row=9,column=2,sticky = W)
tk.Label(my_window, text="[m]").grid(row=10,column=2,sticky = W)
tk.Label(my_window, text="-").grid(row=11,column=2,sticky = W)
tk.Label(my_window, text="[kg/m^3]").grid(row=12,column=2,sticky = W)

tk.Label(my_window, text="-").grid(row=0,column=2,sticky = W)
tk.Label(my_window, text="-").grid(row=1,column = 2,sticky = W)
tk.Label(my_window, text="-").grid(row=2,column = 2,sticky = W)
tk.Label(my_window, text="deg").grid(row=3,column = 2,sticky = W)
tk.Label(my_window, text="deg").grid(row=4,column = 2,sticky = W)
tk.Label(my_window, text="deg").grid(row=5,column = 2,sticky = W)
tk.Label(my_window, text="deg").grid(row=6,column = 2,sticky = W)

# SLOTS
#slots of psi,phi,Rn
psi = tk.Entry(my_window)
phi = tk.Entry(my_window)
Rn = tk.Entry(my_window)
a1ent = tk.Entry(my_window)
a2ent = tk.Entry(my_window)
b1ent = tk.Entry(my_window)
b2ent = tk.Entry(my_window)
psi.grid(row=0, column=1)
phi.grid(row=1, column=1)
Rn.grid(row=2, column=1)
a1ent.grid(row=3, column=1)
a2ent.grid(row=4, column=1)
b1ent.grid(row=5, column=1)
b2ent.grid(row=6, column=1)

#slots for dimensional sizes
N = tk.Entry(my_window)
D = tk.Entry(my_window)
rht = tk.Entry(my_window)
den = tk.Entry(my_window)
N.grid(row=9, column=1)
D.grid(row=10, column=1)
rht.grid(row=11, column=1)
den.grid(row=12, column=1)

#Buttons
# tk.Button(my_window, text='Show angles',fg = 'blue', command=turbine).grid(row=7, column=0, sticky = W+E)
tk.Button(my_window, text='       System solver       ', fg = 'blue', command= results).grid(row=7, column=0, sticky = W+E)
tk.Button(my_window, text='    Velocity triangles    ', command=create_window).grid(row=7, column=1)
tk.Button(my_window, text='Show measurements',fg = 'blue', command=dml_measurements).grid(row=13, column=0, sticky = W+E)
my_window.mainloop()
#End of loop





