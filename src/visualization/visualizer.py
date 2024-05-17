import plotly.graph_objs as go
import numpy as np

class PendulumVisualizer:
    def __init__(self):
        self.fig = go.Figure()

    def update(self, state):
        x1, y1, z1, x2, y2, z2 = self.get_pendulum_positions(state)
        self.fig.data = []  # Clear previous data

        # Add pendulum rods
        self.fig.add_trace(go.Scatter3d(
            x=[0, x1, x2],
            y=[0, y1, y2],
            z=[0, z1, z2],
            mode='lines+markers',
            marker=dict(size=[10, 10, 10], color=['black', 'blue', 'red']),
            line=dict(color='black', width=5)
        ))

        self.fig.show()

    def get_pendulum_positions(self, state):
        # Calculate the 3D positions of the pendulum segments based on the state
        # Placeholder calculations
        x1, y1, z1 = state[0], state[1], state[2]
        x2, y2, z2 = state[3], state[4], state[5]
        return x1, y1, z1, x2, y2, z2

    def animate(self, trajectory):
        for state in trajectory:
            self.update(state)

# Example usage
if __name__ == "__main__":
    visualizer = PendulumVisualizer()
    trajectory = np.random.rand(100, 6)  # Placeholder for actual trajectory data
    visualizer.animate(trajectory)
