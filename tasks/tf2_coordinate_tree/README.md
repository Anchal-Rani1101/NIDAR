# TF2 Coordinate Transform Tree

## Task

Map the TF2 coordinate transform tree:

map -> base_link -> camera_link

## Approach

- Used ROS 2 and tf2_ros to publish TF transforms.
- map -> base_link is published dynamically to simulate drone movement.
- base_link -> camera_link is a fixed transform representing the camera mounted on the drone.
- Added the required tf2_ros dependency in package.xml.
- Added camera_link and its fixed joint to the drone URDF.

## TF Tree

map
└── base_link
    └── camera_link

## Verification

The transforms were verified using tf2_echo:

ros2 run tf2_ros tf2_echo map base_link

ros2 run tf2_ros tf2_echo base_link camera_link

The TF tree was also visualized and verified in RViz2.

## Status

Task completed and TF tree verified successfully.
