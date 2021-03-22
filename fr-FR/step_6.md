## Changer de couleurs

La couleur par défaut du crayon utilisé par le curseur tortue est le noir et la couleur d'arrière-plan par défaut est le blanc. Tu peux changer les couleurs pour rendre tes formes encore plus belles.

- Regarde le code ci-dessous. Il contient trois variables appelées `R`, `G` et `B`. <iframe src="https://trinket.io/embed/python/b964b7d3ce" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

Les variables sont un moyen de stocker une valeur et de lui donner un nom. Par exemple, il existe une variable avec le nom `R` qui contient une valeur de `255`.

La ligne suivante est commentée dans le trinket ci-dessus, mais sera nécessaire si tu utilises un autre éditeur. Donc, si tu ne travailles pas dans Trinket, supprime le symbole `#` , pour décommenter la ligne.

    python
      screen.colormode (255)

- Exécute le code et regarde ce qui se passe.

- Essaye de changer les valeurs des trois variables, et vois ce qui se passe. (Remarque: la valeur maximale est de 255, et après cela, il n'y aura aucun effet.) Que penses-tu que R, G et B représentent?

## \--- collapse \---

## title: Réponse

`R`, `G` et `B` représentent la quantité de rouge, de vert et de bleu qui sera utilisée dans la couleur. Chacune peut avoir une valeur de `0` à `255`.

Donc pour faire du jaune, tu peux essayer ce qui suit :

```python
R = 255
G = 255
B = 0
```

\--- /collapse \---

[[[generic-theory-simple-colours]]]

Tu peux modifier la valeur de tes variables en leur attribuant une nouvelle valeur ou en les augmentant et en les diminuant.

- Tu peux également changer la couleur de la tortue. Exécute le code ci-dessous pour voir ce qui se passe: <iframe src="https://trinket.io/embed/python/ab6732d60e" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

### Défi

Essaye de relever chacun des défis ci-dessous.

- Compléter le triangle ci-dessus avec la couleur de ton choix.
- Dessiner un carré avec des côtés utilisant quatre nuances différentes de rouge.
- Dessiner une croix faite de quatre couleurs différentes.

\--- hints \--- \--- hint \---

Pour changer une couleur, tu peux simplement continuer à ajouter ou à soustraire des valeurs des variables d'origine.

\--- /hint \--- \--- hint \---

Tu peux donc modifier les couleurs en procédant comme suit:

```python
R = 255
G = 0
B = 0

turtle.color((R, G, B))
turtle.forward(100)
turtle.right(120)

R -= 20
G += 20
B += 5

turtle.color((R, G, B))
turtle.forward(100)
turtle.right(120)
```

\--- /hint \--- \--- /hints \---