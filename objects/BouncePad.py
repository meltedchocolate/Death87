"""
    Copyright 2015 Ricky LeDew

    This file is part of Death 87.

    Death 87 is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Death 87 is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import pygame
from Wall import *

class BouncePad(Wall):
    def __init__(self, x, y, width, height, color, friction, bounciness):

        Wall.__init__(self, x, y, width, height, color, friction, True)