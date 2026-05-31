angles = [30, -15, 45, 200, 60, 90]

# Function to check valid angle

def is_valid(angle):
    return 0 <= angle <= 180

# Filter valid angles
valid_angles = list(filter(is_valid, angles))

# Convert to servo commands
servo_commands = list(map(lambda x: x * 10, valid_angles))

print("Valid Angles:", valid_angles)
print("Servo Commands:", servo_commands)