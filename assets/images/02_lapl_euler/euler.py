# -*- coding: utf-8 -*-
"""
Created on Sun Sep 03 19:11:24 2017

@author: spolanski
"""
import numpy as np
import matplotlib.pyplot as plt

def euler(T_0, z_0, h):
    T_x = T_0 + h*z_0
    z_prim = 0.0
    z = z_0 + h*z_prim
    
    return T_x, z

def integrate(x_rng, T_0,T_1,z_0,h):
    """Function which invokes the Euler's method"""
    print 'The dataset T(0)=%.2f z(0)=%.2f' % (0.0, z_0)
    start, stop = x_rng
    rng = np.linspace(start, stop, int(stop/h)+1)

    results = []
    for i in rng:
        print 'x=%.2f   T(x)=%.2f   z(x)=%.2f' % (i, T_0, z_0)
        results.append([i, T_0, z_0])
        T_0, z_0 = euler(T_0, z_0, h)
    
    return results
def main():
# =============================================================================
#   Define the temperature on the boundaries
# =============================================================================
    T_0 = 30.0
    T_1 = 15.0
# =============================================================================
#   Define the step size
# =============================================================================
    h = 0.25
# =============================================================================
#   Define the range for argument x
# =============================================================================
    x_rng = [0.0, 1.0]
# =============================================================================
#   Guess new boundary condition for dataset 1 and solve ODE using Euler's 
#   method
# =============================================================================
    z_0 = 3.0
    t1 = integrate(x_rng, T_0,T_1,z_0,h)
# =============================================================================
#   Guess new boundary condition for dataset 1 and solve ODE using Euler's 
#   method
# =============================================================================
    z_1 = -2.0
    t2 = integrate(x_rng, T_0,T_1,z_1,h)
    
# =============================================================================
#   Create temporary lists to plot graph
# =============================================================================
    t1_x = [i[0] for i in t1]
    t1_y = [i[1] for i in t1]
    t2_x = [i[0] for i in t2]
    t2_y = [i[1] for i in t2]
# =============================================================================
#   Create graph from two datasets
# =============================================================================
    plt.figure(1)
    plt.plot(t1_x,t1_y, label='Dataset 1')
    plt.plot(t2_x,t2_y, label='Dataset 2')
    plt.legend(bbox_to_anchor=(0.2, -0.28, 0.58, .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.) 
    plt.grid()
    plt.xlabel('Thickness of the wall [m]')
    plt.ylabel('Temperature [C]')
    plt.title('Distribution of temperature')
    plt.show()
# =============================================================================
#   Calculate exact value of z
# =============================================================================
    z_ex = z_0 + ((z_1 - z_0)/(t2[-1][1] - t1[-1][1]))*(T_1 - t1[-1][1])
    print 'The exact value of z_ex=%.2f' % z_ex
    t1 = integrate(x_rng, T_0,T_1,-15.0,h)
    t1_x = [i[0] for i in t1]
    t1_y = [i[1] for i in t1]
# =============================================================================
#   Create the final plot    
# =============================================================================
    plt.figure(2)
    plt.plot(t1_x,t1_y)
    plt.grid()
    plt.xlabel('Thickness of the wall [m]')
    plt.ylabel('Temperature [C]')
    plt.ylim(14,31)
    plt.title('Distribution of temperature (final result)')
    plt.savefig('Temperature_euler_fin.png', format='png', dpi=800)
    plt.show()

    
if __name__ == "__main__":
    main()
