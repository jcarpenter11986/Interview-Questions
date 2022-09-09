def initialize_array(n):
  array = []
  for i in range (n):
    row = []
    for j in range (n):
      row.append(0)
    array.append(row)
  return array

def spiral_matrix(n):
  array = initialize_array(n)

  ctr = 0

  top = 0
  bottom = n
  left = 0
  right = n

  while ctr < n * n:
    # fill top from right to left
    for col in range(left, right):
      array[top][col] = ctr
      ctr += 1
    top += 1

    # fill right from top to bottom
    for row in range(top, bottom):
      array[row][right - 1] = ctr
      ctr += 1
    right -= 1

    # fill bottom from right to left
    for col in reversed(range(left, right)):
      array[bottom - 1][col] = ctr
      ctr += 1
    bottom -= 1

    # fill left from bottom to top
    for row in reversed(range(top, bottom)):
      array[row][left] = ctr
      ctr += 1
    left += 1

  for i in range(len(array)):
    print(array[i])


n = 5
spiral_matrix(n)