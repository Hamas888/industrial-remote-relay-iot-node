"""
===============================================================================
  File        : gsm_manager.py
  Project     : Industrial Remote Relay IoT Node
  Description : Manages the GSM module

  Author      : Hamas
  Created on  : 2025-07-21
  Version     : 1.0.0

  Dependencies:
    - pyserial
    - geopy

  Internal Modules:
    - utils.logger

  Notes:
    - Needs hardware uart to be enbaled in the RPI

===============================================================================
"""
# hardware/gsm_manager.py

import  os
import  re
import  sys
import  time
import  serial
import  subprocess
from    geopy.distance  import geodesic
from    utils.logger    import getLogger

class GSMManager:
    def __init__(self, settings, relays):
        """
        Initializes the GSM manager

        """
      
    
    def close(self):
        """
        Close the serial port if it's open.
        
        """

    
    def _stopPeer(self):
        """
        Stops the peer connection.

        """
    
    def _startPeer(self):
        """
        Starts the peer connection.

        """
    
    def restartPeer(self):
        """
        Restarts the peer connection by stopping and enabling it.

        """
       
    def _enablePeer(self):
        """
        Enable the peer connection by starting it and checking its status.

        """
    
    def _initialize(self):
        """
        Initializes the GSM manager Functionality.

        """

    def _startSerial(self):
        """
        Establishes a connection to the serial port specified in the settings.

        """

    def _closeSerial(self):
        """
        Closes the serial port if it is open. 

        """

    def isInitialized(self): 
        """
        Returns True if the GSM manager is initialized, False otherwise.

        """
    
    def _removeAllDefaultRoutes(self):
        """
        Removes all default routes from the system.

        """
         
    def _getGnssInfo(self) -> dict | None:
        """
        Returns dict with GNSS info fields or None:
        { 'run_status', 'fix_status', 'utc', 'lat', 'lon', 'speed', ... }

        """
    
    def isInternetAvailable(self) -> bool:
        """
        Returns True if the internet is available through the ppp0 interface,
        False otherwise.

        """
 
    def _makePeerDefault(self, interface="ppp0"):
        """
        Set the default route to the given interface (ppp0 by default).

        """
      
    def getDeviceIMEI(self, frequent= False) -> str: 
        """
        Returns the device's IMEI number as a string or "Not Configured" if the device is not initialized or the modem is not responding.

        """
    
    def _checkPeerConnection(self, interface="ppp0"):
        """
        Checks the peer connection status and sets the self._isInternet flag accordingly.

        """
    
     
    def _enableGnss(self, enable: bool = True) -> bool:
        """
        Enables or disables the GNSS (GPS) of the device.

        """
    
    def getNetworkStrength(self, frequent= False) -> int:
        """
        Retrieves the current network signal strength as a percentage.

        """
    
    def _sendATCommand(self, command, timeout=2, retries=3):
        """
        Sends an AT command to the modem and returns the response.

        """
        for attempt in range(retries):
            try:
                if self._serial is None or not self._serial.is_open:
                    self._startSerial()
                    if self._serial is None or not self._serial.is_open:
                        self.logger.error("Failed to open serial port")
                        time.sleep(1)  
                        continue

                # Clear any pending data
                self._serial.reset_input_buffer()
                self._serial.reset_output_buffer()
                
                # Send command
                self._serial.write(f"{command}\r\n".encode())
                time.sleep(timeout)
                
                # Read response
                response = self._serial.read_all().decode().strip()
                
                if response:
                    return response
                else:
                    self.logger.warning(f"No response from modem (attempt {attempt + 1}/{retries})")
                    
            except serial.SerialException as e:
                self.logger.error(f"Serial port error: {e}")
                self._closeSerial()
                self._serial = None
                time.sleep(1)  # Wait before retry
            except Exception as e:
                self.logger.error(f"AT command failed: {e}")
                self._closeSerial()
                self._serial = None
                time.sleep(1)  # Wait before retry
                
        self.logger.error(f"AT command '{command}' failed after {retries} attempts")
        return None
    
    def sendSMS(self, message: str, frequent= False) -> bool:
        """
        Sends an SMS message to the configured phone number.

        """
    
    def isInsideGeofence(self, settings, frequent=False) -> int:
        """
        Checks if the device is inside the geofence.

        """

    def _runTerminalcmd(self, cmd, capture_output=True, text=True, wait=0.5):
        """
        Runs a shell command and returns (returncode, stdout, stderr).

        """
    
    def _getCoordinates(self, timeout: int = 60) -> tuple[float,float] | None:
        """
        Acquires the current GPS coordinates using the device's GNSS capability.

        """