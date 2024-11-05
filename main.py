import math
import numpy


def __main__():
    a = [1,2,3]
    print(str(x(a)))
    print(str(srotx(a)))
    print(str(y(a)))
    print(str(sroty(a)))
    print(str(z(a)))
    print(str(srotz(a)))


def srotx(a):
    return [a[0],a[2],a[1]]
def sroty(a):
    return [a[2],a[1],a[0]]
def srotz(a):
    return [a[1],a[0],a[2]]

m = math.pi/2
cos = math.cos(m)
sin = math.sin(m)
rotx = [[1,0,0],[0,cos,-sin],[0,sin,cos]]
roty = [[cos,0,sin],[0,1,0],[-sin,0,cos]]
rotz = [[cos,-sin,0],[sin,cos,0],[0,0,1]]

def mr(a,t):
    a = numpy.matmul(a,t)
    a = r(a)
    return a
def inv(a):
    return [-d for d in a]
def r(a):
    return list([round(d) for d in a])
def x(a):
    return inv(mr(a,rotx))
def y(a):
    return mr(a,roty)
def z(a):
    return inv(mr(a,rotz)) # fudge it, we rotate the wrong way I guess
def addm(a,b):
    return r([a[d]+b[d] for d in range(len(a))])
def add(a):
    # print(str(a))
    a = addm(z(addm(a, [0, -a[1], 0])), [0, a[1], 0])
    # print(str(a))
    a = x(a)
    # print(str(a))
    return a


__main__()
