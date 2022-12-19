def add_X(pt):
  ind = 0
  while (ind < len(pt)):
    l1 = pt[ind]
    if ind == len(pt) - 1:
      if len(pt) % 2 != 0:
        pt = pt + 'X'
        ind += 2
      else:
        ind += 1
      continue
    
    l2 = pt[ind+1]
    if l1 == l2:
      pt = pt[:ind+1] + 'X' + pt[ind+1:]
    ind += 1
  return pt

def create_matrix(key):
  mat = [[0 for i in range(5)] for j in range(5)]
  row = 0
  col = 0
  letters_added = []

  # add the key to the matrix
  for letter in key:
    if letter not in letters_added:
      mat[row][col] = letter
      letters_added.append(letter)
    else:
      continue
    
    if col == 4:
      col = 0
      row += 1
    else:
      col += 1
  
  # add other letter in matrix A=65,....,Z=90
  for letter in range(65,91):
    if letter == 74: #letter is j which is equal to i so ignore
      continue
    
    if chr(letter) not in letters_added:
      letters_added.append(chr(letter))
    
  ind = 0
  for i in range(5):
    for j in range(5):
      mat[i][j] = letters_added[ind]
      ind += 1
    
  return mat

def indexof(letter, mat):
  if ord(letter) == 74:
    letter = 'I'
  
  for row in range(5):
    try:
      col = mat[row].index(letter)
      return (row, col)
    except:
      continue

def encryptdecrypt(pt, matrix, isDecrypt):
  inc = 1
  if isDecrypt:
    inc = -1
  
  ct = ''
  
  for (i,j) in zip(pt[0::2], pt[1::2]):
    r1, c1 = indexof(i, matrix)
    r2, c2 = indexof(j, matrix)

    if c1 == c2:
      ct += matrix[(r1+inc)%5][c1] + matrix[(r2+inc)%5][c2]
    elif r1 == r2:
      ct += matrix[r1][(c1+inc)%5] + matrix[r2][(c2+inc)%5]
    else:
      ct += matrix[r1][c2] + matrix[r2][c1]
  
  return ct



pt = input("Enter pt(capital): ")
key = input("Enter key(capital): ")

pt = add_X(pt)
print("After adding X in required places\nThe plain text is:",pt,'\n')
matrix = create_matrix(key=key)
print("The  matrix is:")
for row in matrix:
  print(row)

ct = encryptdecrypt(pt, matrix, isDecrypt=False)
print("After Encryption\nThe cipher text is:",ct)

pt = encryptdecrypt(ct , matrix, isDecrypt=True)
print("After Decryption\nThe plain text is:",pt)
