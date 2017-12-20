from itertools import takewhile
from sys import stdin

def parse_vec3(s):
	return list(map(int, s.strip("<>").split(",")))

def abs_vec3(v):
	return sum(map(abs, v))

lines = list(takewhile(len, map(str.strip, stdin)))

particle_data = [ { k : parse_vec3(v) for (k,v) in (t.split("=") for t in line.split(", ")) } for line in lines]
particle_abs_data = { i : { k : abs_vec3(data[k]) for k in data } for (i, data) in enumerate(particle_data) }

min_accel = min( abs_vec3(d['a']) for d in particle_data )
min_accel_particles = [ i for i in particle_abs_data if particle_abs_data[i]['a'] == min_accel ]

print([(i, particle_abs_data[i]) for i in min_accel_particles])
