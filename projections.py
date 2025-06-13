import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from constants import *
from sys import argv
def plot_edges(ax, verts, edges, color='b'):
    for i, j in edges:
        xs = [verts[i, 0]/verts[i, 3], verts[j, 0]/verts[j, 3]]
        ys = [verts[i, 1]/verts[i, 3], verts[j, 1]/verts[j, 3]]
        zs = [verts[i, 2]/verts[i, 3], verts[j, 2]/verts[j, 3]]
        ax.plot(xs, ys, zs, color=color)
def plot_edges_2D(ax, verts, edges, color='b'):
    for i, j in edges:
        xs = [verts[i, 0]/verts[i, 2], verts[j, 0]/verts[j, 2]]
        ys = [verts[i, 1]/verts[i, 2], verts[j, 1]/verts[j, 2]]
        ax.plot(xs, ys, color=color)
def _transform(V, R):
    return (R @ V.T).T
def transform(V, R):
    return (_transform(V[0], R), V[1])
def _transform_project(V, R):
    return np.delete(_transform(V, R), 2, axis=1)
def transform_project(V, R):
    return (_transform_project(V[0], R), V[1])
def _octahedra_rotates(hedron):
    fig = plt.figure(figsize=(13, 3))
    ax1 = fig.add_subplot(141, projection='3d')
    plot_edges(ax1, *hedron, color='gray')
    ax2 = fig.add_subplot(142, projection="3d")
    plot_edges(ax2, *transform(hedron, rotation_x(-45)))
    ax3 = fig.add_subplot(143, projection="3d")
    plot_edges(ax3, *transform(hedron, rotation_y(-45)))
    ax4 = fig.add_subplot(144, projection="3d")
    plot_edges(ax4, *transform(hedron, rotation_z(-45)))
    plt.tight_layout()
    plt.show()
def _octahedra_project(hedron):
    fig = plt.figure(figsize=(11, 6))
    ax1 = fig.add_subplot(231, projection="3d")
    plot_edges(ax1, *hedron)
    ax2 = fig.add_subplot(232)
    plot_edges_2D(ax2, *transform_project(hedron, RECT_PROJECTION))
    ax3 = fig.add_subplot(233)
    plot_edges_2D(ax3, *transform_project(hedron, angle_projection(30, 2)))
    ax4 = fig.add_subplot(234)
    plot_edges_2D(ax4, *transform_project(hedron, perspective_projection(1.5)))
    ax5 = fig.add_subplot(235)
    plot_edges_2D(ax5, *transform_project(transform(hedron, translate_z(2)), ndc_projection(1, 10, 180, (1/1))))
    plt.tight_layout()
    plt.show()
def octahedra_project():
    _octahedra_project((transform((transform(transform(CUBE, rotation_x(45)), rotation_y(-15))), rotation_z(30))))
def octahedra_rotates():
    _octahedra_rotates(OCTAHEDRON)
commands = {1: octahedra_rotates, 2: octahedra_project}
commands[int(argv[1])]()