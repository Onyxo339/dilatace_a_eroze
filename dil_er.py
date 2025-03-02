image2d = [[4 - max(abs(i - 4), abs(j - 4)) for j in range(9)] for i in range(9)]

def dil(image2d):
    height, width = len(image2d), len(image2d[0])
    new_image = [[0] * width for _ in range(height)]

    for i in range(height):
        for j in range(width):
            neighbors = [image2d[i][j]]
            if i > 0: neighbors.append(image2d[i-1][j])  # Top
            if i < height-1: neighbors.append(image2d[i+1][j])  # Bottom
            if j > 0: neighbors.append(image2d[i][j-1])  # Left
            if j < width-1: neighbors.append(image2d[i][j+1])  # Right

            new_image[i][j] = max(neighbors)  # Dilation uses max

    return new_image

def er(image2d):
    height, width = len(image2d), len(image2d[0])
    new_image = [[0] * width for _ in range(height)]

    for i in range(height):
        for j in range(width):
            neighbors = [image2d[i][j]]
            if i > 0: neighbors.append(image2d[i-1][j])  # Top
            if i < height-1: neighbors.append(image2d[i+1][j])  # Bottom
            if j > 0: neighbors.append(image2d[i][j-1])  # Left
            if j < width-1: neighbors.append(image2d[i][j+1])  # Right

            new_image[i][j] = min(neighbors)  # Erosion uses min

    return new_image

print("Original:")
for row in image2d:
    print(row)

print("Dilatace:")
dilated = dil(image2d)
for row in dilated:
    print(row)

print("Eroze:")
eroded = er(image2d)
for row in eroded:
    print(row)