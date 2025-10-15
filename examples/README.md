# Examples

This directory contains example scripts demonstrating how to use the Unitree Go2 Python library.

## Available Examples

### 1. Basic Control (`basic_control.py`)

**Description:** Demonstrates fundamental robot control operations.

**Features:**
- Connecting to the robot
- Standing up and sitting down
- Basic forward movement
- Checking robot state
- Proper connection/disconnection handling

**Usage:**
```bash
python examples/basic_control.py
```

**What it does:**
1. Initializes the controller
2. Connects to the robot
3. Makes the robot stand up
4. Checks and displays robot state
5. Moves forward for 3 seconds
6. Stops the robot
7. Makes the robot sit down
8. Disconnects from the robot

**Configuration:**
Edit the robot IP address in the script if your robot uses a different IP:
```python
robot = Go2Controller(robot_ip="YOUR_ROBOT_IP")
```

---

### 2. Advanced Movement (`advanced_movement.py`)

**Description:** Shows how to create complex movement patterns.

**Features:**
- Circular motion
- Square movement pattern
- Custom trajectory planning
- Timed movements

**Usage:**
```bash
python examples/advanced_movement.py
```

**Movement Patterns:**

**Circle Pattern:**
- Moves robot in a circular path
- Configurable radius and duration
- Smooth continuous motion

**Square Pattern:**
- Moves in a square shape
- Configurable side length and speed
- Includes 90-degree turns at corners

**Customization:**
Modify parameters in the script:
```python
# Circle
move_in_circle(robot, radius=0.5, duration=8.0)

# Square
move_in_square(robot, side_length=1.0, speed=0.2)
```

---

## Creating Your Own Examples

### Template

Use this template to create new examples:

```python
#!/usr/bin/env python3
"""
Example: Description of what this example does

This example demonstrates:
- Feature 1
- Feature 2
- Feature 3
"""

import time
from unitree_go2.controller import Go2Controller


def main():
    """Main function."""
    # Initialize controller
    robot = Go2Controller()
    
    # Connect
    if not robot.connect():
        print("Failed to connect")
        return
    
    try:
        # Your robot control logic here
        robot.stand_up()
        time.sleep(2)
        
        # ... more operations ...
        
    finally:
        # Always disconnect
        robot.disconnect()


if __name__ == "__main__":
    main()
```

### Best Practices

1. **Always use try-finally:** Ensure the robot disconnects even if an error occurs
2. **Add delays:** Give the robot time to complete actions before the next command
3. **Check connection:** Verify connection before sending commands
4. **Add comments:** Explain what each section does
5. **Make it runnable:** Add shebang and make executable
6. **Error handling:** Handle connection failures gracefully

### Safety Considerations

⚠️ **Before running any example:**

1. Ensure adequate space around the robot (minimum 2m radius)
2. Keep emergency stop accessible
3. Start with slow speeds
4. Monitor the robot during operation
5. Be prepared to stop the robot if needed
6. Test in simulation first if available

### Testing Examples

Test your examples safely:

```bash
# 1. Test syntax
python -m py_compile examples/your_example.py

# 2. Dry run (without robot)
# Comment out actual robot commands first

# 3. Test with robot
python examples/your_example.py
```

## Example Ideas

Here are some ideas for additional examples:

### Beginner Level
- **hello_robot.py**: Minimal example to verify connection
- **led_control.py**: Control robot LEDs
- **sensor_reading.py**: Read and display sensor data

### Intermediate Level
- **obstacle_avoidance.py**: Simple obstacle avoidance
- **waypoint_navigation.py**: Navigate through predefined waypoints
- **dance_routine.py**: Choreographed movement sequence

### Advanced Level
- **vision_tracking.py**: Follow objects using camera
- **terrain_adaptation.py**: Adapt gait to different terrains
- **multi_robot_coordination.py**: Coordinate multiple robots

## Troubleshooting

### Common Issues

**Problem: Connection fails**
```
Failed to connect to robot
```
**Solution:**
- Check robot is powered on
- Verify network connection
- Confirm correct IP address

**Problem: Robot doesn't move**
```
Moving robot: x=0.3, y=0.0, yaw=0.0
# But robot stays still
```
**Solution:**
- Ensure robot is in the correct mode
- Check if robot is standing
- Verify command is being sent correctly

**Problem: ImportError**
```
ModuleNotFoundError: No module named 'unitree_go2'
```
**Solution:**
```bash
pip install -e .
```

### Getting Help

- Read the [documentation](../docs/)
- Check [GitHub Issues](https://github.com/anvgigz/Unitree-Go2/issues)
- Review [CONTRIBUTING.md](../CONTRIBUTING.md)

## Contributing Examples

We welcome example contributions! To add an example:

1. Create your example script in this directory
2. Add documentation (comments in code + entry in this README)
3. Test thoroughly
4. Submit a pull request

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines.

## Additional Resources

- [API Reference](../docs/) - Detailed API documentation
- [Getting Started](../docs/GETTING_STARTED.md) - Setup guide
- [Project Structure](../docs/PROJECT_STRUCTURE.md) - Project organization

---

**Note:** These examples use placeholder implementations. When the actual Unitree SDK is integrated, the commands will control the real robot hardware.
