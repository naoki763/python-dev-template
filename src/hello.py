import os, sys  # ❌ import の並び順が不適切（isort ルール違反）

def add(x,y):return x+y  # ❌ 引数の間にスペースがない / 改行がない（PEP8違反）

def unused_function():  # ❌ 未使用の関数（F401 警告）
    pass

def   multiply(a ,  b ): # ❌ スペースの不一致
 return ab # ❌ インデントが不正

def long_function_name(x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x1, y1, z1):
    return x + y  # ❌ 長すぎる行（E501）

print( "Hello, World!" ) # ❌ 不要なスペース / クォートの統一が必要


def dev(a,b,c):return ab*c