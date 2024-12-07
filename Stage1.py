import game_world
from Cube import Cube
from checkpoint import Checkpoint
from block import Block
from jump_pad import Jump_Pad
from jump_ring import Jump_Ring
from spike import Spike


def load_stage1():
    #cube = Cube(3, 1)
    cube = Cube(16,6)
    game_world.add_object(cube, 2)

    checkpoint = Checkpoint(12, 6)
    game_world.add_object(checkpoint, 1)

    blocks = [
        Block(23, 1), Block(23, 2), Block(23, 3), Block(20, 5), Block(1, 4),
        Block(16, 5), Block(12, 5), Block(8, 5), Block(5, 7), Block(3, 6),
        Block(3, 11), Block(10, 5), Block(14, 5), Block(18, 5), Block(14, 6),
        Block(10, 6), Block(22, 10), Block(24, 6), Block(8, 9), Block(8, 13),
        Block(18, 10), Block(14, 11), Block(7, 9), Block(1, 13)
    ]
    game_world.add_objects(blocks, 1)

    spikes = [
        Spike(6, 1, "up"), Spike(11, 1, "up"), Spike(12, 1, "up"), Spike(17, 1, "up"), Spike(18, 1, "up"),
        Spike(19, 1, "up"), Spike(22, 1, "left"), Spike(22, 2, "left"), Spike(22, 3, "left"),
        Spike(24, 1, "right"), Spike(24, 2, "right"), Spike(24, 3, "right"), Spike(6, 7, "right"),
        Spike(3, 7, "up"), Spike(3, 10, "down"), Spike(18, 6, "up"), Spike(14, 7, "up"), Spike(10, 7, "up"),
        Spike(19, 5, "right"), Spike(15, 5, "right"), Spike(11, 5, "right"), Spike(17, 5, "left"),
        Spike(13, 5, "left"), Spike(9, 5, "left"), Spike(9, 6, "left"), Spike(11, 6, "right"),
        Spike(24, 5, "down"), Spike(1, 3, "down"), Spike(2, 11, "left"), Spike(1, 12, "down"),
        Spike(8, 12, "down"), Spike(3, 12, "up"), Spike(7, 10, "up"), Spike(6, 9, "left")
    ]
    game_world.add_objects(spikes, 1)

    jump_rings = [Jump_Ring(1, 8, "red"), Jump_Ring(5, 12, "yellow")]
    game_world.add_objects(jump_rings, 1)

    jump_pads = [Jump_Pad(20, 1, "red"), Jump_Pad(1, 5, "red"), Jump_Pad(8, 6, "pink")]
    game_world.add_objects(jump_pads, 1)

    return cube, blocks, spikes, jump_rings, jump_pads, checkpoint
