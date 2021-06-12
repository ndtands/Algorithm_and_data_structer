#4*s_tron/s_vuong
import random 

INTERVAL = 1000
tron_point=0
vuong_point=0

for i in range(INTERVAL**2):
    rand_x = random.uniform(-1,1)
    rand_y = random.uniform(-1,1)

    dist = rand_x**2 + rand_y**2
    if dist <=1:
        tron_point+=1
    vuong_point+=1
pi = 4*tron_point/vuong_point
print(pi)