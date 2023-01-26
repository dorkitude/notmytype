from globals import *

class Control(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        pygame.init()
        # Create the window
        self.screen = pygame.display.set_mode(window_size)

        self.active_sprites = pygame.sprite.Group()

        # Set the title
        pygame.display.set_caption("Matador Sandbox")

        # establish the hud
        # self.hud = Hud()

        # # make the player
        # player = Player(x=100, y=250)
        # sprites_to_render_second.add(player)
        # self.player = player
        # player.control = self

        # # make the starting weapons
        # player.halo = Halo(player, STARTING_HALO_RADIUS)
        # sprites_to_render_first.add(player.halo)

        # player.wand = MagicWand(player, self)

        # player.hurt_sound = pygame.mixer.Sound("sounds/ouch.wav")

    def update(self):
        pass

    def run(self):

        running = True
        while running:
            self.delay_between_frames()
            self.update()

    def delay_between_frames(self):
        pygame.time.delay(frame_duration)