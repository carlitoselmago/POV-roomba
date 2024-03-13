from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.backend.bluetooth import Bluetooth
import elara
import time

def starttimer():
    global start_time
    global duration

def checktimer():
    global start_time
    global duration
    if time.time() - start_time > duration:
        print("Timer reset!")
        start_time = time.time()  # Reset start time
        return True 
    return False

def startroomba():
    db = elara.exe("roomba.db")
    robot = Create3(Bluetooth('MonicaRoomba'))

    firstrun=True

    #timed logics
    start_time = time.time()
    duration=1*60 #each minute 

    @event(robot.when_play)
    async def play(robot):
        
        print("ROBOT PLAY")
        while True:
            command=db.get("command")

            left=0
            right=0

            speed=8
            turningspeed=5
            
            if command=="":
                left=0
                right=0

            if command=="←":
                left=-turningspeed
                right=turningspeed

            if command=="→":
                left=turningspeed
                right=-turningspeed

            if command=="↑":
                left=speed
                right=speed


            if command=="↓":
                left=-speed
                right=-speed

            if checktimer() or firstrun:
                battery = await robot.get_battery_level()
                batterypercent=battery[1]
                db.set("battery", batterypercent)

            if command=="dock":
                await robot.dock()
            else:
                await robot.set_wheel_speeds(left,right )
            
            firstrun=False
    
    robot.play()
    
