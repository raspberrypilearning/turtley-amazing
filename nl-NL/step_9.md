## Loopy kleuren

Om interessantere kleuren te krijgen, kun je veel kleuren in een lange lijst schrijven en dan de kleur van de schildpad blijven veranderen in overeenstemming met de kleur van de lijst. Je kunt lijsten maken in Python, met vierkante haakjes `[]`.

Hieronder zie je een voorbeeld van een lijst met RGB-kleuren:

```python
colours = [(85, 211, 136), (197, 196, 126), (235, 233, 166), (25, 135, 222), (211, 64, 159), (159, 165, 106), (178, 160, 125), (36, 192, 70), (231, 184, 204), (63, 203, 219)]
```

- Dit volgende stukje wordt een beetje ingewikkeld. Bekijk de onderstaande code en voer deze uit om te zien wat er gebeurt. 

<iframe src="https://trinket.io/embed/python/d58123d315" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

De regel `turtle.color(colours[i])` vertelt het programma om het "`i`e" item in de lijst te kiezen. Vergeet niet dat `i` begint bij 0 en gaat tot 9.

- Wat als je een langere rij wilt? Probeer het aantal herhalingen in de `for` lus te wijzigen in `range(20)` en kijk wat er gebeurt. Krijg je een foutmelding?