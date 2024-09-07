import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Set up parameters for the figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d', facecolor='black')

# Cube vertices
vertices = np.array([[1, 1, 1], [-1, 1, 1], [-1, -1, 1], [1, -1, 1],
                     [1, 1, -1], [-1, 1, -1], [-1, -1, -1], [1, -1, -1]])

# Cube edges (in terms of the vertex indices)
edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

# Color for the cube
cube_color = 'red'

def draw_cube(ax, vertices, edge_color='red'):
    """Draw a single cube using vertices and edges."""
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color=edge_color)
    
    # Draw the edges of the cube
    for edge in edges:
        points = vertices[np.array(edge)]
        ax.plot(points[:, 0], points[:, 1], points[:, 2], color=edge_color, lw=2)
        
def rotate(vertices, angle):
    """Apply rotation to the vertices."""
    c, s = np.cos(angle), np.sin(angle)
    
    # Rotation matrix around Z-axis
    Rz = np.array([[c, -s, 0],
                   [s, c, 0],
                   [0, 0, 1]])
    
    return np.dot(vertices, Rz.T)

# Animation function
def update(frame):
    ax.cla()  # Clear the plot for each frame
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_axis_off()  # Hide axes
    
    # Rotate the vertices of the cube
    rotated_vertices = rotate(vertices, np.radians(frame))
    
    # Draw the rotated cube
    draw_cube(ax, rotated_vertices, cube_color)

# Animation parameters
frames = 120  # 5 seconds at 24 FPS
anim = FuncAnimation(fig, update, frames=frames, interval=1000/24)

# Save animation to both GIF and MP4 formats
anim.save('fractal_cube_animation.gif', writer='imagemagick', fps=24)
anim.save('fractal_cube_animation.mp4', writer='ffmpeg', fps=24)
