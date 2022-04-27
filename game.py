import pygame, sys
from pygame.locals import *
from pygame import mixer

pygame.init()
mixer.init()
# Initialize pygame and music mixer

class GameArch:
    """
    A class containing the game's architecture. Primarily for overall view, but also contains
    controls and model for the game architecture itself.
    """

    click = False

    def __init__(self):
        """
        Init function for the GameArch class

        Attributes:
            _main_clock: private game clock for tick-keeping
            _main_font: private font representing 40pt Comic Sans
            _screen: private screen data
            _menu_music: private sound representing the main menu
            music .WAV file
            _game_music: private sound representing the game music
            .WAV file
            _music_channel: private music channel for playing music
            in
        """
        self._main_clock = pygame.time.Clock()
        # Game clock related attributes
        self._main_font = pygame.font.SysFont("Fonts/comic.ttf", 40)
        self._screen = pygame.display.set_mode((500, 500),0,32)
        # Graphics related attributes
        self._menu_music = pygame.mixer.Sound("Music/mainmenu.wav") 
        self._game_music = pygame.mixer.Sound("Music/pianoplaylist.wav")
        self._music_channel = pygame.mixer.Channel(0)
        # Music related attributes

    def draw_text(self, text, color, x, y):
        """
        A method for drawing text with pygame.

        Args:
            text: a string containing the text to be drawn.
            color: a tuple with three int values representing
            RGB color.
            x: integer representing the x position of the text.
            y: integer representing the x position of the text.
        """
        textobj = self._main_font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self._screen.blit(textobj, textrect)

    def main_menu(self):
        """
        A method representing the main menu of the game.
        """
        self._music_channel.play(self._menu_music, loops=-1, fade_ms=5000)
        # Play main menu music while main menu is loaded
        while True:

            self._screen.fill((137,207,240))
            self.draw_text('AMON(gus) Color Pooper', (0, 0, 0), 100, 130)
            self.draw_text('An artistic experience', (0, 0, 0), 100, 165)
            # Fill screen with color and make text

            mx, my = pygame.mouse.get_pos()
            # Create variables to allow for button click recognition
    
            button = pygame.Rect(150, 225, 200, 50)
            button_outside = button.inflate(2,2)
            pygame.draw.rect(self._screen, (0, 0, 0), button_outside)
            pygame.draw.rect(self._screen, (255, 255, 255), button)
            self.draw_text('Begin!', (0, 0, 0), 210, 238)
            if button.collidepoint((mx, my)):
                if click:
                    self.game()
            # Create button to start game

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            # Provide method for user to exit out of menu or enter the game

            pygame.display.update()
            self._main_clock.tick(60)
            # Create game clock

    def game(self):
        """
        A method representing the actual game itself.
        """
        self._music_channel.stop()
        self._music_channel.play(self._game_music, loops=-1, fade_ms=5000)
        # Stop old music and play piano playlist if game is loaded
        running = True
        while running:
            
            self._screen.fill((255,255,255))
            # Fill screen with color

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            # Provide method for user to exit out of game

            pygame.display.update()
            self._main_clock.tick(60)
            # Create game clock

if __name__ == "__main__":
    GameArch().main_menu()
# Initialize the game by starting the main menu
