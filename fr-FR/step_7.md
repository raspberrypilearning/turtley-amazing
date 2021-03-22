## Répétition

La répétition de lignes de code est l'un des moyens les plus rapides d'accomplir quelque chose. Assez souvent en informatique, il est plus logique de répéter des lignes de code plutôt que d'écrire un autre ensemble d'instructions. Par exemple, le carré que tu as créé précédemment utilise les deux mêmes instructions quatre fois. Plutôt que de les écrire quatre fois, tu peux les écrire une fois, mais en ajoutant une instruction pour les répéter.

En Python, il existe deux types de boucles que tu es susceptible d'utiliser: une boucle `while` et une boucle `for`. Si tu veux qu'une section de code se répète indéfiniment, ou jusqu'à ce qu'une condition soit définie, une boucle `while` peut être la meilleure. Si tu souhaites effectuer une boucle un certain nombre de fois, une `for` est préférable.

- Ici, nous avons utilisé une boucle `while True`. Cela signifie que le code à l'intérieur de la boucle (c'est-à-dire le code qui est indenté) se répétera pour toujours. Tu peux l'essayer dans Trinket pour voir ce qu'il fait, mais n'oublie pas qu'il va boucler **pour toujours**!
    
    ```python
    from turtle import Turtle, Screen
    
    turtle = Turtle()
    
    while True:
      turtle.forward(1)
      turtle.right(1)
    ```
    
    Ce type de boucle ne sera pas très utile pour dessiner des formes avec Turtle où tu souhaites être plus précis.

- Dans cet exemple, une boucle `for` a été utilisée. Appuie sur **Exécuter** pour voir ce qui se passe. <iframe src="https://trinket.io/embed/python/b89b6f5457" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

Une boucle `for` répète des instructions un nombre défini de fois, dans ce cas 8 fois. Une boucle `for` a une variable associée (appelée ici `i` ). Dans cet exemple, `i` part de `0` et augmente de `1` à chaque fois. Appliquons ceci au code pour dessiner un carré:

```python from turtle import Turtle, Screen

turtle = Turtle()

for i in range(4): turtle.forward(100) turtle.right(90) ```

- Copie et colle ce code dans l'éditeur Trinket ci-dessus et exécute-le. On a demandé à la tortue de répéter deux instructions quatre fois pour faire un carré.

- Une fois que tu as créé une forme en utilisant une boucle, tu peux répéter la forme encore et encore en la plaçant dans une autre boucle. C'est un excellent moyen de dessiner des spirales. Adapte ton code en le faisant ressembler à ceci :
    
    ```python
    from turtle import Turtle, Screen
    
    turtle = Turtle()
    
    for i in range(30):
      for i in range(4):
          turtle.forward(100)
          turtle.right(90)
      turtle.right(25)
    ```
    
    Une spirale peut être faite en tournant un petit degré, puis en avançant un peu. La section de code pour créer un carré se trouve à l'intérieur d'une autre `for` qui la répète 30 fois, chaque fois en tournant le curseur de 25 degrés pour créer une jolie forme en spirale.

### Défi

Essaye de relever chacun des défis ci-dessous.

- Peux-tu modifier la boucle `for` pour qu'elle dessine une spirale plus intéressante en utilisant l'une des formes que tu as faites plus tôt, comme un triangle ou un cercle?

- Ajoute quelques lignes supplémentaires où tu modifieras les variables `R`, `G`, et `B` pour te permettre de faire une spirale multicouleurs. Essaye de créer une spirale arc-en-ciel.

\--- hints \--- \--- hint \---

Tout comme dans l'exercice précédent, tu peux ajouter ou soustraire aux variables `R`, `G` et `B`.

\--- /hint \--- \--- hint \---

Modifie simplement les variables dans la boucle `for`:

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
        ##ADD SOMETHING HERE
    turtle.right(25)
```

\--- /hint \--- \--- hint \---

Essaye ceci pour commencer :

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

\--- /hint \--- \--- /hints \---