import numpy as np
from typing import NamedTuple


def write_output(filename, answer):
    
    with open('output_' + filename, 'w') as file:
        file.write(str(answer[0]) + ' ' + str(answer[1]))

def distance(p1,p2):
    assert len(p1) == 2
    assert len(p2) == 2
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def get_closest_pair(P):
    
    if len(P) <= 3 : 
    	return brute_force(P)
    X = np.array(sorted(P,key = lambda x : x[1]))
    Y = np.array(sorted(P,key = lambda x : x[2]))
    return compute_closest_points(P,X,Y)


def compute_closest_points(P, X, Y):
    
    if len(P) <= 3 : return brute_force(X)
    compare_y = lambda x : x[2]
    middle_index = int(len(X)/2)
    middle_x = X[middle_index][1]

    left_points = X[:middle_index].copy()
    left_points_y = np.array(sorted(left_points,key=compare_y))

    right_points = X[middle_index:].copy()
    right_points_y = np.array(sorted(right_points,key=compare_y))


    p1_l,p2_l,dleft = compute_closest_points(left_points,left_points,left_points_y)

  
    p1_r,p2_r,dright = compute_closest_points(right_points,right_points,right_points_y)

    if dleft < dright: p1,p2,d = p1_l,p2_l,dleft
    else: p1,p2,d = p1_r,p2_r,dright

    vpxyb = []
    for i in range(len(Y)):
        px = Y[i]
        if abs(px[1] - middle_x) <= d:
            vpxyb.append(p)
    vpxyb = np.array(vpxyb)
    for i in range(len(vpxyb)):
        pi = vpxyb[i]
        count = 0
        for j in range(i + 1,len(vpxyb)):
            pj = vpxyb[j]
            if count >= 7:break
            if (pi[1] - middle_x)*(pj[1] - middle_x) > 0:continue
            count += 1
            real_d = distance(pi[1:],pj[1:])
            if real_d <= d :
                p1 = pi[0]
                p2 = pj[0]
                d  = real_d
    return p1,p2,d


def brute_force(X):
   
   
    assert len(X) <= 3
    assert len(X[0]) == 3
    if len(X) == 2:
        return X[0][0],X[1][0],distance(X[0,1:],X[1,1:])
    Y = np.array(sorted(X,key = lambda x : x[2]))
    dsxyb = []
    if len(X) == 3:
        dsxyb.append((Y[0][0],Y[1][0],distance(Y[0,1:],Y[1,1:])))
        dsxyb.append((Y[0][0],Y[2][0],distance(Y[0,1:],Y[2,1:])))
        dsxyb.append((Y[1][0],Y[2][0],distance(Y[1,1:],Y[2,1:])))
        return sorted(dsxyb,key=lambda d : d[2],reverse = False)[0]

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    #filename = "Input2.dat"
    P = np.genfromtxt(filename)
    import time
    start_time = time.process_time()
    pt1, pt2, delta = get_closest_pair(P)
    end_time = time.process_time()

    print("time taken: {}".format(end_time - start_time))
    write_output(filename, [int(pt1), int(pt2)])
    ds = []
    for i in range(len(P)):
        for j in range(i+1,len(P)):
            pi = P[i]
            pj = P[j]
            ds.append((pi[0], pj[0], distance(pi[1:], pj[1:])))
    print(list(sorted(ds, key=lambda d: d[2], reverse=False)))
