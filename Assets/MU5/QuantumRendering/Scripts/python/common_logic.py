import numpy as np

# //＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
def gray_code(n):
    """nビットのグレイコードを生成する関数"""
    if n == 0:
        return ['']
    smaller_gray_code = gray_code(n - 1)
    return ['0' + code for code in smaller_gray_code] + ['1' + code for code in reversed(smaller_gray_code)]


def gray_code_2d(w, h):
    """w x h の2次元グレイコードを生成する関数"""
    log2_w = (w-1).bit_length()
    log2_h = (h-1).bit_length()
    
    # グレイコードの生成
    gray_codes_x = gray_code(log2_w)
    gray_codes_y = gray_code(log2_h)
    
    # 結果を保存する配列
    gray_code_matrix = [['' for _ in range(w)] for _ in range(h)]
    
    for y in range(0,h):
        for x in range(0,w):
            s_xy = gray_codes_x[x] + gray_codes_y[y]
            gray_code_matrix[y][x] = s_xy
            
    return gray_code_matrix


def gray_to_binary(gray):
    binary = gray[0]  # 最上位ビットをそのまま使用
    for i in range(1, len(gray)):
        # 前のビットと現在のグレイコードのビットとの排他的論理和を取る
        binary += str(int(binary[i-1]) ^ int(gray[i]))
    return binary

def binary_to_decimal(binary):
    return int(binary, 2)

def gray_to_decimal(gray):
    binary = gray_to_binary(gray)
    decimal = binary_to_decimal(binary)
    return decimal

def create_matrix(w,h):
    return [[0 for j in range(w)] for i in range(h)]

# //ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
def clamp(value, value_min, value_max):
    return max(value_min, min(value, value_max))

# //ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
def get_normalizeCoefficient(matrix):
    val = 0
    w = len(matrix[0])
    h = len(matrix)
    for y in range(h):
        for x in range(w):
            val += np.sqrt(matrix[y][x]/255)
    return 1/np.sqrt(val)

def get_normalizedImage(matrix):
    w = len(matrix[0])
    h = len(matrix)
    arr = create_matrix(w,h)
    for y in range(h):
        for x in range(w):
            arr[y][x] = np.sqrt(matrix[y][x]/255)
    return np.array(arr)