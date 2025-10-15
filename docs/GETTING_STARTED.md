# Getting Started with Unitree Go2

This guide will help you get started with the Unitree Go2 robot control library.

## Installation

### System Requirements

- Python 3.8 or higher
- pip package manager
- Network connection to the robot
- Unitree Go2 robot (hardware or simulator)

### Step-by-Step Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anvgigz/Unitree-Go2.git
   cd Unitree-Go2
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the package:**
   ```bash
   pip install -e .
   ```

4. **Verify installation:**
   ```bash
   python -c "from unitree_go2 import Go2Controller; print('Installation successful!')"
   ```

## First Steps

### Connecting to the Robot

1. **Power on the robot** and wait for it to boot up (indicated by LED status)

2. **Connect to the robot's WiFi network:**
   - Network name: Usually starts with "Unitree_Go2_"
   - Password: Check your robot documentation

3. **Verify network connection:**
   ```bash
   ping 192.168.123.161
   ```

### Running Your First Script

Create a file called `my_first_robot.py`:

```python
from unitree_go2.controller import Go2Controller
import time

# Create controller instance
robot = Go2Controller()

# Connect to robot
print("Connecting to robot...")
if robot.connect():
    print("Connected!")
    
    # Stand up
    robot.stand_up()
    time.sleep(3)
    
    # Sit down
    robot.sit_down()
    time.sleep(2)
    
    # Disconnect
    robot.disconnect()
    print("Done!")
else:
    print("Connection failed!")
```

Run it:
```bash
python my_first_robot.py
```

## Basic Operations

### Standing and Sitting

```python
robot = Go2Controller()
robot.connect()

# Stand up
robot.stand_up()
time.sleep(2)

# Sit down
robot.sit_down()
time.sleep(2)

robot.disconnect()
```

### Moving the Robot

```python
# Move forward at 0.3 m/s
robot.move(x=0.3, y=0.0, yaw=0.0)
time.sleep(2)

# Move backward
robot.move(x=-0.2, y=0.0, yaw=0.0)
time.sleep(2)

# Strafe left
robot.move(x=0.0, y=0.2, yaw=0.0)
time.sleep(2)

# Rotate in place
robot.move(x=0.0, y=0.0, yaw=0.5)
time.sleep(2)

# Stop
robot.move(x=0.0, y=0.0, yaw=0.0)
```

### Checking Robot State

```python
state = robot.get_state()
if state:
    print(f"Position: {state['position']}")
    print(f"Battery: {state['battery']}%")
    print(f"Mode: {state['mode']}")
```

## Running Examples

The repository includes example scripts in the `examples/` directory:

### Basic Control
```bash
python examples/basic_control.py
```

This example demonstrates:
- Connecting to the robot
- Standing up and sitting down
- Basic movement
- State monitoring

### Advanced Movement
```bash
python examples/advanced_movement.py
```

This example shows:
- Circular movement patterns
- Square movement patterns
- Custom trajectories

## Safety Tips

⚠️ **Important Safety Guidelines:**

1. **Always maintain clear space** around the robot (at least 2m radius)
2. **Never run untested code** on the physical robot without supervision
3. **Start with slow speeds** and gradually increase
4. **Keep emergency stop accessible** (power button)
5. **Monitor battery levels** - stop operation below 20%
6. **Test in simulation first** when possible

## Troubleshooting

### Cannot Connect to Robot

**Problem:** Connection times out or fails

**Solutions:**
- Verify robot is powered on and booted (check LED indicators)
- Confirm you're connected to the robot's WiFi network
- Check IP address (default: 192.168.123.161)
- Disable VPN if active
- Try pinging the robot: `ping 192.168.123.161`

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'unitree_go2'`

**Solutions:**
- Ensure package is installed: `pip install -e .`
- Activate virtual environment if using one
- Check Python version: `python --version` (must be 3.8+)

### Robot Not Responding

**Problem:** Commands sent but robot doesn't respond

**Solutions:**
- Verify connection: `robot.connected` should be `True`
- Check robot mode/state
- Restart the robot
- Re-establish connection

## Next Steps

Now that you're set up, explore:

1. **Read the API documentation** to understand all available methods
2. **Try the example scripts** to see different use cases
3. **Write your own control scripts** for specific tasks
4. **Join the community** to share and learn from others

## Additional Resources

- [Full API Reference](API.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Example Scripts](../examples/)
- [GitHub Issues](https://github.com/anvgigz/Unitree-Go2/issues)

## Getting Help

If you encounter issues:

1. Check this guide and the troubleshooting section
2. Search [existing issues](https://github.com/anvgigz/Unitree-Go2/issues)
3. Ask in [GitHub Discussions](https://github.com/anvgigz/Unitree-Go2/discussions)
4. Open a new issue with detailed information

Happy coding! 🤖
