import math
def intersection(x1, x2, r1, y1, y2, r2):
    PI = 3.14
    d = math.sqrt((x2-x1)**2 + (y2 - y1)**2)
    if d >= r1 + r2:
        return 0
    if d <= abs(r1-r2):
        r = min(r1, r2)
        return int(PI*r*r)
        
    alpha = 2*math.acos((d*d+r1*r1-r2*r2)/(2*d*r1))
    beta = 2*math.acos((d*d+r2*r2-r1*r1)/(2*d*r2))
    area = (0.5*r1*r1*(alpha - math.sin(alpha))+0.5*r2*r2*(beta - math.sin(beta)))
    
    return int(area)
    
x1, y1, r1 = 0, 0, 4
x2, y2, r2 = 6, 0, 4

print("Arra of intersection is: ", intersection(x1, x2, r1, y1, y2, r2))