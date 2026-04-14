import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tut_bird_tx = pg.image.load("fig/3.png")
    tut_bird_rect = tut_bird_tx.get_rect() #練習10.1
    tut_bird_rect.center = 300,200 #練習10.2
    tmr = 0;movx=0;movy=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(pg.transform.flip(bg_img,1,0),[-x+1600,0])
        screen.blit(pg.transform.flip(bg_img,0,0),[-x+3200,0])
        screen.blit(pg.transform.flip(tut_bird_tx,1,0),tut_bird_rect) #10.5
        pg.display.update()
        tmr += 1        
        x += 1
        clock.tick(200)
        key_lst = pg.key.get_pressed() #練習10.3
        if key_lst[pg.K_UP]:
            movx += 0; movy += -1
        if key_lst[pg.K_DOWN]:
            movx += 0; movy += 1
        if key_lst[pg.K_LEFT]:
            movx += -1; movy += 0
        if key_lst[pg.K_RIGHT]:
            movx += 2; movy += 0
        tut_bird_rect.move_ip(-1+movx,0+movy) #移動
        movx = 0; movy = 0


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()