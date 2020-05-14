## Kleuren veranderen

De standaardkleur voor de pen die door de schildpadcursor wordt gebruikt, is zwart en de standaardachtergrondkleur is wit. Je kunt de kleuren wijzigen om je vormen er nog beter uit te laten zien.

- Bekijk de onderstaande code. Het bevat drie variabelen genaamd `R`, `G`en `B`. 

<iframe src="https://trinket.io/embed/python/b964b7d3ce" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

Variabelen zijn een manier om een waarde op te slaan en een naam te geven. Er is bijvoorbeeld een variabelenaam `R` met een waarde van `255`.

De volgende regel is uitgecommentarieerd in de trinket hierboven, maar zal nodig zijn als je een andere editor gebruikt. Dus als je niet in Trinket werkt, verwijder je het `#` symbool om het uitcommentarieren van de regel ongedaan te maken.

    python
      screen.colormode(255)

- Voer de code uit en kijk wat er gebeurt.

- Probeer de waarden van de drie variabelen te wijzigen en kijk wat er gebeurt. (Opmerking: de maximale waarde is 255 en daarna heeft het geen effect meer.) Wat denk je dat R, G en B vertegenwoordigen?

--- collapse ---
---
title: Antwoord
---
`R`, `G` en `B` geven aan hoeveel rood, groen en blauw in de kleur worden gebruikt. Elk kan een waarde hebben van `0` tot `255`.

Dus om geel te maken, zou je het volgende kunnen proberen:

```python
R = 255
G = 255
B = 0
```

--- /collapse ---

[[[generic-theory-simple-colours]]]

Je kunt de waarde van je variabelen wijzigen door ze op een nieuwe waarde in te stellen of door ze te verhogen en te verlagen.

- Je kunt ook de kleur van de schildpad veranderen. Voer de onderstaande code uit om te zien wat er gebeurt: 

<iframe src="https://trinket.io/embed/python/ab6732d60e" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

### Uitdaging

Probeer elk van de onderstaande uitdagingen te voltooien.

- Voltooi de driehoek hierboven met een kleur naar keuze.
- Teken een vierkant met zijden die vier verschillende tinten rood zijn.
- Teken een kruis gemaakt van vier verschillende kleuren.

--- hints --- --- hint ---

Als je een kleur wilt wijzigen, kun je gewoon waarden bij de oorspronkelijke variabelen blijven optellen of aftrekken.

--- /hint --- --- hint ---

Je kunt dus de kleuren wijzigen door het volgende te doen:

```python
R = 255
G = 0
B = 0

turtle.color((R, G, B))
turtle.forward(100)
turtle.right(120)

R - = 20
G + = 20
B + = 5

turtle.color((R, G, B))
turtle.forward(100)
turtle.right(120)
```

--- /hint --- --- /hints ---