import math
x_o = 2
y_o = 3
eta = 0.01
eps = 0.000001
del_x = 1
del_y = 1
max_iters = 100
iters = 0
def deriv(x,y):
  x_deriv = 6*(x)
  y_deriv = (-5)*math.exp(-y)
  return x_deriv,y_deriv

while max(abs(del_x),abs(del_y)) > eps and iters < max_iters:
  prev_x = x_o
  prev_y = y_o
  del_x,del_y = deriv(prev_x,prev_y)
  del_x = -eta*del_x
  del_y = -eta*del_y
  x_o = x_o+del_x  
  y_o = y_o+del_y
  iters = iters+1


print("The local minimum occurs at",x_o,y_o)
