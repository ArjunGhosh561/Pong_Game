import pygame, sys, random


def ball_animation():
    global ball_speed_x, ball_speed_y,player_score,opponent_score,score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score+=1
        score_time=pygame.time.get_ticks()



    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        opponent_score+=1
        score_time = pygame.time.get_ticks()


    if ball.colliderect(player) and ball_speed_x>0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right-player.left)<10:
            ball_speed_x *= -1
        elif abs(ball.bottom-player.top)<10 and  ball_speed_y>0:
            ball_speed_y*=-1

        elif abs(ball.top-player.bottom)<10 and ball_speed_y<0:
            ball_speed_y*=-1
            ball_speed_x*=-1



    if ball.colliderect(opponent) and  ball_speed_x<0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left-opponent.right)<10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1

        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
            ball_speed_x *= -1




def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
def opponent_ai():
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_start():
    global ball_speed_x,ball_speed_y,score_time
    current_time=pygame.time.get_ticks()
    ball.center=(screen_width/2,screen_height/2)
    if current_time-score_time<700:
        num_three=game_font.render("3",False,light_grey)
        screen.blit(num_three,(screen_width/2,screen_height/2+20))
    if  700< current_time-score_time<1400:
        num_two = game_font.render("2", False, light_grey)
        screen.blit(num_two, (screen_width / 2, screen_height / 2 + 20))
    if 1400<    current_time-score_time<2100:
        num_one = game_font.render("1", False, light_grey)
        screen.blit(num_one, (screen_width / 2, screen_height / 2 + 20))


    if current_time-score_time<2100:
        ball_speed_x,ball_speed_y=0,0
    else:
        ball_speed_y=7*random.choice((1,-1))
        ball_speed_x =7*random.choice((1,-1))
        score_time=None






pygame.init()

clock = pygame.time.Clock()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PONG")

bg_color = pygame.Color('gray40')
light_grey = (200, 200, 200)
ball_color=pygame.Color(240,248,255)
index_color=pygame.Color(184,184,184)
orange=pygame.Color(255,127,0)
red=pygame.Color((220,20,60))

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 50, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(30, screen_height / 2 - 70, 10, 140)

ball_speed_x = 5.5*random.choice((1,-1))
ball_speed_y = 5.5*random.choice((1,-1))
player_speed = 0
opponent_speed=7
player_score=0
opponent_score=0
game_font=pygame.font.Font("freesansbold.ttf",32)

score_time=True
pong_sound=pygame.mixer.Sound("pong.ogg")
score_sound=pygame.mixer.Sound("score.ogg")


while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7



    ball_animation()
    player_animation()
    opponent_ai()

    screen.fill(bg_color)
    pygame.draw.rect(screen, orange, player)
    pygame.draw.rect(screen, orange, opponent)
    pygame.draw.ellipse(screen, ball_color, ball)
    pygame.draw.aaline(screen, orange, (screen_width / 2, 0), (screen_width / 2, screen_height))

    if score_time:
        ball_start()

    index_1 = game_font.render("YOU",False,index_color)
    screen.blit(index_1,(525,400))
    player_text=game_font.render(f"{player_score}",False,light_grey)
    screen.blit(player_text,(555,475))
    index_2 = game_font.render("COMP", False, index_color)
    screen.blit(index_2, (380, 400))
    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (435, 475))



    pygame.display.flip()
    clock.tick(60)
