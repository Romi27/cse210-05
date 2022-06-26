import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        
    def set_keys(self, players, index):
        player = players[index]
        keyboard = player.get_keyboard()
        left = keyboard[0]
        right = keyboard[1]
        up = keyboard[2]
        down = keyboard[3]
        # left
        if self._keyboard_service.is_key_down(left):
                self._direction = Point(-constants.CELL_SIZE, 0)
        
         # right
        if self._keyboard_service.is_key_down(right):
            self._direction = Point(constants.CELL_SIZE, 0)
            
        # up
        if self._keyboard_service.is_key_down(up):
            self._direction = Point(0, -constants.CELL_SIZE)
            
        # down
        if self._keyboard_service.is_key_down(down):
            self._direction = Point(0, constants.CELL_SIZE)
            
        player.turn_head(self._direction)



    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        players = [cast.get_first_actor("player1"), cast.get_first_actor("player2")]
        for i in range(2):
            index = i
            self.set_keys(players, index)
