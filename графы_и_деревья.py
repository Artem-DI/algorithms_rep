#1) поиск в глубину

'''graph = {'0': set(['1', '2']),
'1': set(['0', '3', '4']),
'2': set(['0']),
'3': set(['1']),
'4': set(['2', '3'])}

def dfs(graph, start, visited = []):
	visited.append(start)
	for v in graph[start]:
		if v not in visited:
			visited = dfs(graph, v, visited)
	return visited

print(dfs(graph, '3'))'''



#2)

'''m = [2,5,12,0,4,7,43,235,65,9]

def sort(m):
	for i in range(len(m)):
		j = i - 1
		n = m[i]
		while m[j] > n and j >= 0:
			m[j+1] = m[j]
			j -= 1
		m[j + 1] = n
	return m
print(sort(m))'''


#3)бинарный поиск

''''l = [5,2,0,12,67,864,3,10,8,24,85,1]
l.sort()
a = int(input('Введите число:\n'))

def bs(l, a):
	lower = 0
	upper = len(l) - 1
	while (lower <= upper):
		median = (lower+upper)//2
		if l[median] == a:
			return median
		elif l[median] > a:
			upper = median - 1
		else:
			lower = median + 1
	return None

print()
print(l)
print()
print(bs(l, a))'''


#4)поиск в ширину

'''graph = {'0': set(['1', '2', '3']),
         '1': set(['0', '4', '5']),
         '2': set(['0', '5', '6']),
         '3': set(['0', '4', '5', '6']),
         '4': set(['1', '3', '7']),
         '5': set(['1', '2', '3', '7']),
         '6': set(['2', '3', '7']),
         '7': set(['4', '5', '6'])}


queue = []

def search_in_width(graph, start, visited = []):
    visited.append(start)
    queue.append(start)

    while queue:
    	m = queue.pop(0)
    	print(m, end = " ")

    	for i in graph[m]:
    		if i not in visited:
    			visited.append(i)
    			queue.append(i)

print(search_in_width(graph, '3'))'''