import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D


def rossler(x, y, z, a, b, c):
    dx = - y - z
    dy = x + a*y
    dz = b + z*(x - c)
    
    return dx, dy, dz


def solver(x, y, z, t, a, b, c):
    # solve equation system 
    for i in range(len(t)-1):
        # calculate derivatives
        dx, dy, dz = rossler(x[i], y[i], z[i], a, b, c)
    
        x[i + 1] = x[i] + (dx * (t[i+1]-t[i]))
        y[i + 1] = y[i] + (dy * (t[i+1]-t[i]))
        z[i + 1] = z[i] + (dz * (t[i+1]-t[i]))
        
        
def plot_rossler(x_1, y_1, z_1, t, x_2, y_2, z_2):
    fig = plt.figure(figsize=(14, 7))    
    fig.set_facecolor('#E8E6E6')
    
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    line, = ax1.plot([], [], [], color='b', linewidth=0.5, label='$(x_1, y_1, z_1): IC = (0.1, 0., 0.1)$')
    line2, = ax1.plot3D([], [], [], color='r', linewidth=0.5, label='$(x_2, y_2, z_2): IC = (0.1001, 0., 0.1001)$')
    ax1.set_facecolor('#E8E6E6')
    ax1.xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax1.yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax1.zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax1.view_init(elev=23, azim=-131)
    
    # set limits 
    ax1.set_xlim(-10, 15)
    ax1.set_ylim(-15, 10)
    ax1.set_zlim(0, 25)
    
    # set axis labels
    ax1.set_xlabel('X', fontsize=12)
    ax1.set_ylabel('Y', fontsize=12)
    ax1.set_zlabel('Z', fontsize=12)
    
    # remove tick labels 
    ax1.set_yticklabels([])
    ax1.set_xticklabels([])
    ax1.set_zticklabels([])
    
    # legend
    ax1.legend(loc=(0.2, -0.08), fancybox=True, facecolor='white', edgecolor='black', frameon=True)
    
    # set title
    ax1.set_title('Phase Space: Trajectories', fontsize=14)
        
    # plot x_1 and x_2 values against time
    ax2 = fig.add_subplot(2, 2, 2)
    line3, = ax2.plot([], [], 'b-', linewidth=0.8)
    line4, = ax2.plot([], [], 'r-', linewidth=0.8)
    ax2.set_xlim(t[0], t[len(t)-1])
    ax2.set_ylim(-10, 12.5)
    ax2.set_ylabel('x(t)', fontsize=12)
    ax2.set_title('$Solutions: x_1 (Blue), x_2 (Red)$', fontsize=14)
    
    # plot difference (x2-x1)
    difference = x_2 - x_1
    ax3 = fig.add_subplot(2, 2, 4)
    line5, = ax3.plot([], [], 'g-', linewidth=0.8)
    ax3.set_xlim(t[0], t[len(t)-1])
    ax3.set_ylim(-8, 8)
    ax3.set_ylabel('$|x_2 - x_1|$', fontsize=12)
    ax3.set_xlabel('time (s)', fontsize=12)
    ax3.set_title('Negligible Difference', fontsize=14)
    
    plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.35)
    
    def update(i):
        i = 500*i
        line.set_data(x_1[0:i], y_1[0:i])
        line.set_3d_properties(z_1[0:i])
        
        line2.set_data(x_2[0:i], y_2[0:i])
        line2.set_3d_properties(z_2[0:i])
        
        line3.set_data(t[0:i], x_1[0:i])
        line4.set_data(t[0:i], x_2[0:i])

        line5.set_data(t[0:i], difference[0:i])
        
        return line, line2, line3, line4, line5,
    
    ani = FuncAnimation(fig, update, frames=np.size(x_1), interval=0, blit=True)
    
    plt.show()
    # plt.savefig('rossler.png', dpi = 300, facecolor=fig.get_facecolor(), edgecolor='none')
    
        
def main(): 
    # parameters
    a = 0.2
    b = 0.2
    c = 5.7
    
    # time interval and the step size
    t = np.arange(0, 300, 0.001)
    
    # vectors for the solutions
    x_1 = np.zeros((len(t)))
    y_1 = np.zeros((len(t)))
    z_1 = np.zeros((len(t)))
    
    x_2 = np.zeros((len(t)))
    y_2 = np.zeros((len(t)))
    z_2 = np.zeros((len(t)))
    
    # initial conditions
    x_1[0], y_1[0], z_1[0] = (0.1, 0., 0.1)
    x_2[0], y_2[0], z_2[0] = (0.1001, 0., 0.1001)
    
    solver(x_1, y_1, z_1, t, a, b, c)
    solver(x_2, y_2, z_2, t, a, b, c)
    
    plot_rossler(x_1, y_1, z_1, t, x_2, y_2, z_2)
  
    
if __name__ == "__main__":
    main()
