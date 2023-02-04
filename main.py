from pygame import *

init()

# Stałe

BACKGROUND_COLOR = [700, 700]

PANEL_COLOR = (222, 184, 135)

DIALOGBOX_X_POSITION = 50
DIALOGBOX_Y_POSITION = 450
DIALOGBOX_POSITION = [(DIALOGBOX_X_POSITION, DIALOGBOX_Y_POSITION+200),
                      (DIALOGBOX_X_POSITION, DIALOGBOX_Y_POSITION),
                      (DIALOGBOX_X_POSITION+600, DIALOGBOX_Y_POSITION),
                      (DIALOGBOX_X_POSITION+600, DIALOGBOX_Y_POSITION+200)]

ALLAY_CHARACTER_PANEL_X_POSITION = 50
ALLAY_CHARACTER_PANEL_Y_POSITION = 50
ALLAY_CHARACTER_PANEL_POSITION = [(ALLAY_CHARACTER_PANEL_X_POSITION + 25, ALLAY_CHARACTER_PANEL_Y_POSITION),
                                  (ALLAY_CHARACTER_PANEL_X_POSITION, ALLAY_CHARACTER_PANEL_Y_POSITION + 50),
                                  (ALLAY_CHARACTER_PANEL_X_POSITION + 175, ALLAY_CHARACTER_PANEL_Y_POSITION + 50),
                                  (ALLAY_CHARACTER_PANEL_X_POSITION + 200, ALLAY_CHARACTER_PANEL_Y_POSITION)]

ENEMY_CHARACTER_PANEL_X_POSITION = 450
ENEMY_CHARACTER_PANEL_Y_POSITION = 275
ENEMY_CHARACTER_PANEL_POSITION = [(ENEMY_CHARACTER_PANEL_X_POSITION + 25, ENEMY_CHARACTER_PANEL_Y_POSITION),
                                  (ENEMY_CHARACTER_PANEL_X_POSITION, ENEMY_CHARACTER_PANEL_Y_POSITION + 50),
                                  (ENEMY_CHARACTER_PANEL_X_POSITION + 175, ENEMY_CHARACTER_PANEL_Y_POSITION + 50),
                                  (ENEMY_CHARACTER_PANEL_X_POSITION + 200, ENEMY_CHARACTER_PANEL_Y_POSITION)]

EMPTY_HP_COLOR = (152, 245, 255)
EMPTY_HP_BAR_WIDTH = 6
HP_COLOR = (138, 43, 226)

# Wielkość Ekranu

screen = display.set_mode(BACKGROUND_COLOR)

# Główna pętla

running = True

while running:

    # Wyłączanie gry

    for eve in event.get():

        if eve.type == QUIT:
            running = False

    # Tło

    screen.fill((0, 0, 0))

    # Przeciwnicy

    draw.circle(screen, (238, 59, 59), (550, 150), 75)
    draw.circle(screen, (152, 245, 255), (150, 350), 75)

    # Pasek Zagrzybienia

    draw.polygon(screen, PANEL_COLOR, ALLAY_CHARACTER_PANEL_POSITION)
    draw.line(screen, EMPTY_HP_COLOR,
              (ALLAY_CHARACTER_PANEL_X_POSITION+25, ALLAY_CHARACTER_PANEL_Y_POSITION+25),
              (ALLAY_CHARACTER_PANEL_X_POSITION+175, ALLAY_CHARACTER_PANEL_Y_POSITION+25),
              EMPTY_HP_BAR_WIDTH)

    draw.polygon(screen, PANEL_COLOR, ENEMY_CHARACTER_PANEL_POSITION)


    # Pasek dialogowy

    draw.polygon(screen, PANEL_COLOR, DIALOGBOX_POSITION)

    # Aktualizacja Ekranu

    display.flip()

# Wyjście for real

quit()
