#-*- coding:utf-8 -*-
import pygame, random

pygame.init()

imagesize = 30

class Missile:
    def __init__(self, screen, cx, cy, tx, ty):
        self.screen = screen
        self.x = cx + 10
        self.y = cy + 10
        self.vx = tx - cx
        self.vy = ty - cy
        self.check = False
        self.mImage = pygame.image.load("picture/missile.png")
        self.mImage = pygame.transform.scale(self.mImage, (int(10), int(10)))
        self.mVector = pygame.math.Vector2(self.vx, self.vy)
        self.mVector = pygame.math.Vector2.normalize(self.mVector)

    def update(self):
        global widthSize, heightSize
        self.x += self.mVector[0]
        self.y += self.mVector[1]
        if self.x < 0 or self.y < 0:
            self.check = True
        if self.x > widthSize or self.y > heightSize:
            self.check = True

    def draw(self):
        mRect = self.mImage.get_rect()
        mRect = mRect.fit((self.x, self.y, 50, 50))
        self.screen.blit(self.mImage, mRect)

class Enemy:
    def __init__(self, screen, ex, ey, tx, ty):
        self.screen = screen
        self.x = ex
        self.y = ey
        self.vx = tx - ex
        self.vy = ty - ey
        self.mImage = pygame.image.load("picture/enemy1.png")
        self.mImage = pygame.transform.scale(self.mImage, (int(30), int(30)))
        self.mVector = pygame.math.Vector2(self.vx, self.vy)
        self.mVector = pygame.math.Vector2.normalize(self.mVector)

    def update(self):
<<<<<<< HEAD

        global widthSize, heightSize , imagesize
        self.x += self.mVector[0]
        self.y += self.mVector[1]
        if self.y < 0 or self.y > heightSize-imagesize:
            self.mVector = pygame.math.Vector2(self.vx,-self.vy)
            self.mVector = pygame.math.Vector2.normalize(self.mVector)
        if self.x < 0 or self.x > widthSize - imagesize:
            self.mVector = pygame.math.Vector2(-self.vx, self.vy)
            self.mVector = pygame.math.Vector2.normalize(self.mVector)

=======
        global widthSize, heightSize
        self.x += self.mVector[0]
        self.y += self.mVector[1]
        if self.x < 0 or self.y < 0:
            self.check = True
        if self.x > widthSize or self.y > heightSize:
            self.check = True
>>>>>>> 8b11ec416427a11f7606b34c9364d8b5d19bee63

    def draw(self):  #나중에 부모클래스 하나 만들어서 상속받아도 될듯
        mRect = self.mImage.get_rect()
        mRect = mRect.fit((self.x, self.y, 50, 50))
        self.screen.blit(self.mImage, mRect)

<<<<<<< HEAD


=======
>>>>>>> 8b11ec416427a11f7606b34c9364d8b5d19bee63
#----------------------------------## 게임 기본 설정 관련 ##---------------------------------------


#게임 전체 스크린 사이즈
widthSize = 500
heightSize = 400


#게임 스크린 사이즈와 게임 제목 설정
game_screen = pygame.display.set_mode((widthSize,heightSize))
pygame.display.set_caption("test")

#오디오 출력용
pygame.mixer.music.load('sound/ponyo.wav')
pygame.mixer.music.play(0)

#-----------------------------------## 게임 관련 함수 ##---------------------------------------


def show_img(ourScreen, img_name, x_Position,y_Position) :
    myimg = pygame.image.load(img_name)
    ourScreen.blit(myimg, (x_Position, y_Position))


def show_text(ourScreen,text,x_Position, y_Position):
    text_Font = pygame.font.Font("freesansbold.ttf", 20)
    textSurface = text_Font.render(text, True, (0, 100, 0))
    ourScreen.blit(textSurface, (x_Position, y_Position))


#-----------------------------------## 게임 사용 변수 ##---------------------------------------

#키보드 이동용 전역변수 초기위치지정용도
x = widthSize/2
y = heightSize/2


finish = False
Page = 1

missileList = []
enemyList = []

makeEnemy = False
#-----------------------------------## 게임 로직 시작 ##---------------------------------------
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    pressd = pygame.key.get_pressed()  # 키 이벤트
    gametime = int(pygame.time.get_ticks()) #게임 타이머

    if Page == 1:  #초기화면
        game_screen.fill((200, 200, 0))  # 배경색

        # 텍스트 출력용
        show_text(game_screen, "Gamestart", 100, 100)

        # 임시로 준것
        if pressd[pygame.K_UP]:   Page = 2




    elif Page == 2: #게임 시작화면
        game_screen.fill((0, 200, 0))  #배경색

        if pressd[pygame.K_RIGHT]:
<<<<<<< HEAD
            if x < widthSize-imagesize:     x += 5
        elif pressd[pygame.K_LEFT]:
            if x > 0:                       x -= 5
        elif pressd[pygame.K_UP]:
            if y > 0:                       y -= 5
        elif pressd[pygame.K_DOWN]:
            if y < heightSize-imagesize:    y += 5
=======
            if x < widthSize-30:
                x += 5
        if pressd[pygame.K_LEFT]:
            if x > 0:
                x -= 5
        if pressd[pygame.K_UP]:
            if y > 0:
                y -= 5
        if pressd[pygame.K_DOWN]:
            if y < heightSize-30:
                y += 5
>>>>>>> 8b11ec416427a11f7606b34c9364d8b5d19bee63

        # 임시로 준것
        if pressd[pygame.K_p]:   Page = 3


        show_img(game_screen, "picture/airplane.png", x, y)


        if pressd[pygame.K_SPACE]:
            missile = Missile(game_screen, x, y, x, y-1)
            missileList.append(missile)

        for m in missileList:
            m.update()
            m.draw()
            if m.check == True:
                missileList.remove(m)

        if makeEnemy == False:
            for i in range(10):
<<<<<<< HEAD
                random_x = random.randrange(0, widthSize-imagesize)
                random_y = random.randrange(0, heightSize - imagesize)
                enemy = Enemy(game_screen,random_x, random_y, x, y)  #200,200 은 방향을 지정하는거니깐 내쪽으로 움직이게 해야겠다
=======
                random_x = random.randrange(0, widthSize-30)
                random_y = random.randrange(0, heightSize - 30)
                enemy = Enemy(game_screen,random_x, random_y, 200, 200)
>>>>>>> 8b11ec416427a11f7606b34c9364d8b5d19bee63
                enemyList.append(enemy)

            makeEnemy = True

        for m in enemyList:
            m.update()
            m.draw()




        # 텍스트 출력용
        show_text(game_screen, "Gametime : " + str(gametime), 10, 10)




    elif Page == 3: #엔딩 화면
        game_screen.fill((200, 200, 200))  # 배경색
        show_text(game_screen, "GameOver", 100, 100)


    pygame.display.flip() #프레임 갱신