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


def gameover(screen: pg.Surface) -> None:  # 演習問題1
    # 1. 黒い矩形を描画するための空のSurfaceを作り，黒い矩形を描画する
    black_surf = pg.Surface((WIDTH, HEIGHT))
    black_surf.fill((0, 0, 0))
    # 2. 1のSurfaceの透明度を設定する
    black_surf.set_alpha(200)
    # 3. 白文字でGame Overと書かれたフォントSurfaceを作り，1のSurfaceにblitする
    fonto = pg.font.Font(None, 100)
    txt = fonto.render("Game Over", True, (255, 255, 255))
    txt_rct = txt.get_rect()
    # 4. こうかとん画像をロードし，こうかとんSurfaceを作り，1のSurfaceにblitする
    cry_img = pg.transform.rotozoom(pg.image.load("fig/8.png"), 0, 1.0)
    cry_rct = cry_img.get_rect()
    # 文字とこうかとんを左右中央に配置するコード
    total_width = cry_rct.width + 100 + txt_rct.width + 100 + cry_rct.width
    start_x = (WIDTH - total_width) // 2
    center_y = HEIGHT // 2
    left_x = start_x
    left_y = center_y - cry_rct.height // 2
    black_surf.blit(cry_img, (left_x, left_y))
    txt_x = left_x + cry_rct.width + 100
    txt_y = center_y - txt_rct.height // 2
    black_surf.blit(txt, (txt_x, txt_y))
    right_x = txt_x + txt_rct.width + 100
    right_y = center_y - cry_rct.height // 2
    black_surf.blit(cry_img, (right_x, right_y))
    # 5. 1のSurfaceをscreen Surfaceにblitする
    screen.blit(black_surf, (0, 0))
    # 6. pg.display.update()したら，time.sleep(5)する
    pg.display.update()
    pg.time.wait(5000)



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
            
        # if kk_rct.colliderect(bb_rct):  #練習問題4 こうかとんと爆弾が衝突したら
        #     print("ゲームオーバー")  #練習問題4
        #     return  #練習問題4
        
        if kk_rct.colliderect(bb_rct):  #演習課題1
            gameover(screen)  #演習課題1
            return  #演習課題1

        
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