from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.speed=3
a = 1
b = 1
for x in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        for y in range(a):
            robotArm.moveRight()
        a += 1
        robotArm.drop()
        for z in range(b):
            robotArm.moveLeft()
            b += 1
    else:
        break
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()