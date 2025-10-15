"""
Tests for the Go2Controller class.
"""

import pytest
from unitree_go2.controller import Go2Controller


class TestGo2Controller:
    """Test suite for Go2Controller class."""
    
    def test_initialization(self):
        """Test controller initialization."""
        controller = Go2Controller()
        assert controller.robot_ip == "192.168.123.161"
        assert controller.port == 8080
        assert controller.connected is False
    
    def test_custom_initialization(self):
        """Test controller initialization with custom parameters."""
        controller = Go2Controller(robot_ip="192.168.1.100", port=9090)
        assert controller.robot_ip == "192.168.1.100"
        assert controller.port == 9090
    
    def test_connect(self):
        """Test connection to robot."""
        controller = Go2Controller()
        result = controller.connect()
        assert result is True
        assert controller.connected is True
    
    def test_disconnect(self):
        """Test disconnection from robot."""
        controller = Go2Controller()
        controller.connect()
        controller.disconnect()
        assert controller.connected is False
    
    def test_move_when_connected(self):
        """Test movement command when connected."""
        controller = Go2Controller()
        controller.connect()
        result = controller.move(1.0, 0.0, 0.0)
        assert result is True
    
    def test_move_when_not_connected(self):
        """Test movement command when not connected."""
        controller = Go2Controller()
        result = controller.move(1.0, 0.0, 0.0)
        assert result is False
    
    def test_stand_up_when_connected(self):
        """Test stand up command when connected."""
        controller = Go2Controller()
        controller.connect()
        result = controller.stand_up()
        assert result is True
    
    def test_stand_up_when_not_connected(self):
        """Test stand up command when not connected."""
        controller = Go2Controller()
        result = controller.stand_up()
        assert result is False
    
    def test_sit_down_when_connected(self):
        """Test sit down command when connected."""
        controller = Go2Controller()
        controller.connect()
        result = controller.sit_down()
        assert result is True
    
    def test_get_state_when_connected(self):
        """Test getting robot state when connected."""
        controller = Go2Controller()
        controller.connect()
        state = controller.get_state()
        assert state is not None
        assert "position" in state
        assert "orientation" in state
        assert "battery" in state
        assert "mode" in state
    
    def test_get_state_when_not_connected(self):
        """Test getting robot state when not connected."""
        controller = Go2Controller()
        state = controller.get_state()
        assert state is None
