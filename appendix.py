# speed sin and cos 
# global scope score 

# FROM THE PYGAME DOCUMENTATION / GEEKSFORGEEKS for random module 

# pygame.init
# initialize all imported pygame modules

# pygame.quit
# uninitialize all pygame modules

# sys.exit()
# system.exit()

# pygame.display.set_mode
# Initialize a window or screen for display

# pygame.display.set_caption
# Set the current window caption

# pygame.time.Clock
# create an object to help track time

# pygame.font.SysFont
# create a Font object from the system fonts

# The randrange() method returns a randomly selected element from the specified range.
# random.randrange(start, stop, step)

# The randint() method returns an integer number selected element from the specified range.
# This method is an alias for randrange(start, stop+1)
# random.randint(start, stop)

# pygame.mouse.get_pos()
# get the mouse cursor position
# get_pos() -> (x, y)
# Returns the x and y position of the mouse cursor. The position is relative to the top-left corner of the display. 
# The cursor position can be located outside of the display window, but is always constrained to the screen.

# pygame.draw.rect()
# draw a rectangle
# rect(surface, color, rect) -> Rect
# rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1) -> Rect
# Draws a rectangle on the given surface.
# Parameters
# surface (Surface) -- surface to draw on
# color (Color or int or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])
# rect (Rect) -- rectangle to draw, position and dimensions
# width (int) --
# (optional) used for line thickness or to indicate that the rectangle is to be filled (not to be confused with the width value of the rect parameter)
# if width == 0, (default) fill the rectangle
# if width > 0, used for line thickness
# if width < 0, nothing will be drawn
# border_radius (int) -- (optional) used for drawing rectangle with rounded corners. The supported range is [0, min(height, width) / 2], with 0 representing a rectangle without rounded corners.
# border_top_left_radius (int) -- (optional) used for setting the value of top left border. If you don't set this value, it will use the border_radius value.
# border_top_right_radius (int) -- (optional) used for setting the value of top right border. If you don't set this value, it will use the border_radius value.
# border_bottom_left_radius (int) -- (optional) used for setting the value of bottom left border. If you don't set this value, it will use the border_radius value.
# border_bottom_right_radius (int) --
#(optional) used for setting the value of bottom right border. If you don't set this value, it will use the border_radius value.
# if border_radius < 1 it will draw rectangle without rounded corners
# if any of border radii has the value < 0 it will use value of the border_radius
# If sum of radii on the same side of the rectangle is greater than the rect size the radii
# will get scaled
# Returns
# a rect bounding the changed pixels, if nothing is drawn the bounding rect's position will be the position of the given rect parameter and its width and height will be 0
# Return type
# Rect


# pygame.draw.line()
# draw a straight line
# line(surface, color, start_pos, end_pos) -> Rect
# line(surface, color, start_pos, end_pos, width=1) -> Rect
# Draws a straight line on the given surface. There are no endcaps. For thick lines the ends are squared off.
# Parameters
# surface (Surface) -- surface to draw on
# color (Color or int or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])
# start_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- start position of the line, (x, y)
# end_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- end position of the line, (x, y)
# width (int) --
# (optional) used for line thickness
# if width >= 1, used for line thickness (default is 1)
# if width < 1, nothing will be drawn
# Note When using width values > 1, lines will grow as follows.
# For odd width values, the thickness of each line grows with the original line being in the center.
# For even width values, the thickness of each line grows with the original line being offset from the center (as there is no exact center line drawn). As a result, lines with a slope < 1 (horizontal-ish) will have 1 more pixel of thickness below the original line (in the y direction). Lines with a slope >= 1 (vertical-ish) will have 1 more pixel of thickness to the right of the original line (in the x direction).
# Returns
# a rect bounding the changed pixels, if nothing is drawn the bounding rect's position will be the start_pos parameter value (float values will be truncated) and its width and height will be 0
# Return type
# Rect
# Raises
# TypeError -- if start_pos or end_pos is not a sequence of two numbers



