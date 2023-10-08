clc 
clear all
deltaT=0.1;                                % Timestep 
Rint=0.1;                                  % Internal resistance
Irms=100;                                  % RMS drive cycle current draw
T=0:0.1:5000;                               % Time vector
Cthermal=476;                              %Battery Thermal Capacity(kJ/C)
Tin=23;                                    % Initial battery temperature
                                     % Final battery temperature
for(i=1:1:50001)
    if(i==1)
        Qgen(i)=Irms^2*Rint ;                       %Power (W)
        Egen(i)=Qgen(i)*deltaT;                     %Energy (J)
    else
        Qgen(i)=Irms^2*Rint;                      %Power(W)
        Egen(i)=(Qgen(i)*deltaT+Egen(i-1));       % Energy (J) Heat generated at current timestep plus previous value
    end
end
Tf=(Egen/(Cthermal*1000))+Tin;                      %Egen is in joules, Cthermal in kilojoules
set(figure,'Color','White','WindowStyle','docked')


plot(T,Qgen/1000)                                   % Power loss (kW)
xlabel('Time(s)')
ylabel('Power Loss(kW)')

set(figure,'Color','White','WindowStyle','docked')

plot(T,Egen/(3600*1000));                           %  Heat generated (kWh)
xlabel('Time(s)')
ylabel('Heat Generated (kWh)')

set(figure,'Color','White','WindowStyle','docked')

plot(T/60,Tf);                                         
xlabel('Time(mins)')
ylabel('Final Temperature (Celsius)')


%Egen=Cthermal*(Tf-Tin);

