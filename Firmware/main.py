print("Starting")

import busio
import board

from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D6, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.VOLU, KC.VOLD, KC.MUTE,
     KC.PGUP, KC.UP, KC.PGDOWN,
     KC.LEFT, KC.DOWN, KC.RIGHT ]
]

encoder_handler.pins = (
    (board.D8, board.D9, None),
    )
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.NO),),
]

i2c_bus = busio.I2C(board.D5, board.D4)
driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    display=driver,
    width=128,
    height=32,
    entries = [
    TextEntry(text="Layer = 1", x=0, y=0),
    TextEntry(text="Macros", x=0, y=12),
    TextEntry(text="Hey there!", x=0, y=24),
]
)
keyboard.extensions.append(display)

rgb = RGB(pixel_pin=board.D10, num_pixels=9)
keyboard.extensions.append(rgb)




if __name__ == '__main__':
    keyboard.go()