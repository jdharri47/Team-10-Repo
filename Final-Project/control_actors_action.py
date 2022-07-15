import constants
from action import Action
from point import Point
from tank import Tank


class ControlActorsAction(Action):
    """
    An input action that controls the tank.
    
    The responsibility of ControlActorsAction is to get the direction and move the tanks.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction_one = Point(constants.CELL_SIZE, 0)
        self._direction_two = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # first tank up
        if self._keyboard_service.is_key_down('w'):
            self._direction_one = Point(0, -constants.CELL_SIZE)
        
        # first tank down
        if self._keyboard_service.is_key_down('s'):
            self._direction_one = Point(0, constants.CELL_SIZE)
            
        #frist tank fire
        if self._keyboard_service.is_key_down('f'):
            
          
        # second tank up
        if self._keyboard_service.is_key_down('u'):
            self._direction_two = Point(0, -constants.CELL_SIZE)
        
        # second tank down
        if self._keyboard_service.is_key_down('j'):
            self._direction_two = Point(0, constants.CELL_SIZE)
            
        # second tank fire
        if self._keyboard_service.is_key_down('l'):

        tank_one = cast.get_first_actor("tank1")
       
        tank_two = cast.get_first_actor("tank2")
        