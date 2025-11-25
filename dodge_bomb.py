import os
import random  #練習問題2
import sys
import pygame as pg


WIDTH, HEIGHT = 1100, 650
DELTA = {  #練習問題1
    pg.K_UP: (0, -5),  #練習問題1
    pg.K_DOWN: (0, +5),  #練習問題1
    pg.K_LEFT: (-5, 0),  #練習問題1
    pg.K_RIGHT: (+5, 0),  #練習問題1
}
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def check_bound(rct: pg.Rect)-> tuple[bool, bool]:  #練習問題3
    """
    引数：こうかとんRectかばくだんRect
    戻り値：判定結果タプル（横方向の判定結果，縦方向の判定結果）
    画面内ならTrue，画面外ならFalse
    """
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:  #練習問題3  横方向のはみ出しチェック
        yoko = False  #練習問題3
    if rct.top < 0 or HEIGHT < rct.bottom:  #練習問題3  縦方向のはみ出しチェック
        tate = False  #練習問題3
    return yoko, tate  #練習問題3


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    bb_img = pg.Surface((20, 20))  #練習問題2  空のSurface
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  #練習問題2
    bb_img.set_colorkey((0, 0, 0))  #練習問題2
    bb_rct = bb_img.get_rect()  #練習問題2  爆弾Rect
    bb_rct.centerx = random.randint(0, WIDTH)  #練習問題2
    bb_rct.centery = random.randint(0, HEIGHT)  #練習問題2
    vx, vy = +5, +5  #練習問題2  爆弾の横速度、縦速度
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        # if key_lst[pg.K_UP]:
        #     sum_mv[1] -= 5
        # if key_lst[pg.K_DOWN]:
        #     sum_mv[1] += 5
        # if key_lst[pg.K_LEFT]:
        #     sum_mv[0] -= 5
        # if key_lst[pg.K_RIGHT]:
        #     sum_mv[0] += 5
        for key, mv in DELTA.items():  #練習問題1
            if key_lst[key]:  #練習問題1
                sum_mv[0] += mv[0]  #練習問題1　横方向の移動量
                sum_mv[1] += mv[1]  #練習問題1　横方向の移動量
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):  #練習問題2  画面外なら
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])  #練習問題2  移動しなかったことにする
        screen.blit(kk_img, kk_rct)  #練習問題2
        yoko, tate = check_bound(bb_rct)  #練習問題3
        if not yoko:  #練習問題3
            vx *= -1  #練習問題3
        if not tate:  #練習問題3
            vy *= -1  #練習問題3
        bb_rct.move_ip(vx, vy)  #練習問題2
        screen.blit(bb_img, bb_rct)  #練習問題2
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()