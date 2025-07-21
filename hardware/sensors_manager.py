"""
===============================================================================
  File        : sensors_manager.py
  Project     : Industrial Remote Relay IoT Node
  Description : Manages the sensors

  Author      : Hamas
  Created on  : 2025-07-21
  Version     : 1.0.0

  Dependencies:
    - adafruit-blinka
    - adafruit-circuitpython-ads1x15

  Internal Modules:
    - utils.logger

  Notes:
    - 

===============================================================================
"""
# hardware/sensos_manager.py

import time
import board
import busio
from   utils.logger                 import getLogger

try:
    from adafruit_ads1x15.ads1115   import ADS1115
    from adafruit_ads1x15.analog_in import AnalogIn
    ADS_AVAILABLE = True
except (ImportError, RuntimeError):
    ADS_AVAILABLE = False

class SensorsManager:
    def __init__(self, config=None):
        """
        Initialize the sensors manager.

        """
    
    def readSensors(self): 
        """
        Reads sensor values and calculates pressures.

        """
    
    def _readVoltages(self):
        """
        Reads the voltage values from all channels.

        """
    
    def _check_connection(self):
        """
        Check if the ADS1115 is connected and responding.

        """

    def _calculatePressures(self):
        """
        Calculate pressures from the voltages read from all channels.

        """