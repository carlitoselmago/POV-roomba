from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.backend.serial import Serial
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

#robot = Root(Bluetooth())
#robot = Create3(Bluetooth())
robot = Serial('/dev/ttyACM0')
#robot=Create3(Bluetooth('MonicaRoomba'))


@event(robot.when_play)
async def play(robot):
    await robot.set_lights_on_rgb(25, 100, 255)
    battery = await robot.get_battery_level()
    print('Name:', await robot.get_name())
    print('Battery: ', battery[0], 'mV; ', battery[1], '%')
    print('Serial #:', await robot.get_serial_number())
    print('SKU:', await robot.get_sku())

robot.play()