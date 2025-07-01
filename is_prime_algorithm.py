zzz = [q for q in range(2, 100) if all(q % w for w in range(2, int(q**0.5) + 1))]
print(zzz[:10])