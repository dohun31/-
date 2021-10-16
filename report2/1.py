"""
영상비전처리 과제 #2
201911900 백도훈 
2-1. 엠보싱 효과 프로그램
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'embossing'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def on_mask_processing(i, j):
    # 마스크 계산 값을 저장할 변수 s를 0으로 초기화
    s = 0
    for m in mask:
        for (di, dj), v in m:
            ci = i + di
            cj = j + dj
            if 0 <= ci < row and 0 <= cj < col:
                s += in_img[ci][cj] * v
    # overflow 방지
    if s > 255: s = 255
    elif s < 0: s = 0
    return s

def embossing_image():
    out_img = copy.deepcopy(in_img)
    # 마스크 프로세싱
    for i in range(row):
        for j in range(col):
            out_img[i][j] = on_mask_processing(i, j)
    return out_img

if __name__ == "__main__":
    mask = [
        [[(-1, -1), 1], [(-1, 0), 1], [(-1, 1), 1]],
        [[(0, -1), 1], [(0, 0), -8], [(0, 1), 1]],
        [[(1, -1), 1], [(1, 0), 1], [(1, 1), 1]]
    ]
    in_img, row, col = image_handler()
    out_img = embossing_image()
    show_result_image(out_img)