import pygame

window_size = (1024, 768)

# Set the frame rate
frame_rate = 60
frame_duration = int(1000 / frame_rate)

# define a function to get the current time, in milliseconds
def now():
  return pygame.time.get_ticks()

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

# Set the more complex colors
dark_gray = (50, 50, 50)
light_gray = (200, 200, 200)
dark_red = (150, 0, 0)
dark_green = (0, 150, 0)
dark_blue = (0, 0, 150)
dark_yellow = (150, 150, 0)
dark_cyan = (0, 150, 150)
dark_magenta = (150, 0, 150)

