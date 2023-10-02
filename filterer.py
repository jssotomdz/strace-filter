import sys

f = open(sys.argv[1], "r")
lines = f.readlines()

lines = [line for line in lines if "/" in line]

for line in lines:
 line = line.split(" ")

relevant = [line for line in lines if "file" in line and "directory)" in line]

tokens = []
for line in relevant:
 i=0
 if len(line.split(" ")[i])>0:
  while "/" not in line.split(" ")[i] and i<len(line.split(" ")):
   i+=1
  token = line.split(" ")[i].split("/")[-1]
  if token[0:-2] not in tokens:
   tokens.append(token[0:-2])

tokens.remove("lib")
libtokens = [token for token in tokens if "lib" in token]

result = libtokens.copy()
for token in libtokens:
 hits = [line for line in lines if token in line]
 for hit in hits:
  if hit.split(" ")[-1].rstrip().isdigit():
   if token in result:
    result.remove(token)
print("Missing libraries:")
print(result)
