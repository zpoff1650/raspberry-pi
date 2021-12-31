import microcontroller as mc
import board


mc.delay_us(1)

board_pins = []
for pin in dir(mc.pin):
    if isinstance(getattr(mc.pin, pin), mc.Pin):
        pins = []
        for alias in dir(board):
            if getattr(board, alias) is getattr(mc.pin, pin):
                pins.append("board.{}".format(alias))
                if len(pins) > 0:
                    board_pins.append("".join(pins))

for pins in sorted(board_pins):
    print(pins)