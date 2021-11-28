
import numpy as np
import math
import matplotlib.pyplot as plt

#카메라 배율 확인 후 단위 결정

Gx,Gy=1000,2828 #경로상의 좌표(카메라가 줌) #cm 단위
Ld= length = ((Gx) ** 2 + (Gy+24) ** 2) ** 0.5 # 카메라가 준 Ld값

x=abs(Gx)
y=Gy+24 #뒤축에서 카메라까지의 거리

r=(Ld**2)/(2*x)
theta=math.atan(y/x)
alpha=math.pi-(2*theta)
L=r*math.tan(alpha/2)
delta=math.atan(2*L*math.sin(alpha/2)/Ld)
degrees=math.degrees(delta)

if Gx < 0:
    driving_angle=(-1)*degrees
else:
    driving_angle=degrees

