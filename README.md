### Drone perching

Mainly 3 packages are required

#### Installing TooN

```
$ git clone https://github.com/edrosten/TooN.git
$ cd TooN
$ ./configure && make && sudo make install
```

### In terminal 1

```
roslaunch cylinder_detection cylinder_detection.launch
```
This will take a published image and detect lines from that image and publish it in the form of ```ImageFeatures``` message.

### In terminal 2

```
python imgPulisher.py
```
This will publish one image and a fixed IMU message continuously and cylinder_detection package will find edges in that iamge.

### In terminal 3

```
roslaunch process_image_features simple_test.launch
```
 This will get the ```ImageFeatures``` messages along with the IMU data of drone to predict the pose of cylinder in space.


## rotorS simulator

Simulator and installation instrunctions can be found [here](https://github.com/ethz-asl/rotors_simulator)

For camera we need to change some of the things. 
This can run a rotor without any camera
```
$ roslaunch rotors_gazebo mav_hovering_example.launch mav_name:=firefly world_name:=basic
```
For drone with camera. But camea is in front direction. We need camera on top.
To mount camera on top, we need to change some of the things in rotor's urdf files. Go to rotor_description/urdf/mav_with_vi_sensor.gazebo and change the following line.
```<origin xyz="0.1 0 -0.03" rpy="0.0 0.1 0.0">``` to this line ```<origin xyz="0 0 0.1" rpy="0.0 -1.57 0.0" />```

Now use this command to start a simulator with the camera on the top of the drone.
```
$ roslaunch rotors_gazebo mav_hovering_example_with_vi_sensor.launch mav_name:=firefly world_name:=basic
```
