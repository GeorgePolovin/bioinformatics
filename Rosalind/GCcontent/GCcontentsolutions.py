import time

'''
dna = {}

while True:
  try:
    line = input()
    if line[0] == '>':
      label = line[1:]
      dna[label] = ""
    else:
      dna[label] += line
  except EOFError:
    break

def gc_content(e):
  l, s = e
  return 100 * (s.count('G') + s.count('C')) / len(s)

e = max(dna.items(), key=gc_content)
print(e[0])
print(gc_content(e))
'''

t0=time.time()

f = open('rosalind_gc.txt', 'r')

max_gc_name, max_gc_content = '', 0

buf = f.readline().rstrip()
while buf:
    seq_name, seq = buf[1:], ''
    buf = f.readline().rstrip()
    while not buf.startswith('>') and buf:
        seq = seq + buf
        buf = f.readline().rstrip()
    seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
    if seq_gc_content > max_gc_content:
        max_gc_name, max_gc_content = seq_name, seq_gc_content

print('%s\n%.6f%%'% (max_gc_name, max_gc_content * 100))
f.close()

t1=time.time()

print(t1-t0)
