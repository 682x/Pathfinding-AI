import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
crashed = False

map = [['*'] for i in range(20)]
map.insert(0, ['*' for i in range(22)])
map.append(['*' for i in range(22)])
for i in range(1, 21):
    x = input()
    for j in x:
        map[i].append(j)
    map[i].append('*')
print(map)

def drawworld(world):
    for i in range(22):
        for j in range(22):
            if world[i][j] == '*':
                pygame.draw.rect(gameDisplay, (0, 0, 0), (j * 30, i * 30, 30, 30))
            elif world[i][j] == 'P':
                pygame.draw.rect(gameDisplay, (0, 0, 255), (j * 30, i * 30, 30, 30))
            elif world[i][j] == 'E':
                pygame.draw.rect(gameDisplay, (255, 0, 0), (j * 30, i * 30, 30, 30))
            elif world[i][j] == 'R':
                pygame.draw.rect(gameDisplay, (0, 255, 0), (j * 30, i * 30, 30, 30))


map[5][5] = 'P'
map[12][12] = 'E'


def pathing(world, ex, ey, px, py):
    q = [(ex, ey)]
    vis = [[False for i in range(22)] for i in range(22)]
    count = 0
    while len(q) != 0:
        for i in range(len(q)):
            cx = q[0][0]
            cy = q[0][1]
            vis[cx][cy] = True
            if world[cx][cy] == 'P':
                return True, count
            if world[cx + 1][cy] != '*' and vis[cx + 1][cy] is False:
                q.append((cx + 1, cy))
            if world[cx - 1][cy] != '*' and vis[cx - 1][cy] is False:
                q.append((cx - 1, cy))
            if world[cx][cy + 1] != '*' and vis[cx][cy + 1] is False:
                q.append((cx, cy + 1))
            if world[cx][cy - 1] != '*' and vis[cx][cy - 1] is False:
                q.append((cx, cy - 1))
            del q[0]
        count += 1
    return False, 0


def findpath(world, ex, ey, px, py, distance, vis):
    vis[ex][ey] = distance
    if distance < 0:
        return False, [(-1, -1)]
    if ex == px and ey == py and distance == 0:
        return True, [(ex, ey)]
    if world[ex + 1][ey] != '*' and distance - 1 > vis[ex + 1][ey]:
        found, route = findpath(world, ex + 1, ey, px, py, distance - 1, vis)
        if found is True:
            route.insert(0, (ex, ey))
            return True, route
    if world[ex - 1][ey] != '*' and distance - 1 > vis[ex - 1][ey]:
        found, route = findpath(world, ex - 1, ey, px, py, distance - 1, vis)
        if found is True:
            route.insert(0, (ex, ey))
            return True, route
    if world[ex][ey + 1] != '*' and distance - 1 > vis [ex][ey + 1]:
        found, route = findpath(world, ex, ey + 1, px, py, distance - 1, vis)
        if found is True:
            route.insert(0, (ex, ey))
            return True, route
    if world[ex][ey - 1] != '*' and distance - 1 > vis [ex][ey - 1]:
        found, route = findpath(world, ex, ey - 1, px, py, distance - 1, vis)
        if found is True:
            route.insert(0, (ex, ey))
            return True, route
    return False, [(-1, -1)]


canpath, dist = (pathing(map, 12, 12, 5, 5))
if canpath is True:
    owo, path = findpath(map, 12, 12, 5, 5, dist, [[-1 for i in range(22)] for i in range(22)])
    for i, j in path:
        if map[i][j] == ' ':
            map[i][j] = 'R'

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    #print(event)
    gameDisplay.fill((255, 255, 255))
    drawworld(map)

    pygame.display.update()
    clock.tick(60)

