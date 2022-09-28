from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

robotArm.speed = 2
for i in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.grab()

robotArm.wait()