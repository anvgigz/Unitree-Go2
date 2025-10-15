# Unitree Go2 Robot Control

A Python library for controlling and programming the Unitree Go2 quadruped robot. This project provides a high-level interface for robot control, motion planning, and task execution.

## Features

- 🤖 Simple and intuitive API for robot control
- 🎯 High-level motion primitives (walk, stand, sit, etc.)
- 🔄 Real-time robot state monitoring
- 📝 Well-documented codebase with examples
- 🧪 Comprehensive test suite
- 🛠️ Easy to extend and customize

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Access to Unitree Go2 robot (physical or simulator)

### Basic Installation

1. Clone the repository:
```bash
git clone https://github.com/anvgigz/Unitree-Go2.git
cd Unitree-Go2
```

2. Install the package:
```bash
pip install -e .
```

### Development Installation

For development work, install with development dependencies:

```bash
pip install -e ".[dev]"
# or
pip install -r requirements-dev.txt
```

## Quick Start

Here's a simple example to get started:

```python
from unitree_go2.controller import Go2Controller
import time

# Initialize and connect to robot
robot = Go2Controller(robot_ip="192.168.123.161")
robot.connect()

# Stand up
robot.stand_up()
time.sleep(2)

# Move forward
robot.move(x=0.3, y=0.0, yaw=0.0)
time.sleep(3)

# Stop and sit down
robot.move(x=0.0, y=0.0, yaw=0.0)
robot.sit_down()

# Disconnect
robot.disconnect()
```

## Documentation

### Project Structure

```
Unitree-Go2/
├── src/
│   └── unitree_go2/        # Main package
│       ├── __init__.py
│       └── controller.py   # Robot controller
├── tests/                   # Test suite
│   ├── __init__.py
│   └── test_controller.py
├── examples/                # Example scripts
│   ├── basic_control.py
│   └── advanced_movement.py
├── docs/                    # Documentation
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

### Running Examples

Basic control example:
```bash
python examples/basic_control.py
```

Advanced movement patterns:
```bash
python examples/advanced_movement.py
```

## Development

### Setting Up Development Environment

1. Fork the repository
2. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/Unitree-Go2.git
cd Unitree-Go2
```

3. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

### Running Tests

Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=unitree_go2 --cov-report=html
```

### Code Quality

Format code with Black:
```bash
black src/ tests/ examples/
```

Run linter:
```bash
flake8 src/ tests/ examples/
```

Type checking:
```bash
mypy src/
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on:
- Code of conduct
- Development workflow
- Coding standards
- How to submit pull requests

## Configuration

### Robot Connection

The default robot IP is `192.168.123.161` with port `8080`. You can customize this:

```python
robot = Go2Controller(robot_ip="YOUR_ROBOT_IP", port=YOUR_PORT)
```

### Network Setup

Ensure your computer is connected to the same network as the robot. The robot typically creates a WiFi network that you can connect to directly.

## API Reference

### Go2Controller

Main controller class for the Unitree Go2 robot.

#### Methods

- `connect()` - Establish connection with the robot
- `disconnect()` - Disconnect from the robot
- `move(x, y, yaw)` - Move the robot with specified velocities
- `stand_up()` - Command the robot to stand up
- `sit_down()` - Command the robot to sit down
- `get_state()` - Get current robot state

See the [API documentation](docs/) for complete details.

## Troubleshooting

### Connection Issues

If you cannot connect to the robot:
1. Verify the robot is powered on
2. Check network connection
3. Confirm the correct IP address
4. Ensure no firewall is blocking the connection

### Common Errors

**"Robot not connected"** - Call `robot.connect()` before sending commands

**Import errors** - Ensure the package is installed: `pip install -e .`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Unitree Robotics for the Go2 robot platform
- Contributors and maintainers of this project

## Support

- 📧 Email: [Open an issue](https://github.com/anvgigz/Unitree-Go2/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/anvgigz/Unitree-Go2/discussions)
- 🐛 Bug Reports: [Issue Tracker](https://github.com/anvgigz/Unitree-Go2/issues)

## Roadmap

- [ ] Complete SDK integration
- [ ] Add vision processing capabilities
- [ ] Implement advanced motion planning
- [ ] Add simulation support
- [ ] Create ROS integration
- [ ] Build GUI control interface

## Citation

If you use this project in your research, please cite:

```bibtex
@software{unitree_go2_python,
  title = {Unitree Go2 Python Control Library},
  author = {Unitree Go2 Team},
  year = {2024},
  url = {https://github.com/anvgigz/Unitree-Go2}
}
```
