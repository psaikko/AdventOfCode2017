dirs = {'n':(0,1,-1),'ne':(1,0,-1),'se':(1,-1,0),'s':(0,-1,1),'sw':(-1,0,1),'nw':(-1,1,0)}
path = list(map(dirs.__getitem__, input().split(',')))
print(max(max(map(abs,(map(sum,zip(*path[:i]))))) for i in range(1,1+len(path))))