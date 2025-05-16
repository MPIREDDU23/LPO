#!/usr/bin/env python3

s = "Linguaggi di programmazione 33.8999"

l = s.split()
titolo2 = ""
for i in range(len(l)-1):
    titolo2 = titolo2 + l[i]
    titolo2 += " "
titolo2 = titolo2[:-1]
print(titolo2)
prezzo = l[-1]
print(prezzo)

