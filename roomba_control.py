from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.backend.bluetooth import Bluetooth
import elara


def startroomba(q):
    db = elara.exe("roomba.db")
    robot = Create3(Bluetooth('MonicaRoomba'))

    @event(robot.when_play)
    async def play(robot):
        
        print("ROBOT PLAY")
        while True:
            command=db.get("direction")

            left=0
            right=0

            speed=5
            
            if command=="":
                left=0
                right=0

            if command=="←":
                left=-speed
                right=speed

            if command=="→":
                left=speed
                right=-speed

            if command=="↑":
                left=speed
                right=speed


            if command=="↓":
                left=-speed
                right=-speed

            await robot.set_wheel_speeds(left,right )
    
    robot.play()
    
