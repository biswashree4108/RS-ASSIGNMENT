def decide_movement(sensor_values):
    if sensor_values == [0, 0, 0, 0, 0, 0]:
        return "Stop Robot"
    elif sensor_values == [1, 1, 1, 1, 1, 1]:
        return "Junction Detected"
    elif sensor_values[2] == 1 or sensor_values[3] == 1:
        return "Move Forward"
    elif sensor_values[0] == 1 or sensor_values[1] == 1:
        return "Turn Left"
    elif sensor_values[4] == 1 or sensor_values[5] == 1:
        return "Turn Right"
    else:
        return "No Action"