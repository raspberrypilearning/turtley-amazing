## Modulo komt te hulp

In het vorige voorbeeld heb je een manier nodig om door de lijstitems te blijven lopen, dus als `i` bij 9 komt, zal het teruggaan en het "0e" item uit de lijst opnieuw halen. Dit is waar de modulo-operator `%` je kan helpen.

- Bekijk de onderstaande code: voer deze uit en kijk of je kunt achterhalen wat er aan de hand is. Je moet om te beginnen `0` krijgen. <iframe src="https://trinket.io/embed/python/8fd77a1942" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

- Probeer de nummers in de opdracht `print` te veranderen. Hieronder volgen enkele voorbeelden:
    
    ```python
    print(17 % 6)
    print(12 % 6)
    print(13 % 6)
    print(6 % 6)
    print(0 % 6)
    print(1 % 6)
    print(8 % 6)
    print(11 % 6)
    ```

- Heb je het uitgevonden? De operator `%` drukt de rest van een deling af. Bijvoorbeeld, 15 ÷ 6 is 2 met een rest van 3. Daarom zou 15 % 6 dus 3 zijn. We kunnen deze operator gebruiken om te helpen met het probleem van het einde van de lijst. Als de `range` boven de lengte van de lijst uitkomt, kun je gewoon een `%` van de lengte van de lijst doen.

- Bekijk het onderstaande voorbeeld en lees de code zorgvuldig door om er zeker van te zijn dat je kunt zien hoe de modulo-operator wordt gebruikt. <iframe src="https://trinket.io/embed/python/c56b5cb705" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>