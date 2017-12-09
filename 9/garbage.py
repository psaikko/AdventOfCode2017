line=input()

score = 0
garbage_length = 0

def parse_garbage(s, i):
	global garbage_length
	if s[i] != '<': raise "Expected < got " + s[i]
	j = i+1
	while j < len(s):
		if s[j] == '>':
			print("parsed garbage " + s[i:j+1])
			return j+1
		elif s[j] == '!':
			j += 1
		else:
			garbage_length += 1
		j += 1
	raise "Unterminated garbage"
	return j

def parse_group(s, i, d):
	global score
	score += d
	if s[i] != '{': raise "Expected { got " + s[i]
	start = i
	i += 1
	while i < len(s):
		if s[i] == '{':
			i = parse_group(s, i, d+1)
		elif s[i] == '}':
			print("parsed group " + s[start:i+1])
			return i+1
		elif s[i] == '<':
			i = parse_garbage(s, i)
		elif s[i] == ',':
			if s[i-1] not in "}>": raise ", after "+s[i-1]
			i += 1
		else:
			i += 1
	raise "Unterminated group"

parse_group(line, 0, 1)
print("score:", score)
print("garbage:", garbage_length)