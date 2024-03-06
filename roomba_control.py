from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.backend.bluetooth import Bluetooth



def startroomba(q):
    robot = Create3(Bluetooth('MonicaRoomba'))

    @event(robot.when_play)
    async def play(robot):
        
        print("ROBOT PLAY")
        while True:
            try:
                command = q.get(timeout=2)
                print("got command",command)
            except Exception as e:
                print("could not get queue",e)
                command=""
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
    


"""
class roombacontrol():

    left=0
    right=0

    speed=5

    moving=True

    def __init__(self):
        pass

    def startroomba(self):
        robot = Create3(Bluetooth('MonicaRoomba'))

        @event(robot.when_play)
        async def play(robot):

            while self.moving:

                await robot.set_wheel_speeds(self.left,self.right )
        
        robot.play()
    
    async def docommand(self, command):
        if command=="":
            self.left=0
            self.right=0

        if command=="←":
            self.left=-self.speed
            self.right=self.speed

        if command=="→":
            self.left=self.speed
            self.right=-self.speed

        if command=="↑":
            self.left=self.speed
            self.right=self.speed


        if command=="↓":
            self.left=-self.speed
            self.right=-self.speed

        #await self.robot.set_wheel_speeds(self.left,self.right )
"""