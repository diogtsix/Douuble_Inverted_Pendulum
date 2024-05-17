# main.py

import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from models.pendulum import DoubleInvertedPendulum
from visualization.visualizer import PendulumVisualizer
from controllers.mpc import MPCController
import numpy as np

def main():
    # Parameters for the pendulum
    m1, m2 = 1.0, 1.0
    l1, l2 = 1.0, 1.0
    pendulum = DoubleInvertedPendulum(m1, m2, l1, l2)
    
    # Initial state: [x, x_dot, theta1, theta1_dot, theta2, theta2_dot]
    initial_state = [0, 0, np.pi/4, 0, np.pi/4, 0]
    t = np.linspace(0, 10, 1000)  # 10 seconds, 1000 time steps

    # Simulate the pendulum without control for now
    trajectory = pendulum.simulate(initial_state, t)
    
    # Visualize the trajectory
    visualizer = PendulumVisualizer()
    visualizer.animate(trajectory)
    
    # Implement MPC control
    mpc = MPCController(pendulum, prediction_horizon=10)
    current_state = initial_state
    for ti in t:
        control_input = mpc.control_law(current_state)
        # Apply control input to update the state (placeholder)
        current_state = np.zeros_like(current_state)  # Update with new state
        
        visualizer.update(current_state)  # Update visualization

if __name__ == '__main__':
    main()
