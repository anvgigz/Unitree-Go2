#!/usr/bin/env python3
"""
Basic Example: Connecting and controlling the Unitree Go2 robot.

This example demonstrates how to:
1. Connect to the robot
2. Make the robot stand up
3. Move the robot forward
4. Check robot state
5. Make the robot sit down
6. Disconnect
"""

import time
from unitree_go2.controller import Go2Controller


def main():
    """Main function demonstrating basic robot control."""
    # Initialize controller
    print("Initializing Go2 Controller...")
    robot = Go2Controller(robot_ip="192.168.123.161")
    
    # Connect to robot
    print("\nConnecting to robot...")
    if not robot.connect():
        print("Failed to connect to robot")
        return
    
    print("Connected successfully!")
    
    try:
        # Stand up
        print("\nMaking robot stand up...")
        robot.stand_up()
        time.sleep(2)
        
        # Check state
        print("\nChecking robot state...")
        state = robot.get_state()
        if state:
            print(f"Position: {state['position']}")
            print(f"Orientation: {state['orientation']}")
            print(f"Battery: {state['battery']}%")
            print(f"Mode: {state['mode']}")
        
        # Move forward
        print("\nMoving robot forward...")
        robot.move(x=0.3, y=0.0, yaw=0.0)
        time.sleep(3)
        
        # Stop
        print("\nStopping robot...")
        robot.move(x=0.0, y=0.0, yaw=0.0)
        time.sleep(1)
        
        # Sit down
        print("\nMaking robot sit down...")
        robot.sit_down()
        time.sleep(2)
        
    finally:
        # Always disconnect
        print("\nDisconnecting from robot...")
        robot.disconnect()
        print("Done!")


if __name__ == "__main__":
    main()
