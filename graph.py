from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
import numpy as np
import sys
import getopt


def main(argv):
    if(argv):
        try:
            opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
        except getopt.GetoptError:
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit(2)
        if args[0] == '12':
            draw(np.array([0.17, 0.144, 0.201, 0.389, 0.207, 0.223,
                           0.292, 0.356, 0.219, 0.3, 0.312, 0.405]))
        elif args[0] == '24':
            draw(([0.192, 0.153, 0.250, 0.418, 0.226, 0.280,
                   0.312, 0.521, 0.337, 0.352, 0.371, 0.528]))
        elif args[0] == '72':
            draw(np.array([0.245, 0.175, 0.375, 0.468, 0.287, 0.352,
                           0.401, 0.547, 0.551, 0.577, 0.536, 0.529]))
        elif args[0] == '120':
            draw(np.array([0.417, 0.19, 0.41, 0.535, 0.31,
                           0.428, 0.454, 0.672, 0.67, 0.636, 0.656, 0.788]))
        elif args[0] == '160':
            draw(np.array([0.579, 0.587, 0.584, 0.6, 0.702,
                           0.726, 0.491, 0.723, 0.727, 0.752, 0.726, 0.935]))
        elif args[0] == '384':
            draw(np.array([0.67, 0.586, 0.651, 0.715, 0.76,
                           0.816, 0.51, 0.723, 0.79, 0.782, 0.782, 0.998]))
    else:
        print 'enter -h 12, 24, 72, 120, 160'


def draw(z):
    x = np.array([32, 32, 32, 32, 64, 64, 64, 64, 96, 96, 96, 96])
    y = np.array([0.1, 0.5, 1, 3, 0.1, 0.5, 1, 3, 0.1, 0.5, 1, 3])
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    xi = np.linspace(min(x), max(x))
    yi = np.linspace(min(y), max(y))

    X, Y = np.meshgrid(xi, yi)
    Z = griddata(x, y, z, xi, yi, interp='linear')

    surf = ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap=cm.jet,
                           linewidth=1, antialiased=True)

    ax.set_zlim3d(np.min(Z), np.max(Z))
    fig.colorbar(surf)

    plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])
