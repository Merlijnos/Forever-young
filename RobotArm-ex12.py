from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
# Jouw python instructies zet je vanaf hier:
var1=1
robotArm.speed = 1
for j in range(9): 
    robotArm.grab()
    if robotArm.scan() == 'red':
        var1+=1
        for k in range(9):
            robotArm.moveRight()
        robotArm.drop()
        var2 = 10-var1
        for c in range(var2):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
        var1+=1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()