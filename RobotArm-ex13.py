from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
for j in range(9):
    robotArm.grab()
    for i in range(10, 0, -1):
        if i % 2 == 0:
            for x in range(i):
                robotArm.moveRight()
            robotArm.drop()
        else:
            for j in range(9):
                robotArm.moveLeft()
                robotArm.grab()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()