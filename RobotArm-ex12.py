from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
for i in range(9):
    robotArm.moveRight()
for i in range(18): 
    robotArm.grab()
    if robotArm.scan() == 'red':
        for i in range(9):
            robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()