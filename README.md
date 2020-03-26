### Drone perching

Mainly 3 packages are required

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
