import sys

import pygame
from pygame.locals import *

# 使用pygame之前必须初始化
pygame.init()

screen: pygame.Surface = pygame.display.set_mode((1280, 720))
screen.fill('white')

# 设置窗口的标题，即游戏名称
pygame.display.set_caption('PyMines')

# 引入字体类型
f: pygame.font = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 50)
# 生成文本信息，第一个参数文本内容；第二个参数，字体是否平滑；
# 第三个参数，RGB模式的字体颜色；第四个参数，RGB模式字体背景颜色；
text: pygame.Surface = f.render('测试pygame基本功能~', True, (255, 0, 0), (0, 0, 0))
# 获得显示对象的rect区域坐标
textRect = text.get_rect()
# 设置对象居中
textRect.center = (630, 360)
# 将准备好的文本信息，绘制到主屏幕 Screen 上
screen.blit(text, textRect)

# 创建一个50*50的图像并优化显示
face = pygame.Surface((50, 50), flags=pygame.HWSURFACE)
face.fill(color='pink')

# 获得毫秒为单位德时间
# 该时间指的从pygame初始化后开始计算，到调用该函数为止
t = pygame.time.get_ticks()
# 暂停游戏3000毫秒
t1 = pygame.time.wait(1000)
print(t1)

# 加载一张图片
image_surface = pygame.image.load(
    'D:/VSCode Workspace/Python/PyMines/tests/t.jpg').convert()
# rect(left,top,width,height)指定图片上某个区域
# special_flags功能标志位,指定颜色混合模式，默认为 0 表示用纯色填充
image_surface.fill((0, 0, 255), rect=(100, 100, 100, 50), special_flags=0)
# 200,100 表示图像在水平、垂直方向上的偏移量，以左上角为坐标原点
image_surface.scroll(100, 50)
image_new = pygame.transform.scale(image_surface, (300, 300))
# 查看新生成的图片的对象类型
print(type(image_new))
# 对新生成的图像旋转45度
image_1 = pygame.transform.rotate(image_new, 45)
# 使用rotozoom旋转0渡，缩小0.5倍
image_2 = pygame.transform.rotozoom(image_1, 0, 0.7)

rect1 = pygame.Rect(50, 50, 100, 100)
# 在原图的基础上创建一个新的子图（surface对象）
image_sub = image_surface.subsurface(rect1)
rect2 = image_sub.get_rect()
print(rect2)

# 创建时钟对象（控制游戏的FPS）
clock = pygame.time.Clock()

# 固定代码段，实现点击"X"号退出界面的功能，几乎所有的pygame都会使用该段代码
while True:
    # 通过时钟对象，指定循环频率，每秒循环60次
    clock.tick(60)
    # 循环获取事件，监听事件状态
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            # 卸载所有模块
            pygame.quit()
            # 终止程序，确保退出程序
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('鼠标按下', event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            print('鼠标弹起', event.pos)
        if event.type == pygame.MOUSEMOTION:
            print('鼠标移动')
        # 键盘事件
        if event.type == pygame.KEYDOWN:
            print('键盘按下', chr(event.key))
        if event.type == pygame.KEYUP:
            print('键盘弹起')
    # 将绘制的图像添加到主屏幕上，(100,100)是位置坐标，显示屏的左上角为坐标系的(0,0)原点
    screen.blit(image_2, (150, 250))
    screen.blit(image_sub, rect1)
    # screen.blit(face, (100, 100))
    # screen.blit(image_surface, (0, 0))
    # 更新屏幕内容
    pygame.display.flip()