# pygame.draw.ellipse()
# draw an ellipse
# ellipse(surface, color, rect) -> Rect
# ellipse(surface, color, rect, width=0) -> Rect
# Draws an ellipse on the given surface.
# Parameters
# surface (Surface) -- surface to draw on
# color (Color or int or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])
# rect (Rect) -- rectangle to indicate the position and dimensions of the ellipse, the ellipse will be centered inside the rectangle and bounded by it
# width (int) --
# (optional) used for line thickness or to indicate that the ellipse is to be filled (not to be confused with the width value of the rect parameter)
# if width == 0, (default) fill the ellipse
# if width > 0, used for line thickness
# if width < 0, nothing will be drawn
# Note When using width values > 1, the edge lines will only grow inward from the original boundary of the rect parameter.
# Returns
# a rect bounding the changed pixels, if nothing is drawn the bounding rect's position will be the position of the given rect parameter and its width and height will be 0
# Return type
# Rect
# Changed in pygame 2.0.0: Added support for keyword arguments.


# blit()
# draw one image onto another
# blit(source, dest, area=None, special_flags=0) -> Rect
# Draws a source Surface onto this Surface. The draw can be positioned with the dest argument. The dest argument can either be a pair of coordinates representing the position of the upper left corner of the blit or a Rect, where the upper left corner of the rectangle will be used as the position for the blit. The size of the destination rectangle does not effect the blit.
# An optional area rectangle can be passed as well. This represents a smaller portion of the source Surface to draw.
# The return rectangle is the area of the affected pixels, excluding any pixels outside the destination Surface, or outside the clipping area.
# Pixel alphas will be ignored when blitting to an 8 bit Surface.
# For a surface with colorkey or blanket alpha, a blit to self may give slightly different colors than a non self-blit.


# pygame.event.get()
# get events from the queue
# get(eventtype=None) -> Eventlist
# get(eventtype=None, pump=True) -> Eventlist
# get(eventtype=None, pump=True, exclude=None) -> Eventlist
# This will get all the messages and remove them from the queue. If a type or sequence of types is given only those messages will be removed from the queue and returned.
# If a type or sequence of types is passed in the exclude argument instead, then all only other messages will be removed from the queue. If an exclude parameter is passed, the eventtype parameter must be None.
# If you are only taking specific events from the queue, be aware that the queue could eventually fill up with the events you are not interested.
# If pump is True (the default), then pygame.event.pump()internally process pygame event handlers will be called.


# fill()
# fill Surface with a solid color
# fill(color, rect=None, special_flags=0) -> Rect
# Fill the Surface with a solid color. If no rect argument is given the entire Surface will be filled. The rect argument will limit the fill to a specific area. The fill will also be contained by the Surface clip area.
# The color argument can be either a RGB sequence, a RGBA sequence or a mapped color index. If using RGBA, the Alpha (A part of RGBA) is ignored unless the surface uses per pixel alpha (Surface has the SRCALPHA flag).
# This will return the affected Surface area.


# pygame.display.update()
# Update portions of the screen for software displays
# update(rectangle=None) -> None
# update(rectangle_list) -> None
# This function is like an optimized version of pygame.display.flip() for software displays. It allows only a portion of the screen to be updated, instead of the entire area. If no argument is passed it updates the entire Surface area like pygame.display.flip().
# Note that calling display.update(None) means no part of the window is updated. Whereas display.update() means the whole window is updated.
# You can pass the function a single rectangle, or a sequence of rectangles. It is more efficient to pass many rectangles at once than to call update multiple times with single or a partial list of rectangles. If passing a sequence of rectangles it is safe to include None values in the list, which will be skipped.
# This call cannot be used on pygame.OPENGL displays and will generate an exception.


# tick()
# update the clock
# tick(framerate=0) -> milliseconds
# This method should be called once per frame. It will compute how many milliseconds have passed since the previous call.
# If you pass the optional framerate argument the function will delay to keep the game running slower than the given ticks per second. This can be used to help limit the runtime speed of a game. By calling Clock.tick(40) once per frame, the program will never run at more than 40 frames per second.
# Note that this function uses SDL_Delay function which is not accurate on every platform, but does not use much CPU. Use tick_busy_loop if you want an accurate timer, and don't mind chewing CPU.


    def draw(self):
        pygame.draw.line(window, DARKBLUE, (self.x + self.a/2, self.y + self.b), (self.x + self.a/2, self.y + self.b + self.length))
        pygame.draw.ellipse(window, self.color, (self.x, self.y, self.a, self.b))
        pygame.draw.ellipse(window, self.color, (self.x + self.a/2 - 5, self.y + self.b -3, 10, 10))