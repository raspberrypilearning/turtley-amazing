## De meilleures spirales

- Essaye de lire le code ci-dessous et de deviner ce qu'il fait. Ensuite, exécute-le pour voir si tu avais raison. 
<iframe src="https://trinket.io/embed/python/8f98ccf1fa" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

- La première chose que tu remarqueras probablement est que cela prendra des années à fonctionner. Nous pouvons cependant accélérer un peu les choses. Ajoute la ligne suivante, avant la boucle `for`:
    
    ```python
    turtle.speed(0)
    ```

- Exécute à nouveau le code : il devrait être un peu plus rapide.

- Notre code a créé une spirale multicolore en modifiant les variables `R`, `G` et `B`. Les couleurs sont cependant un peu unidimensionnelles. Peux-tu améliorer ceci ?