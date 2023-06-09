import numpy as np
import random


# Generate Key and Compress to 56 Bits (Left and Right)
key = np.zeros(64, dtype=int)


for i in range(64):
  key[i] = random.randint(0, 1)


f_key = np.zeros(56, dtype=int)
c = 0
for i in range(64):
  if (i + 1) % 8 == 0:
    continue
  else:
    f_key[c] = key[i]
    c += 1
print(f_key)
lo_key = f_key[:28]
ro_key = f_key[28:56]


# 64 Bit Plaintext to Binary
b_m = np.zeros(64)
strng = "hello123"
print("The original string is : " + strng)
re = ''.join(format(ord(i), '08b') for i in strng)


for i in range(len(re)):
  b_m[i] = int(re[i])


#Initial permutation of Plain Text
initial_perm = np.array([58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7])


p_text = np.zeros(64)


for i in range(64):
  p_text[i] = b_m[initial_perm[i] - 1]


# Right and Left Plain Text
lpt = p_text[:32]
rpt = p_text[32:64]


n_pt = np.zeros(64)


rolls = [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1]


for x in rolls:


  # Roll Keys by 1 and combine to form 56 bit
  l_key = np.roll(lo_key, rolls[x])
  r_key = np.roll(ro_key, rolls[x])


  key = np.concatenate((l_key, r_key))


  # RPT 32 to 48 bit Expansion
  exp_d = [32, 1, 2, 3, 4, 5, 4, 5,
          6, 7, 8, 9, 8, 9, 10, 11,
          12, 13, 12, 13, 14, 15, 16, 17,
          16, 17, 18, 19, 20, 21, 20, 21,
          22, 23, 24, 25, 24, 25, 26, 27,
          28, 29, 28, 29, 30, 31, 32, 1]


  e_text = np.zeros(48)


  for i in range(48):
    e_text[i] = rpt[exp_d[i] - 1]


  # Compress Key 56 bits to 48bits
  key_comp = [14, 17, 11, 24, 1, 5,
              3, 28, 15, 6, 21, 10,
              23, 19, 12, 4, 26, 8,
              16, 7, 27, 20, 13, 2,
              41, 52, 31, 37, 47, 55,
              30, 40, 51, 45, 33, 48,
              44, 49, 39, 56, 34, 53,
              46, 42, 50, 36, 29, 32]


  c_key = np.zeros(48)


  for i in range(48):
    c_key[i] = key[key_comp[i] - 1]


  # XOR of RPT And Key
  res = np.zeros(48)


  for i in range(48):
    res[i] = int(c_key[i]) ^ int(e_text[i])


  # S-Box Substitution
  sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
 
          [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
 
          [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
 
          [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
 
          [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
 
          [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
 
          [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
 
          [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]


  resu = []


  for i in range(0,8):
    j = i*6
    row = "{}".format(int(10*res[j]+res[j+5]))
    col = "{}".format(int(1000*res[j+1]+100*res[j+2]+10*res[j+3]+res[j+4]))
    row = int(row,2)
    col = int(col,2)
    number = format(sbox[i][row][col], '04b')
    for digit in str(number):
      resu.append(int(digit))


  # P-box permutation
  pbox = [16,  7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2,  8, 24, 14,
        32, 27,  3,  9,
        19, 13, 30,  6,
        22, 11,  4, 25]


  aprp = np.zeros(32)


  for i in range(32):
    aprp[i] = resu[pbox[i] - 1]


  n_rpt = np.zeros(32)


  for i in range(32):
    n_rpt[i] = int(aprp[i]) ^ int(lpt[i])


  lpt = rpt
  rpt = n_rpt
  n_pt = np.concatenate((lpt, rpt))


# Final Permutation Table
final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]


fet = np.zeros(64)
for i in range(64):
    fet[i] = n_pt[final_perm[i] - 1]
print(fet)


for i in range(0,8):
    j = i*8
    num = "{}".format(int(10000000*fet[j]+1000000*fet[j+1]+100000*fet[j+2]+10000*fet[j+3]+1000*fet[j+4]+100*fet[j+5]+10*fet[j+6]+fet[j+7]))
    print(chr(int(num, 2)),end='')
