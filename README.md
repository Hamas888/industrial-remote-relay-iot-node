# Industrial Remote Relay IoT Node

![Project Image](https://drive.google.com/uc?export=view&id=1gMNMCP0JVgDr9rk988y_4HUUdz9aIBgh)

## Table of Contents
1. **[Overview](#overview)**  
   - [Key Highlights](#key-highlights)
   - [Evolution Journey](#evolution-journey)
2. **[Features](#features)**  
3. **[Technical Specifications](#technical-specifications)**  
   - Production Model (Raspberry Pi 5)
   - Earlier Prototypes
4. **[Hardware](#hardware)**
5. **[Firmware](#firmware)**  
6. **[DevOps Solution](#devops-solution)**  
   - CI/CD Pipeline
   - Automated Deployment
   - OTA Update Integration
7. **Installation Guide**  
   - [Hardware Setup](#hardware-setup)  
   - [Software Configuration](#software-configuration)  
8. **[AWS Architecture](#aws-architecture)**  
   - [AWS Architecture Flow Chart](#aws-architecture-flow-chart)  
9. **[Web Application](#web-application)**  
   - [Application Screenshots](#application-screenshots)
10. **Power Management**  
11. **Future Enhancements**  
12. **Licensing**  
    - [Commercial Use](#commercial-use)

## Overview
The Industrial Remote Relay IoT Node is an advanced industrial automation and monitoring system designed for real-time control, video surveillance, and data acquisition in remote locations. This comprehensive solution combines robust hardware with sophisticated cloud-based software, providing relay control, high-resolution video monitoring with motion detection, GPS geofencing, analog sensor integration, and live streaming capabilities—all managed through a role-based web application built on AWS infrastructure.

### Key Highlights
- **Industrial-Grade Hardware**: Raspberry Pi 5-based system with 64MP Arducam, SIM7600 LTE modem, dual relays, and multi-sensor support.
- **Advanced Video Processing**: Multi-threaded architecture for continuous recording, motion detection, encoding, and cloud uploads with zero event gaps.
- **Real-Time Monitoring**: Live video streaming via WebRTC, sensor data visualization, and GPS tracking with geofencing capabilities.
- **Complete AWS Integration**: MQTT communication via AWS IoT Core, S3 video storage, Lambda-based processing, and comprehensive cloud management.
- **Role-Based Web Application**: React-based dashboard with device management, scheduling, alerts, recordings, and user administration.

### Evolution Journey
The project evolved through multiple development phases to meet increasing requirements:

**Phase 1 - Proof of Concept**: Initial prototype built on ESP32 with SIM7000G modem for basic MQTT communication and relay control functionality.

**Phase 2 - First Prototype**: Migration to Raspberry Pi Zero to add video processing capabilities and enhanced sensor integration.

**Phase 3 - Production Model**: Final upgrade to Raspberry Pi 5 driven by critical requirements:
- High-resolution video processing (64MP Arducam with autofocus)
- Real-time motion detection using OpenCV
- Multi-threaded parallel processing to eliminate event gaps during recording
- Simultaneous recording, motion detection, encoding, and uploading
- Modem upgrade from SIM7000 (NB-IoT/LTE-M) to SIM7600 (LTE Cat 4) for reliable large file uploads
- libcamera support and Picamera2 integration for enhanced camera control

The evolution was necessary because sequential processing (record → encode → upload) resulted in missed events. The multi-threaded architecture on Raspberry Pi 5 enables continuous operation across all functions simultaneously.

## Features

- **Dual Relay Control**: Two independent relay outputs with scheduling, manual control, and duration settings.
- **Input Point Detection**: Two digital input channels for monitoring external device states and triggering events.
- **High-Resolution Surveillance**: 64MP Arducam with autofocus providing crystal-clear security footage.
- **Real-Time Motion Detection**: OpenCV-powered motion detection running continuously in parallel thread.
- **Multi-Threaded Processing**: Simultaneous recording, motion detection, FFmpeg encoding, and S3 uploads with zero event gaps.
- **Live Video Streaming**: On-demand WebRTC streaming for real-time device monitoring via web application.
- **Analog Sensor Integration**: Multiple analog sensor inputs with real-time data transmission to cloud.
- **GPS Geofencing**: Location tracking with customizable geofence boundaries and breach alerts.
- **AWS Cloud Integration**: MQTT via AWS IoT Core with S3 storage for recordings and DynamoDB for device data.
- **Comprehensive Web Application**: React-based dashboard with device management, user roles, scheduling, and analytics.
- **Multi-Channel Alerts**: SMS, email, and in-app notifications for geofence, relay, sensor, and system events.
- **Scheduled Automation**: Time-based relay control with flexible scheduling and cloud execution.

## Technical Specifications

- **Production Model (Raspberry Pi 5)**
  - **Main Controller**: Raspberry Pi 5 (Quad-core ARM Cortex, 4GB/8GB RAM)
  - **Modem**: SIM7600 (LTE Cat 4 - up to 150 Mbps download, 50 Mbps upload)
  - **Camera**: 64MP Arducam with autofocus and libcamera support
  - **Relay Outputs**: 2 channels (10A per channel, isolated)
  - **Digital Inputs**: 2 channels (3.3V - 24V range, isolated)
  - **Analog Inputs**: Multiple ADC channels (12/16-bit resolution)
  - **GPS**: Integrated GPS/GNSS with SIM7600
  - **Power Supply**: 9V - 36V DC input with battery backup
  - **Connectivity**: LTE Cat 4, MQTT over AWS IoT Core
  - **Enclosure**: IP65-rated weatherproof housing

- **Earlier Prototypes**
  - **Phase 1**: ESP32 + SIM7000G (NB-IoT/LTE-M)
  - **Phase 2**: Raspberry Pi Zero + SIM7000G
  - **Upgrade Rationale**: SIM7600 provides superior bandwidth for video uploads; Raspberry Pi 5 delivers processing power for parallel video operations

## Key Functions

1. **Intelligent Relay Control**
   - Scheduled automation with time-based relay operations
   - Manual override via web application for instant control
   - Duration-based control with automatic shutoff
   - Real-time relay state monitoring and alerts

2. **Advanced Video Surveillance**
   - 24/7 continuous recording with motion-triggered highlights
   - Multi-threaded parallel processing:
     - Thread 1: Continuous camera capture (Picamera2)
     - Thread 2: Real-time motion detection (OpenCV)
     - Thread 3: Video encoding (FFmpeg - H.264/H.265)
     - Thread 4: Cloud uploads to AWS S3 (Boto3)
   - Zero event gaps through simultaneous operations
   - Secure encrypted storage on AWS S3 with retention policies

3. **Live Video Streaming**
   - On-demand WebRTC streaming initiated from web application
   - Low-latency real-time viewing with adaptive bitrate
   - Multi-user simultaneous stream support
   - Bandwidth-optimized transmission

4. **GPS Geofencing**
   - Real-time location tracking and mapping
   - Custom geofence region creation and modification
   - Expand, contract, and move geofence boundaries
   - Instant breach alerts when device exits defined area
   - Location history tracking and playback

5. **Sensor Data Acquisition**
   - Multiple analog sensor channels with real-time monitoring
   - Configurable threshold-based alerts
   - Historical data logging and visualization
   - MQTT-based real-time data streaming to cloud

6. **Input Point Monitoring**
   - External device state detection (ON/OFF events)
   - Event logging with timestamps and metadata
   - Configurable alerts for state changes
   - Integration with external switches and control systems

7. **Multi-Channel Alerting**
   - SMS notifications to configured phone numbers
   - Email alerts with detailed event information
   - In-app real-time notifications
   - Alert types: geofence breach, relay state change, input point change, sensor thresholds, system errors, network issues, battery warnings
   - Granular alert enable/disable controls per user

## Mechanical Design

- **Industrial-Grade Enclosure**: IP65-rated weatherproof housing designed for harsh outdoor environments.
- **Thermal Management**: Proper ventilation and heat dissipation for continuous Raspberry Pi 5 operation.
- **Component Protection**: Shock-resistant mounting for camera, sensors, and electronics.
- **Cable Management**: Sealed cable entry points with strain relief for all connections.
- **Easy Access**: Tool-free battery access panel for quick replacements.
- **Mounting Options**: Versatile mounting brackets for wall, pole, or surface installation.

## Hardware

- **Raspberry Pi 5 Core**: Provides computational power for parallel video processing, multi-threading, and real-time operations.
- **SIM7600 LTE Modem**: LTE Cat 4 connectivity with integrated GPS/GNSS, USB interface for high-speed data transfer to Raspberry Pi.
- **64MP Arducam Module**: High-resolution imaging with autofocus, wide field of view, libcamera compatibility, and low-light optimization.
- **Relay Module**: 2-channel isolated relays with optical isolation, LED status indicators, and high current handling (10A per channel).
- **Input Interface**: 2 isolated digital inputs with wide voltage range (3.3V - 24V), debouncing circuitry, and reverse polarity protection.
- **Analog Input Module**: Multiple ADC channels with 12/16-bit resolution, configurable ranges, and signal conditioning.
- **Power Management System**: Wide input voltage (9V - 36V DC), battery backup support, low-power sleep modes, and voltage/current monitoring.

## Firmware

The firmware employs a multi-threaded Python architecture optimized for continuous operation and real-time processing. The design ensures no events are missed during video recording, encoding, or uploading operations.

- **Multi-Threaded Architecture**: Separate threads handle camera capture, motion detection, video encoding, cloud uploads, MQTT communication, sensor acquisition, GPS tracking, and system monitoring.
- **Parallel Processing**: All operations run simultaneously using circular buffers to prevent memory overflow during high-activity periods.
- **Motion Detection Pipeline**: OpenCV background subtraction with configurable sensitivity, triggering high-quality recordings on detected motion with pre-roll buffer support.
- **Video Encoding**: FFmpeg-based H.264/H.265 encoding with metadata embedding (timestamps, GPS coordinates, sensor data).
- **AWS SDK Integration**: 
  - Persistent MQTT connection to AWS IoT Core with automatic reconnection
  - Boto3 for efficient multipart S3 uploads of large video files
  - Device Shadow for state synchronization
  - Error handling with retry logic and message queuing
- **Over-the-Air Updates**: Support for remote firmware updates via AWS S3 with safe rollback on failure.
- **Watchdog System**: Automatic recovery and restart on system errors or hangs.

## DevOps Solution

A complete CI/CD pipeline has been developed for automated building, testing, and deployment of firmware updates:

- **Continuous Integration Pipeline:**
  - Automated build system triggered on code commits to main branch
  - Version management with automatic version bumping
  - Firmware compilation and binary generation
  - Automated testing and validation

- **Deployment Automation:**
  - Python scripts automate the entire deployment workflow
  - Firmware binaries automatically uploaded to AWS S3 buckets
  - Version manifest files generated and distributed
  - Deployment notifications to monitoring systems

- **OTA Update Integration:**
  - Devices periodically check AWS S3 for firmware updates
  - Automatic download and installation of new firmware versions
  - Safe rollback mechanism on update failures
  - Update status reporting back to cloud infrastructure

The DevOps pipeline ensures rapid deployment of bug fixes and new features to all deployed devices with zero manual intervention.

## Installation and Setup

### Hardware Setup
- **Step 1**: Mount the device enclosure in desired location with proper orientation for camera view.
- **Step 2**: Connect power supply (9V - 36V DC) ensuring correct polarity.
- **Step 3**: Insert activated SIM card with data plan into SIM7600 modem.
- **Step 4**: Attach LTE and GPS antennas securely to designated connectors.
- **Step 5**: Wire relay outputs to controlled devices (ensure proper load ratings).
- **Step 6**: Connect input points to monitored sources (switches, sensors, etc.).
- **Step 7**: Connect analog sensors to designated input channels if required.

### Software Configuration
- **Step 1**: Admin provisions device in web application and generates device credentials.
- **Step 2**: Device automatically connects to AWS IoT Core on first boot using pre-configured certificates.
- **Step 3**: Assign device to user or group via web application.
- **Step 4**: Configure alert preferences (SMS numbers, email addresses, alert types).
- **Step 5**: Create geofence boundary on map interface if location monitoring required.
- **Step 6**: Set up relay schedules and automation rules as needed.
- **Step 7**: Test live video stream and verify sensor data transmission.

## AWS Architecture

The system leverages a comprehensive AWS infrastructure for data processing, storage, user management, and real-time communication. All devices connect to a centralized cloud platform that handles device management, video storage, alert processing, and user interactions.

**Core AWS Services:**
- **AWS IoT Core**: MQTT broker for device-to-cloud communication with secure TLS connections
- **AWS S3**: Video and image storage with intelligent tiering and lifecycle policies
- **AWS Lambda**: Serverless functions for data processing, alerts, and business logic
- **AWS API Gateway**: RESTful API backend for web application
- **AWS Cognito**: User authentication, authorization, and role-based access control
- **AWS DynamoDB**: Device metadata, user profiles, schedules, and event logs
- **AWS SNS**: SMS and email notification delivery service
- **AWS CloudWatch**: System monitoring, logging, and performance metrics

**Data Flow:**
1. Device publishes sensor data, events, and status to AWS IoT Core via MQTT
2. IoT Rules engine processes incoming data and triggers appropriate Lambda functions
3. Lambda functions update DynamoDB records and generate alerts via SNS
4. Video files uploaded to S3 with event metadata and indexed in DynamoDB
5. Web application queries data through API Gateway REST endpoints
6. CloudWatch monitors system health, device connectivity, and error rates
7. Users receive real-time alerts via SMS, email, or in-app notifications

### AWS Architecture Flow Chart
![Project Image](https://drive.google.com/uc?export=view&id=INSERT_YOUR_AWS_ARCHITECTURE_IMAGE_ID) 

## Web Application

A comprehensive React-based web application provides complete system management with role-based access control, real-time monitoring, and advanced device administration.

**Core Application Features:**

1. **Device Management Dashboard**
   - Real-time overview of all devices with status indicators
   - Complete device details: sensor data, alerts, errors, network info, battery status, GPS location
   - Device provisioning and registration (Admin only)
   - Device assignment to users or groups
   - Live camera icon for instant WebRTC stream launch
   - Remote configuration and parameter updates

2. **User Management System**
   - Role-based access control: Admin, User, Viewer permissions
   - User CRUD operations with granular permission management
   - Admin privilege escalation and revocation
   - User activity logging and audit trails

3. **Device Groups**
   - Create and manage logical device groups
   - Add/remove devices from groups dynamically
   - Bulk operations on multiple devices
   - Group-based permission assignments

4. **Event Scheduling**
   - Create time-based relay schedules with specific dates, times, and durations
   - Select which relays to control (Relay 1, Relay 2, or both)
   - Recurring event patterns (daily, weekly, custom)
   - Cloud-executed schedules with manual override capability
   - Schedule history and audit logs

5. **Interactive Map View**
   - Real-time GPS positions of all devices on interactive map
   - Geofence boundary visualization with customizable regions
   - Geofence editor: draw, move, expand, contract, and delete boundaries
   - Device location history playback with timeline
   - Device clustering for large fleets

6. **Recordings Library**
   - Browse all recorded videos organized by device and date
   - Filter by date range, device, motion events, and duration
   - In-browser video player with seek controls and playback speed
   - Download recordings for offline viewing
   - Display metadata: timestamps, GPS location, sensor data during recording
   - Thumbnail preview grid for quick scanning

7. **Live Data Feed**
   - Real-time raw device data packets as they arrive via MQTT
   - Live sensor value updates with graphical visualization
   - System status monitoring: network quality, signal strength, battery level
   - Event log stream showing all device activities
   - Debug console for technical diagnostics and troubleshooting

8. **Alert Configuration**
   - Configure notification channels: SMS (phone numbers), Email (addresses), In-App
   - Enable/disable specific alert types: geofence breach, relay state change, input point change, sensor thresholds, system errors, battery warnings
   - Set alert priority levels and custom message templates
   - Alert history and acknowledgment tracking

9. **Analytics Dashboard**
   - Device uptime and availability statistics
   - Data usage and bandwidth consumption metrics
   - Event counts and patterns over time
   - Sensor data trends with historical visualization
   - Relay operation logs and usage patterns
   - System health and performance diagnostics

### Application Screenshots
![Project Image](https://drive.google.com/uc?export=view&id=INSERT_DASHBOARD_SCREENSHOT_ID)
*Dashboard Overview*

![Project Image](https://drive.google.com/uc?export=view&id=INSERT_DEVICE_DETAILS_SCREENSHOT_ID)
*Device Details Page*

![Project Image](https://drive.google.com/uc?export=view&id=INSERT_MAP_VIEW_SCREENSHOT_ID)
*Map View with Geofencing*

![Project Image](https://drive.google.com/uc?export=view&id=INSERT_RECORDINGS_SCREENSHOT_ID)
*Recordings Library*

![Project Image](https://drive.google.com/uc?export=view&id=INSERT_LIVE_STREAM_SCREENSHOT_ID)
*Live Video Stream*

![Project Image](https://drive.google.com/uc?export=view&id=INSERT_SCHEDULING_SCREENSHOT_ID)
*Event Scheduling Interface*

## Power Management
The system is designed for continuous 24/7 operation with intelligent power management. The device operates primarily on main power (9V - 36V DC) with automatic battery backup during power outages. Real-time voltage and current monitoring tracks power consumption, with configurable low-battery alerts. The system supports optional sleep modes during inactive periods to reduce power consumption, with graceful shutdown procedures on critical battery levels to protect data integrity.

## Future Enhancements
- **AI-Powered Analytics**: Machine learning for predictive maintenance and anomaly detection.
- **Enhanced Motion Detection**: Object classification to distinguish between people, vehicles, and animals.
- **Multi-Camera Support**: Connect multiple cameras to single node for comprehensive coverage.
- **Audio Integration**: Microphone support for audio recording and two-way communication.
- **Edge Processing**: On-device AI inference to reduce bandwidth usage and enable offline operation.
- **Mesh Networking**: Multi-node communication for extended coverage without additional infrastructure.
- **Third-Party Integrations**: APIs for Zapier, IFTTT, and home automation platforms.
- **Mobile Applications**: Native iOS and Android apps for enhanced mobile experience.
- **Advanced Scheduling**: Sunrise/sunset-based scheduling and conditional logic based on sensor inputs.

## Licensing
The code provided in this repository is available under the following conditions:

- **Non-Commercial Use**: You may use and distribute the code for non-commercial purposes.
- **Restricted Modification**: You may not reverse-engineer, modify, or distribute any part of the implementation not explicitly provided in this repository.

### Commercial Use
For commercial use, including selling or distributing products based on this project, please contact [hamasaeed@gmail.com](mailto:hamasaeed888@gmail.com) for licensing details.
