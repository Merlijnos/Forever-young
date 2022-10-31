from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

for i in range(10, 0, -1):
    if i % 2 == 1:
        for x in range(i):
            robotArm.moveRight()
        robotArm.drop()
    else:
        for x in range(i):
            robotArm.moveLeft()
        robotArm.grab()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()