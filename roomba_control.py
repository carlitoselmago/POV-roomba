from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.backend.bluetooth import Bluetooth

class roombacontrol():

    left=0
    right=0

    speed=5

    moving=False

    def __init__(self):
        self.robot = Create3(Bluetooth('MonicaRoomba'))

        @event(self.robot.when_play)
        async def move():

            while self.moving:

                await self.robot.set_wheel_speeds(self.left,self.right )
        
        #self.robot.play()

    
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

        await self.robot.set_wheel_speeds(self.left,self.right )