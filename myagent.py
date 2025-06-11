import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        
        sensor_readings = observations['lidar']
        speed = observations['velocity']
        
        
        angle_left = sensor_readings[0]
        forward = sensor_readings[2]
        angle_right = sensor_readings[4]

        
        threshold = 0.7 + speed + 0.2 * min(angle_left, angle_right)

        
        if angle_right - angle_left > 0.2:
            steering = 'right'
        elif angle_left - angle_right > 0.2:
            steering = 'left'
        else:
            steering = 'straight'

        
        if speed == 0:
            motion = 'accelerate'
        elif angle_left <= threshold or angle_right <= threshold:
            motion = 'brake'
        elif speed < 0.35 and forward > 0.45:
            motion = 'accelerate'
        else:
            motion = 'coast'

        
        return (steering, motion)
