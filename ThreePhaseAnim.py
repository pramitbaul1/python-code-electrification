# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
f1 = lambda x: np.sin(x)
f2 =lambda x: np.sin(x-np.pi*2/3)
f3 =lambda x: np.sin(x-np.pi*4/3)
x = np.linspace(-np.pi*9/4, np.pi*9/4, 100)
x11 = np.linspace(100, 100, 100)
V_Line=120
#x1 = np.linspace(-np.pi*9/2, np.pi*9/2, 100)

#Voltage Phase values
u_volts = f1(x)*V_Line
v_volts=f2(x)*V_Line
w_volts=f3(x)*V_Line

#Phase Color Conventions-Change as needed
u_color='orange'
v_color='green'
w_color='blue'
#Motor Impedance Values- Assuming a 
mot_resistance=2 #Ohms
mot_reactance=2 #Ohms
mot_impedance=complex(mot_resistance,mot_reactance)
mot_magnitude=np.sqrt(mot_resistance**2 + mot_reactance**2)
mot_phase=np.arctan2(mot_resistance, mot_reactance)

#Current Calculation: Voltage Divided 
u_Amps = (V_Line*f1(x-mot_phase))/mot_magnitude
v_Amps= (V_Line*f2(x-mot_phase))/mot_magnitude
w_Amps= (V_Line*f3(x-mot_phase))/mot_magnitude
I_line= V_Line/mot_magnitude
#Power Calculations
Power=u_volts*u_Amps+v_volts*v_Amps+w_volts*w_Amps
Power_mag=sum(Power)/len(Power)

# Initialize plot: Voltage, Power, And Current Plotted In that Order
fig, ax = plt.subplots(3,1)
fig.tight_layout()
ax_voltage=ax[0,]
ax_power=ax[1,]
ax_current=ax[2,]

#Voltage Axis Settings
ax_voltage.set_xticks([-np.pi*2,-np.pi*3/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, np.pi*3/2, np.pi*2])
ax_voltage.set_xticklabels((r"-$2\pi$",r"-$3\pi/2$",r"-$\pi$", r"-$\pi/2$", "0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$",r"-$2\pi$"))
ax_voltage.set_yticks([-V_Line, 0, V_Line])
ax_voltage.grid(True)
ax_voltage.set_title(r"3 Phase Voltage")
ax_voltage.set_ylim([-V_Line, V_Line])

#Power Axis Settings
ax_power.set_title(r"3 Phase Power")
ax_power.set_xticks([-np.pi*2,-np.pi*3/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, np.pi*3/2, np.pi*2])
ax_power.set_xticklabels((r"-$2\pi$",r"-$3\pi/2$",r"-$\pi$", r"-$\pi/2$", "0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$",r"-$2\pi$"))
ax_power.grid(True)
ax_power.set_yticks([Power_mag-500,Power_mag-300,Power_mag,Power_mag+300,Power_mag+500])
ax_power.set_ylim([Power_mag-500,Power_mag+500])

#Current Axis Settings
ax_current.set_title(r"3 Phase Current")
ax_current.set_xticks([-np.pi*2,-np.pi*3/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, np.pi*3/2, np.pi*2])
ax_current.set_xticklabels((r"-$2\pi$",r"-$3\pi/2$",r"-$\pi$", r"-$\pi/2$", "0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$",r"-$2\pi$"))
ax_current.grid(True)
ax_current.set_ylim([-V_Line/mot_magnitude,V_Line/mot_magnitude])
ax_current.set_yticks([-V_Line/mot_magnitude,0,V_Line/mot_magnitude])

#Set Up Plots for Voltage, Current, And Power
uVolts_plot, = ax_voltage.plot([], [],color=u_color)
vVolts_plot, = ax_voltage.plot([], [],color=v_color)
wVolts_plot, = ax_voltage.plot([], [],color=w_color)
uAmps_plot, = ax_current.plot([], [],linestyle='-.',color=u_color)
vAmps_plot, = ax_current.plot([], [],linestyle='-.',color=v_color)
wAmps_plot, = ax_current.plot([], [],linestyle='-.',color=w_color)
Power_watts, = ax_power.plot([], [])

#Marker Plots: Voltage
dot_uVolt, = ax_voltage.plot([], [], 'h', color=u_color, label="Phase U(Volts)")
dot_vVolt, = ax_voltage.plot([], [], 'D', color=v_color,label="Phase V(Volts)")
dot_wVolt, = ax_voltage.plot([], [], '^', color=w_color,label="Phase W(Volts)")


dot_power, = ax_power.plot([], [], '^',label="3 Phase Power (Watts)" )

#Marker Plots: Current
dot_uAmp, = ax_current.plot([], [], 'h',color=u_color, label="Phase U(Amps)")
dot_vAmp, = ax_current.plot([], [], 'D',color=v_color, label="Phase V(Amps)")
dot_wAmp, = ax_current.plot([], [], '^',color=w_color, label="Phase W(Amps)")
ax_voltage.legend(loc="upper right")
ax_current.legend(loc="upper right")
ax_power.legend(loc="upper right")

#Marker Plots: Current
dot_uAmp, = ax_current.plot([], [], 'h', label="Phase U(Amps)")
dot_vAmp, = ax_current.plot([], [], 'D', label="Phase V(Amps)")
dot_wAmp, = ax_current.plot([], [], '^', label="Phase W(Amps)")

def sine(i):
    #Plotting Voltage Waves Sequentially, adding a marker
    uVolts_plot.set_data(x[:i],u_volts[:i])
    dot_uVolt.set_data(x[i],u_volts[i])
    vVolts_plot.set_data(x[:i],v_volts[:i])
    dot_vVolt.set_data(x[i],v_volts[i])
    wVolts_plot.set_data(x[:i],w_volts[:i])
    dot_wVolt.set_data(x[i],w_volts[i])
    
    Power_watts.set_data(x[:i],Power[:i])
    dot_power.set_data(x[i],Power[i])
    
    #Plotting Current Waves Sequentially, adding a marker
    uAmps_plot.set_data(x[:i],u_Amps[:i])
    dot_uAmp.set_data(x[i],u_Amps[i])
    vAmps_plot.set_data(x[:i],v_Amps[:i])
    dot_vAmp.set_data(x[i],v_Amps[i])
    wAmps_plot.set_data(x[:i],w_Amps[:i])
    dot_wAmp.set_data(x[i],w_Amps[i])
    return

anim = animation.FuncAnimation(fig, sine, frames=len(x), interval=50)
anim.save('basic_animation.gif')
plt.show()

