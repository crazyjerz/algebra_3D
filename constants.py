import numpy as np
TETRAHEDRON_VERTICES = np.array([
    [1,  1,  1, 1],
    [-1, -1,  1, 1],
    [-1,  1, -1, 1],
    [1, -1, -1, 1]
]) / np.sqrt(3)
CUBE_VERTICES = np.array([
    [-1, -1, -1, 1],
    [ 1, -1, -1, 1],
    [ 1,  1, -1, 1],
    [-1,  1, -1, 1],
    [-1, -1,  1, 1],
    [ 1, -1,  1, 1],
    [ 1,  1,  1, 1],
    [-1,  1,  1, 1]
])
OCTAHEDRON_VERTICES = np.array([
    [ 1,  0,  0, 1],
    [-1,  0,  0, 1],
    [ 0,  1,  0, 1],
    [ 0, -1,  0, 1],
    [ 0,  0,  1, 1],
    [ 0,  0, -1, 1]
])
TETRAHEDRON_EDGES = [
    (0, 1), (0, 2), (0, 3),
    (1, 2), (1, 3),
    (2, 3)
]
CUBE_EDGES = [
    (0, 1), (1, 2), (2, 3), (3, 0), 
    (4, 5), (5, 6), (6, 7), (7, 4),  
    (0, 4), (1, 5), (2, 6), (3, 7)   
]
OCTAHEDRON_EDGES = [
    (0, 2), (0, 3), (0, 4), (0, 5),
    (1, 2), (1, 3), (1, 4), (1, 5),
    (2, 4), (4, 3), (3, 5), (5, 2)
]
TETRAHEDRON = (TETRAHEDRON_VERTICES, TETRAHEDRON_EDGES)
CUBE = (CUBE_VERTICES, CUBE_EDGES)
OCTAHEDRON = (OCTAHEDRON_VERTICES, OCTAHEDRON_EDGES)
def rotation_x(deg: int) -> np.array:
    rad = deg * (180/np.pi)
    return np.array([
        [1, 0, 0, 0],
        [0, np.cos(rad), -np.sin(rad), 0],
        [0, np.sin(rad), np.cos(rad), 0],
        [0, 0, 0, 1]
    ])
def rotation_y(deg: int) -> np.array:
    rad = deg * (180/np.pi)
    return np.array([
        [np.cos(rad), 0, np.sin(rad), 0],
        [0, 1, 0, 0],
        [-np.sin(rad), 0, np.cos(rad), 0],
        [0, 0, 0, 1]
    ])
def _rad(deg: int) -> float:
    return deg * (180/np.pi)
def rotation_z(deg: int) -> np.array:
    rad = _rad(deg)
    return np.array([
        [np.cos(rad), -np.sin(rad), 0, 0],
        [np.sin(rad), np.cos(rad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
RECT_PROJECTION = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
])
def direction_projection(x: float, y: float, z: float) -> np.array:
    return np.array([
        [1, 0, -x/z, 0],
        [0, 1, -y/z, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ])
def angle_projection(deg: int, z: float) -> np.array:
    rad = _rad(deg)
    return direction_projection(np.cos(rad), np.sin(rad), z)
def perspective_projection(d: float) -> np.array:
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1/d, 1]
    ])
def ndc_projection(n: float, f: float, fov: int, a: float):
    e = 1/np.tan(_rad(fov/2))
    return np.array([
        [e, 0, 0, 0],
        [0, e/a, 0, 0],
        [0, 0, -(f+n)/(f-n), -(2*f*n)/(f-n)],
        [0, 0, -1, 0]
    ])
def translate_z(z: int):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])