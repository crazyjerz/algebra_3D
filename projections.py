import numpy as np
import matplotlib.pyplot as plt
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
    assert V.shape[1] == R.shape[1]
    return (R @ V.T).T
def transform(V, R):
    return (_transform(V[0], R), V[1])
def _transform_project(V, R):
    return np.delete(_transform(V, R), (V.shape)[1]-2, axis=1)
def transform_project(V, R):
    return (_transform_project(V[0], R), V[1])
def _rotates(hedron):
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
def _project(hedron):
    fig = plt.figure(figsize=(11, 6))
    ax1 = fig.add_subplot(231, projection="3d")
    plot_edges(ax1, *hedron)
    ax2 = fig.add_subplot(232)
    plot_edges_2D(ax2, *transform_project(hedron, RECT_PROJECTION))
    ax3 = fig.add_subplot(233)
    plot_edges_2D(ax3, *transform_project(hedron, angle_projection(60, 2)))
    ax4 = fig.add_subplot(234)
    plot_edges_2D(ax4, *transform_project(hedron, perspective_projection(0.5)))
    ax5 = fig.add_subplot(235)
    plot_edges_2D(ax5, *transform_project(transform(hedron, translate_z(2)), ndc_projection(0, 1, 100, (16/9))))
    ax6 = fig.add_subplot(236)
    plot_edges_2D(ax6, *transform_project(hedron, ISOMETRIC_MATRIX))
    plt.tight_layout()
    plt.show()
def _tesseract(choron):
    fig = plt.figure(figsize=(12, 6))
    ax1 = fig.add_subplot(231, projection="3d")
    hedron1 = transform_project(choron, RECT_PROJECTION_4D)
    plot_edges(ax1, *hedron1)
    ax2 = fig.add_subplot(232, projection="3d")
    hedron2 = transform_project(choron, perspective_projection_4D(3))
    plot_edges(ax2, *hedron2)
    ax3 = fig.add_subplot(233, projection="3d")
    hedron3 = transform_project(choron, angle_projection_4D(45, 45, 1))
    plot_edges(ax3, *hedron3)
    ax4 = fig.add_subplot(234)
    plot_edges_2D(ax4, *transform_project(hedron1, ISOMETRIC_MATRIX))
    ax5 = fig.add_subplot(235)
    plot_edges_2D(ax5, *transform_project(hedron2, ISOMETRIC_MATRIX))
    ax6 = fig.add_subplot(236)
    plot_edges_2D(ax6, *transform_project(hedron3, ISOMETRIC_MATRIX))
    plt.tight_layout()
    plt.show()
def project():
    _project(transform(CUBE, rotation_x(45)@rotation_y(0)@rotation_z(0)))
def rotates():
    _rotates(OCTAHEDRON)
def tesseract():
    _tesseract(transform(TESSERACT, rotate_xw(0)@rotate_yw(0)@rotate_zw(0)@rotate_xy(30)@rotate_yz(0)@rotate_xz(0)))
def main():
    pass
commands = {0: main, 1: rotates, 2: project, 3: tesseract}
commands[int(argv[1])]()