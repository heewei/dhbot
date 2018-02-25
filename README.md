# dhbot
Differential Robot


gundam.py - instance of robot with all robot functionalities
robotBuilder.py - Add more sensors and actuator to robot
robotBaseClass.py - Add motion sensors and odometry 
motionController.py - Allow setting motion target


Unit Classes:

odometry.py - read encoder tick updates, calculate distance traveled per wheel before robot pose based on simple differential drive 

Need to run:
1. sudo pigpiod


Yet to fix 
1. licence and registration...
2. Add localization with KF plus integrate into motionController.py
