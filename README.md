# VirtMouse

This project implements a virtual mouse using hand tracking powered by OpenCV, MediaPipe, and PyAutoGUI. It allows users to control their mouse pointer through hand gestures, creating a touch-free and interactive experience. By tracking the index and thumb fingertips, users can move the mouse pointer and perform click actions based on the relative position of these fingers.

Real-time Hand Tracking: Uses MediaPipe for fast, accurate hand landmark detection.
Smooth Mouse Movements: Exponential smoothing and low-pass filtering ensure smooth cursor control.
Click Detection: Detects and triggers mouse clicks based on the proximity of the index and thumb fingertips.
Customizable Sensitivity: Easily adjust thresholds and smoothing factors for optimized performance.

Requirements:
Python 3.7+
OpenCV (for video capture and display)
MediaPipe (for hand landmark detection)
PyAutoGUI (for mouse control)

Usage:
Ensure your webcam is connected and positioned correctly.
Run the script and observe the webcam feed in a new window titled Virtual Mouse.
Move your index finger to control the cursor on the screen.
Bring your index finger and thumb together to simulate a mouse click.
Press Q on your keyboard to exit the application.

Code Explanation
The core functionality of the virtual mouse is split into several key parts:

Capture Setup: The webcam feed is initialized using OpenCV. The frame rate is set for smoother processing.

Hand Detection: MediaPipe's Hands class is used to detect and track hand landmarks. The hand detector is set with a high confidence threshold for accurate tracking.

Gesture Recognition:

Mouse Movement: The index finger's position is mapped to the screen dimensions, enabling pointer control.
Click Action: When the index and thumb fingertips are close enough (below a defined distance threshold), a click event is triggered.
Smoothing Techniques:

Exponential Smoothing: Smooths the cursor movement to avoid jitter and sudden changes.
Dual-Threshold Click Detection: Enhances click accuracy by avoiding unintentional clicks due to minor finger movements.
Screen Mapping: Converts the detected hand landmark coordinates to the full screen’s resolution for accurate cursor movement.
