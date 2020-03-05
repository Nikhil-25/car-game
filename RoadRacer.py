import sys
import pygame
import time
import random
pygame.init()
gray = (119, 118, 110)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 200)
bright_blue = (0, 0, 255)
bright_red = (255, 0, 0)
display_width = 800
display_height = 600
crash_sound = pygame.mixer.Sound("crash.wav")

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Road Racer")
clock = pygame.time.Clock()
image = pygame.image.load('car1.jpg')
backgroundimg = pygame.image.load('grass.jpg')
yellow_strip = pygame.image.load('yellow.jpg')
strip = pygame.image.load('strip1.jpg')
intro_background = pygame.image.load('background.jpg')
instruction_background = pygame.image.load('instruction.jpg')
car_width = 64
pause = True


def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gameDisplay.blit(intro_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("ROAD RACER", largetext)
        TextRect.center = (400, 100)
        gameDisplay.blit(TextSurf, TextRect)
        button("START", 150, 520, 100, 50, green, bright_green, "play")
        button("QUIT", 550, 520, 100, 50, red, bright_red, "quit")
        button("INSTRUCTION", 300, 520, 200, 50, blue, bright_blue, "intro")
        pygame.display.update()
        clock.tick(50)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textsurf, textrect = text_objects(msg, smalltext)
        textrect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(textsurf, textrect)
        if click[0] == 1 and action is not None:
            if action == "play":
                countdown()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit
            elif action == "intro":
                introduction()
            elif action == "menu":
                intro_loop()
            elif action == "pause":
                paused()
            elif action == "unpaused":
                unpaused()

    else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
            smalltext = pygame.font.Font("freesansbold.ttf", 20)
            textsurf, textrect = text_objects(msg, smalltext)
            textrect.center = ((x+(w/2)), (y+(h/2)))
            gameDisplay.blit(textsurf, textrect)


def introduction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gameDisplay.blit(instruction_background, (0, 0))
        large_text = pygame.font.Font("freesansbold.ttf", 80)
        small_text = pygame.font.Font("freesansbold.ttf", 20)
        medium_text = pygame.font.Font("freesansbold.ttf", 40)
        textSurf, textRect = text_objects("IN THIS CAR GAME USER NEED TO DODGE THE COMING CARS", small_text)
        textRect.center = (350, 200)
        TextSurf, TextRect = text_objects("INSTRUCTION", large_text)
        textRect.center = (400, 100)
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(textSurf, textRect)
        stextSurf, stextRect = text_objects("ARROW LEFT : LEFT TURN", small_text)
        stextRect.center = (150, 400)
        htextSurf, htextRect = text_objects("ARROW RIGHT : RIGHT TURN", small_text)
        htextRect.center = (150, 450)
        atextSurf, atextRect = text_objects("A : ACCELERATION", small_text)
        atextRect.center = (150, 500)
        rtextSurf, rtextRect = text_objects("B : BRAKE ", small_text)
        rtextRect.center = (150, 550)
        ptextSurf, ptextRect = text_objects("P : PAUSE", small_text)
        ptextRect.center = (150, 350)
        sTextSurf, sTextRect = text_objects("CONTROLS", medium_text)
        sTextRect.center = (350, 300)
        gameDisplay.blit(stextSurf, stextRect)
        gameDisplay.blit(htextSurf, htextRect)
        gameDisplay.blit(atextSurf, atextRect)
        gameDisplay.blit(rtextSurf, rtextRect)
        gameDisplay.blit(ptextSurf, ptextRect)
        gameDisplay.blit(sTextSurf, sTextRect)
        button("BACK", 600, 450, 100, 50, blue, bright_blue, "menu")
        pygame.display.update()
        clock.tick(30)


def paused():
    global pause

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gameDisplay.blit(intro_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("PAUSED", largetext)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("CONTINUE", 150, 450, 150, 50, green, bright_green, "unpaused")
        button("RESTART", 350, 450, 150, 50, blue, bright_blue, "play")
        button("MAIN MENU", 550, 450, 200, 50, red, bright_red, "menu")
        pygame.display.update()
        clock.tick(30)


def unpaused():
    global pause
    pause = False


def countdown_background():
    font = pygame.font.SysFont(None, 25)
    x = (display_width*0.45)
    y = (display_height*0.8)
    gameDisplay.blit(backgroundimg, (0, 0))
    gameDisplay.blit(backgroundimg, (0, 200))
    gameDisplay.blit(backgroundimg, (0, 400))
    gameDisplay.blit(backgroundimg, (700, 0))
    gameDisplay.blit(backgroundimg, (700, 200))
    gameDisplay.blit(backgroundimg, (700, 400))
    gameDisplay.blit(yellow_strip, (400, 0))
    gameDisplay.blit(yellow_strip, (400, 100))
    gameDisplay.blit(yellow_strip, (400, 200))
    gameDisplay.blit(yellow_strip, (400, 300))
    gameDisplay.blit(yellow_strip, (400, 400))
    gameDisplay.blit(yellow_strip, (400, 500))
    gameDisplay.blit(strip, (100, 0))
    gameDisplay.blit(strip, (100, 100))
    gameDisplay.blit(strip, (100, 200))
    gameDisplay.blit(strip, (100, 300))
    gameDisplay.blit(strip, (100, 400))
    gameDisplay.blit(strip, (660, 0))
    gameDisplay.blit(strip, (660, 100))
    gameDisplay.blit(strip, (660, 200))
    gameDisplay.blit(strip, (660, 300))
    gameDisplay.blit(strip, (660, 400))
    gameDisplay.blit(image, (x, y))
    text = font.render("passed: 0", True, black)
    score = font.render("score: 0", True, red)
    gameDisplay.blit(text, (0, 50))
    gameDisplay.blit(score, (0, 30))
    button("pause", 650, 0, 150, 50, blue, bright_blue, "pause")


def countdown():
    countdown = True

    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gameDisplay.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("3", largetext)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        gameDisplay.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("2", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        gameDisplay.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("1", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        gameDisplay.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("GO!!!", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        game_loop()





def obstacle(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load("obs1.jpg")
    elif obs == 1:
        obs_pic = pygame.image.load("obs2.jpg")
    elif obs == 2:
        obs_pic = pygame.image.load("obs3.jpg")
    gameDisplay.blit(obs_pic, (obs_startx, obs_starty))


def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    message_display("YOU CRASHED")


def background():
    gameDisplay.blit(backgroundimg, (0, 0))
    gameDisplay.blit(backgroundimg, (0, 200))
    gameDisplay.blit(backgroundimg, (0, 400))
    gameDisplay.blit(backgroundimg, (700, 0))
    gameDisplay.blit(backgroundimg, (700, 200))
    gameDisplay.blit(backgroundimg, (700, 400))
    gameDisplay.blit(yellow_strip, (400, 0))
    gameDisplay.blit(yellow_strip, (400, 100))
    gameDisplay.blit(yellow_strip, (400, 200))
    gameDisplay.blit(yellow_strip, (400, 300))
    gameDisplay.blit(yellow_strip, (400, 400))
    gameDisplay.blit(yellow_strip, (400, 500))
    gameDisplay.blit(strip, (100, 200))
    gameDisplay.blit(strip, (100, 300))
    gameDisplay.blit(strip, (100, 400))
    gameDisplay.blit(strip, (660, 0))
    gameDisplay.blit(strip, (660, 100))
    gameDisplay.blit(strip, (660, 200))
    gameDisplay.blit(strip, (660, 300))
    gameDisplay.blit(strip, (660, 400))


def score_system(passed, score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("passed"+str(passed), True, black)
    score = font.render("score"+str(passed), True, red)
    gameDisplay.blit(text, (0, 50))
    gameDisplay.blit(score, (0, 30))


def car(x, y):
    gameDisplay.blit(image, (x, y))


def game_loop():
    global pause
    pygame.mixer.music.load('jazz.wav')
    pygame.mixer.music.play(-1)
    x = (display_width*0.45)
    y = (display_height*0.75)
    x_change = 0
    obstacle_speed = 9
    obs = random.randrange(0, 4)
    y_change = 0
    obs_startx = random.randrange(200, (display_width-200))
    obs_starty = -750
    obs_width = 56
    obs_height = 150
    level = 0
    score = 0
    passed = 0
    y2 = 7
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                x_change = -5
              if event.key == pygame.K_RIGHT:
                x_change = 5
              if event.key == pygame.K_a:
                obstacle_speed += 2
              if event.key == pygame.K_b:
                obstacle_speed -= 2
            if event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

        x += x_change
        gameDisplay.fill(gray)
        rel_y = y2 % backgroundimg.get_rect().width
        gameDisplay.blit(backgroundimg, (0, rel_y-backgroundimg.get_rect().width))
        gameDisplay.blit(backgroundimg, (700, rel_y - backgroundimg.get_rect().width))
        if rel_y<800:
            gameDisplay.blit(backgroundimg, (0, rel_y))
            gameDisplay.blit(backgroundimg, (700, rel_y))
            gameDisplay.blit(yellow_strip, (400, rel_y-100))
            gameDisplay.blit(yellow_strip, (400, rel_y))
            gameDisplay.blit(yellow_strip, (400, rel_y+100))
            gameDisplay.blit(yellow_strip, (400, rel_y+200))
            gameDisplay.blit(yellow_strip, (400, rel_y+300))
            gameDisplay.blit(yellow_strip, (400, rel_y+400))
            gameDisplay.blit(yellow_strip, (400, rel_y+500))
            gameDisplay.blit(strip, (100, rel_y + 200))
            gameDisplay.blit(strip, (100, rel_y + 100))
            gameDisplay.blit(strip, (100, rel_y + 300))
            gameDisplay.blit(strip, (100, rel_y))
            gameDisplay.blit(strip, (100, rel_y - 100))
            gameDisplay.blit(strip, (100, rel_y-200))
            gameDisplay.blit(strip, (100, rel_y-300))
            gameDisplay.blit(strip, (100, rel_y-400))
            gameDisplay.blit(strip, (100, rel_y - 500))
            gameDisplay.blit(strip, (660, rel_y + 100))
            gameDisplay.blit(strip, (660, rel_y + 200))
            gameDisplay.blit(strip, (660, rel_y + 300))
            gameDisplay.blit(strip, (660, rel_y))
            gameDisplay.blit(strip, (660, rel_y - 100))
            gameDisplay.blit(strip, (660, rel_y-200))
            gameDisplay.blit(strip, (660, rel_y-300))
            gameDisplay.blit(strip, (660, rel_y-400))
            gameDisplay.blit(strip, (660, rel_y - 500))

        y2 += obstacle_speed

        obs_starty -= (obstacle_speed/4)
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed
        car(x, y)
        score_system(passed, score)
        if x > 660-car_width or x < 100:
            crash()
        if x > display_width-(car_width+100) or x < 100:
            crash()
        if obs_starty > display_height:
            obs_starty = 0-obs_height
            obs_startx = random.randrange(170, (display_width-170))
            obs = random.randrange(0, 1)
            passed = passed+1
            score = passed*10
            if int(passed) % 10 == 0:
                level = level+1
                obstacle_speed+2
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf, textrect = text_objects("LEVEL"+str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                gameDisplay.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y<obs_starty+obs_height:
            if x>obs_startx and x<obs_startx+obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()
        button("pause", 650, 0, 150, 50, blue, bright_blue, "pause")
        pygame.display.update()
        clock.tick(60)


intro_loop()
game_loop()
pygame.quit()
quit()
