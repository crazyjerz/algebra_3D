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
        [0, e*a, 0, 0],
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
ISOMETRIC_MATRIX = np.array([
    [1/np.sqrt(6), -1/np.sqrt(6),  2/np.sqrt(6), 0],
    [1/np.sqrt(2),  1/np.sqrt(2),  0,            0],
    [-1/np.sqrt(3), 1/np.sqrt(3),  1/np.sqrt(3), 0],
    [0,            0,             0,            1]
])
TESSERACT_VERTICES = np.array([
    [-1, -1, -1, -1,  1],
    [-1, -1, -1,  1,  1],
    [-1, -1,  1, -1,  1],
    [-1, -1,  1,  1,  1],
    [-1,  1, -1, -1,  1],
    [-1,  1, -1,  1,  1],
    [-1,  1,  1, -1,  1],
    [-1,  1,  1,  1,  1],
    [ 1, -1, -1, -1,  1],
    [ 1, -1, -1,  1,  1],
    [ 1, -1,  1, -1,  1],
    [ 1, -1,  1,  1,  1],
    [ 1,  1, -1, -1,  1],
    [ 1,  1, -1,  1,  1],
    [ 1,  1,  1, -1,  1],
    [ 1,  1,  1,  1,  1]
])
TESSERACT_EDGES = np.array([
    (0, 1), (0, 2), (0, 4), (0, 8), 
    (1, 3), (1, 5), (1, 9), 
    (2, 3), (2, 6), (2, 10), 
    (3, 7), (3, 11), 
    (4, 5), (4, 6), (4, 12), 
    (5, 7), (5, 13), 
    (6, 7), (6, 14), 
    (7, 15), 
    (8, 9), (8, 10), (8, 12), 
    (9, 11), (9, 13), 
    (10, 11), (10, 14), 
    (11, 15),
    (12, 13), (12, 14),
    (13, 15),
    (14, 15)
])
TESSERACT = (TESSERACT_VERTICES, TESSERACT_EDGES)
FIVECELL_VERTICES = np.array([
    [ 1,  1,  1, -1/np.sqrt(5), 1],
    [ 1, -1, -1, -1/np.sqrt(5), 1],
    [-1,  1, -1, -1/np.sqrt(5), 1],
    [-1, -1,  1, -1/np.sqrt(5), 1],
    [ 0,  0,  0, 4/np.sqrt(5), 1]
])
FIVECELL_EDGES = np.array([
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 2), (1, 3), (1, 4),
    (2, 3), (2, 4),
    (3, 4)
])
FIVECELL = (FIVECELL_VERTICES, FIVECELL_EDGES)
RECT_PROJECTION_4D = np.array([
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1]
])
def perspective_projection_4D(d: float) -> np.array:
    return np.array([
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1/d, 1]
    ])
def direction_projection_4D(x: float, y: float, z: float, w: float) -> np.array:
    return np.array([
        [1, 0, 0, -x/w, 0],
        [0, 1, 0, -y/w, 0],
        [0, 0, 1, -z/w, 0],
        [0, 0, 0,   0,  0],
        [0, 0, 0,   0,  1]
    ])
def angle_projection_4D(phi_deg: float, psi_deg: float, w: float): # współrzędne sferyczne
    Φ = _rad(phi_deg)
    Ψ = _rad(psi_deg)
    x = np.cos(Φ) * np.cos(Ψ)
    y = np.sin(Φ) * np.cos(Ψ)
    z = np.sin(Ψ)

    return direction_projection_4D(x, y, z, w)
def rotate_xy(deg: int):
    rad = _rad(deg)
    return np.array([
        [np.cos(rad), -np.sin(rad), 0, 0, 0],
        [np.sin(rad),  np.cos(rad), 0, 0, 0],
        [0,            0,           1, 0, 0],
        [0,            0,           0, 1, 0],
        [0,            0,           0, 0, 1]
    ])
def rotate_xz(deg: int):
    rad = _rad(deg)
    return np.array([
        [np.cos(rad), 0, -np.sin(rad), 0, 0],
        [0,           1,  0,           0, 0],
        [np.sin(rad), 0,  np.cos(rad), 0, 0],
        [0,           0,  0,           1, 0],
        [0,           0,  0,           0, 1]
    ])
def rotate_xw(deg: int):
    rad = _rad(deg)
    return np.array([
        [np.cos(rad), 0, 0, -np.sin(rad), 0],
        [0,           1, 0,  0,           0],
        [0,           0, 1,  0,           0],
        [np.sin(rad), 0, 0,  np.cos(rad), 0],
        [0,           0, 0,  0,           1]
    ])
def rotate_yz(deg: int):
    rad = _rad(deg)
    return np.array([
        [1, 0,           0,            0, 0],
        [0, np.cos(rad), -np.sin(rad), 0, 0],
        [0, np.sin(rad),  np.cos(rad), 0, 0],
        [0, 0,           0,            1, 0],
        [0, 0,           0,            0, 1]
    ])
def rotate_yw(deg: int):
    rad = _rad(deg)
    return np.array([
        [1, 0, 0,           0,            0],
        [0, np.cos(rad), 0, -np.sin(rad), 0],
        [0, 0, 1,           0,            0],
        [0, np.sin(rad), 0,  np.cos(rad), 0],
        [0, 0, 0,           0,            1]
    ])
def rotate_zw(deg: int):
    rad = _rad(deg)
    return np.array([
        [1, 0, 0, 0,           0],
        [0, 1, 0, 0,           0],
        [0, 0, np.cos(rad), -np.sin(rad), 0],
        [0, 0, np.sin(rad),  np.cos(rad), 0],
        [0, 0, 0, 0,           1]
    ])