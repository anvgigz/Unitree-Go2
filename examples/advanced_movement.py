#!/usr/bin/env python3
"""
Advanced Example: Custom movement patterns for the Unitree Go2 robot.

This example demonstrates how to create custom movement patterns
such as circles, squares, and figure-8s.
"""

import time
import math
from unitree_go2.controller import Go2Controller


def move_in_circle(robot: Go2Controller, radius: float = 0.5, duration: float = 10.0):
    """
    Move the robot in a circular pattern.
    
    Args:
        robot: Go2Controller instance
        radius: Radius of the circle in meters
        duration: Duration to complete the circle in seconds
    """
    print(f"Moving in circle (radius={radius}m, duration={duration}s)...")
    
    # Calculate velocities for circular motion
    angular_velocity = 2 * math.pi / duration
    linear_velocity = radius * angular_velocity
    
    start_time = time.time()
    while time.time() - start_time < duration:
        robot.move(x=linear_velocity, y=0.0, yaw=angular_velocity)
        time.sleep(0.1)
    
    robot.move(x=0.0, y=0.0, yaw=0.0)


def move_in_square(robot: Go2Controller, side_length: float = 1.0, speed: float = 0.2):
    """
    Move the robot in a square pattern.
    
    Args:
        robot: Go2Controller instance
        side_length: Length of each side in meters
        speed: Movement speed in m/s
    """
    print(f"Moving in square (side={side_length}m, speed={speed}m/s)...")
    
    duration_per_side = side_length / speed
    turn_time = 1.5  # Time to turn 90 degrees
    
    for i in range(4):
        print(f"  Side {i+1}/4")
        # Move forward
        robot.move(x=speed, y=0.0, yaw=0.0)
        time.sleep(duration_per_side)
        
        # Stop
        robot.move(x=0.0, y=0.0, yaw=0.0)
        time.sleep(0.5)
        
        # Turn 90 degrees
        robot.move(x=0.0, y=0.0, yaw=math.pi/2 / turn_time)
        time.sleep(turn_time)
        
        # Stop
        robot.move(x=0.0, y=0.0, yaw=0.0)
        time.sleep(0.5)


def main():
    """Main function demonstrating advanced movement patterns."""
    print("Initializing Go2 Controller for advanced movements...")
    robot = Go2Controller()
    
    if not robot.connect():
        print("Failed to connect to robot")
        return
    
    print("Connected successfully!")
    
    try:
        # Stand up
        print("\nMaking robot stand up...")
        robot.stand_up()
        time.sleep(2)
        
        # Move in circle
        print("\n--- Circle Pattern ---")
        move_in_circle(robot, radius=0.5, duration=8.0)
        time.sleep(2)
        
        # Move in square
        print("\n--- Square Pattern ---")
        move_in_square(robot, side_length=1.0, speed=0.2)
        time.sleep(2)
        
        # Sit down
        print("\nMaking robot sit down...")
        robot.sit_down()
        time.sleep(2)
        
    finally:
        print("\nDisconnecting from robot...")
        robot.disconnect()
        print("Done!")


if __name__ == "__main__":
    main()
