## Herhaling

Het herhalen van coderegels is een van de snelste manieren om iets voor elkaar te krijgen. Heel vaak in de informatica is het logischer om coderegels te herhalen in plaats van een andere reeks instructies te schrijven. Het vierkant dat je eerder hebt gemaakt, gebruikt bijvoorbeeld vier keer dezelfde twee instructies. In plaats van ze vier keer uit te schrijven, zou je ze een keer kunnen uitschrijven, maar een instructie toevoegen om ze te herhalen.

In Python zijn er twee soorten lussen die je waarschijnlijk zult gebruiken: een lus van `while` en een lus van `for`. Als je wilt dat een gedeelte van de code voor altijd wordt herhaald, of totdat een voorwaarde is ingesteld, is een lus van `while` misschien het beste. Als je een bepaald aantal keren wilt lussen, heeft een `for` lus de voorkeur.

- Hier hebben we een `while True` lus gebruikt. Dit betekent dat de code in de lus (d.w.z. de ingesprongen code) voor altijd zal worden herhaald. Je kunt het proberen in Trinket om te zien wat het doet, maar vergeet niet dat het voor **altijd** doorgaat!
    
    ```python
    from turtle import Turtle, Screen
    
    turtle = Turtle()
    
    while True:
      turtle.forward(1)
      turtle.right(1)
    ```
    
    Dit type lus zal niet erg handig zijn voor het tekenen van vormen met Turtle waar je preciezer wilt zijn.

- In dit voorbeeld is een `for` lus gebruikt. Druk op **Run** om te zien wat er gebeurt. <iframe src="https://trinket.io/embed/python/b89b6f5457" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

Een `for` lus herhaalt instructies een bepaald aantal keren, in dit geval 8 keer. Een `for` lus heeft een bijbehorende variabele (hier `i` genoemd). In dit voorbeeld begint `i` vanaf `0` en neemt deze telkens met `1` toe. Laten we dit toepassen op de code om een vierkant te tekenen:

```python from turtle import Turtle, Screen

turtle = Turtle()

for i in range(4): turtle.forward(100) turtle.right(90) ```

- Kopieer en plak deze code in de Trinket-editor hierboven en voer deze uit. De schildpad is gevraagd om twee instructies vier keer te herhalen om een vierkant te maken.

- Nadat je met behulp van een lus een vorm hebt gemaakt, kun je de vorm steeds opnieuw herhalen door deze in een andere lus te plaatsen. Dit is een geweldige manier om spiralen te tekenen. Pas je code aan door deze er als volgt uit te laten zien:
    
    ```python
    from turtle import Turtle, Screen
    
    turtle = Turtle()
    
    for i in range(30):
      for i in range(4):
        turtle.forward(100)
        turtle.right(90)
      turtle.right(25)
    ```
    
    Een spiraal kan worden gemaakt door een kleine graad te draaien en vervolgens een kleine hoeveelheid vooruit te gaan. Het gedeelte met code voor het maken van een vierkant bevindt zich in een andere `for` lus die het 30 keer herhaalt, waarbij de cursor telkens 25 graden wordt gedraaid om een aangename spiraalvorm te maken.

### Uitdaging

Probeer elk van de onderstaande uitdagingen te voltooien.

- Kun je de `for` lus wijzigen zodat deze een interessantere spiraal trekt met één van de vormen die je eerder hebt gemaakt, zoals een driehoek of cirkel?

- Door een paar extra lijnen toe te voegen waar je de variabelen `R`, `G`en `B` wijzigt, kun je een veelkleurige spiraal maken. Probeer een regenboogspiraal te creëren.

--- hints --- 
--- hint ---

Net als in de vorige oefening kun je optellen bij of aftrekken van de variabelen `R`, `G`en `B`.

--- /hint --- --- hint ---

Wijzig gewoon de variabelen binnen de `for` lus:

```python
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

R = 255
G = 0
B = 124

for i in range(30):
turtle.color((R, G, B))
for i in range(4):
turtle.forward(100)
turtle.right(90)
##VOEG HIER IETS TOE
turtle.right(25)
```

--- /hint --- --- hint ---

Probeer dit om te beginnen:

```python
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

R = 255
G = 0
B = 124

for i in range(30):
turtle.color((R, G, B))
for i in range(4):
turtle.forward(100)
turtle.right(90)
R -= 1
G += 1
turtle.right(25)
```

--- /hint --- --- /hints ---