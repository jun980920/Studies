import pygame
pygame.init() 


screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width, screen_height))


pygame. display.set_caption("Nado Game")
#FPS-클락 함수 생성
clock=pygame.time.Clock()
background=pygame.image.load('C:\\Users\\ces30_x16wgwl\\Desktop\\아나\\background.png')
character=pygame.image.load('C:\\Users\\ces30_x16wgwl\\Desktop\\아나\\jerry.png')


character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2-character_width/2
character_y_pos=screen_height-character_size[1]


#이동할 좌표
to_x=0
to_y=0
#프레임이 달라진다고 이동속도가 달라져선 안된다.

#character_speed
charcter_speed=0.6
running=True
#enemy

enemy=pygame.image.load('C:\\Users\\ces30_x16wgwl\\Desktop\\아나\\tom.png')


enemy_size=enemy.get_rect().size
enemy_width=enemy_size[0]
enemy_height=enemy_size[1]
enemy_x_pos=screen_width/2-enemy_width/2
enemy_y_pos=screen_height/2-enemy_height/2








#글자 활용
#폰트정의
game_font=pygame.font.Font(None, 40)

#총 시간 정하기(게임시간)
total_time=10

#시작 시간 정보 입력
start_ticks=pygame.time.get_ticks()

while running:
    #게임화면의 프레임수 설정, 델타에 저장
    dt=clock.tick(100)
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running= False

        if event.type==pygame.KEYDOWN:#키가 눌려졌냐
            if event.key==pygame.K_LEFT:#캐릭터를 왼쪽으로
                to_x-=charcter_speed
            elif event.key==pygame.K_RIGHT:#캐릭터를 오른쪽으로
                to_x+=charcter_speed
            elif event.key==pygame.K_UP:#캐릭터를 위로
                to_y-=charcter_speed
            elif event.key==pygame.K_DOWN:#캐릭터를 아래로
                to_y+=charcter_speed
        if event.type==pygame.KEYUP:#방향키를 떼면 멈춤
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0
    
    #캐릭터 좌표 갱신
    character_x_pos+=to_x*dt
    character_y_pos+=to_y*dt
    

    #경계값 처리
    if character_x_pos<0:
        character_x_pos=0
    if character_x_pos>480-character_width:
        character_x_pos=480-character_width
    if character_y_pos<0:
        character_y_pos=0
    if character_y_pos>640-character_height:
        character_y_pos=640-character_height
        
    #충돌처리
    #각각의 정보 최신화
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos
    enemy_rect=enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos
    
    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print('충돌했어요')
        running=False
    screen.blit(background,(0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    #타이머 집어넣기
    #경과 시간 계산
    elapsed_time=(pygame.time.get_ticks()-start_ticks)/1000
    timer=game_font.render(str(int(total_time-elapsed_time)), True, (0, 0, 0))
    screen.blit(timer, (10, 10))
    if int(total_time-elapsed_time)<0:
        print('time out')
        running=False
    #출력할  글자, True, 글자색상
    pygame.display.update() 
pygame.time.delay(2000)
pygame.quit()