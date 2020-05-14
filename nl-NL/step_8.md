## Betere spiralen

- Lees de onderstaande code eens door en raad eens wat het doet. Voer het vervolgens uit om te zien of je gelijk hebt. <iframe src="https://trinket.io/embed/python/8f98ccf1fa" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

- Het eerste wat je waarschijnlijk zal opvallen is dat dit eeuwen gaat duren om uit te voeren. We kunnen de zaken echter een beetje versnellen. Voeg de volgende regel toe, vóór de `for` lus:
    
    ```python
    turtle.speed(0)
    ```

- Voer de code opnieuw uit: deze zou iets sneller moeten zijn.

- Onze code heeft een veelkleurige spiraal gemaakt door de variabelen `R`, `G`en `B` te veranderen. De kleuren zijn echter een beetje eendimensionaal. Kun jij het beter doen?