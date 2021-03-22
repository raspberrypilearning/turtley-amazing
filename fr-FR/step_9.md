## Couleurs excentriques

Pour obtenir des couleurs plus intéressantes, tu peux écrire beaucoup de couleurs dans une longue liste, puis continuer à changer la couleur de la tortue en fonction de la couleur de la liste. Tu peux créer des listes en Python, en utilisant des crochets `[ ]`.

Voici un exemple de liste de couleurs RGB:

```python
colours = [(85, 211, 136), (197, 196, 126), (235, 233, 166), (25, 135, 222), (211, 64, 159), (159, 165, 106) , (178, 160, 125), (36, 192, 70), (231, 184, 204), (63, 203, 219)]
```

- La prochaine étape devient un peu compliquée. Jette un coup d'œil au code ci-dessous, puis exécute-le pour voir ce qui se passe. 
<iframe src="https://trinket.io/embed/python/d58123d315" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

La ligne `turtle.color(colours[i])` indique au programme de choisir le "`i`e" élément de la liste. N'oublie pas que `i` commence à 0 et va jusqu'à 9.

- Que se passe-t-il si tu veux une ligne plus longue ? Essaie de changer le nombre d'itération dans la boucle `for` en `range(20)` et regarde ce qui se passe. As-tu reçu une erreur ?