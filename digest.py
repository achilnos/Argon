

fd = open('spinel.txt')
count = 0

A = []
for line in fd.readlines():
  A.append([])
  for word in line.split('\t'):
    intensity = float(word)
    A[-1].append(intensity)

print "Dimension: %d x %d" % (len(A), len(A[0]))

print "A = ["
for i in range(len(A)):
  print " ", A[i]
print "]"

for i in range(len(A)):
  for j in range(len(A[i])):
    pass # Do whatever  


