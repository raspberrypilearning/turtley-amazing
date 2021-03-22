## Modulo à la rescousse

Dans l'exemple précédent, tu avais besoin d'un moyen de continuer à parcourir les éléments de la liste, donc quand `i` arrivait à 9, il retournerait au début et récupérerait le "0e" élément de la liste. C'est là que l'opérateur modulo `%` peut t'aider.

- Regarde le code ci-dessous: exécute-le pour voir si tu peux comprendre ce qui se passe. Tu devrais obtenir `0` pour commencer. <iframe src="https://trinket.io/embed/python/8fd77a1942" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

- Essaie de changer les nombres dans la commande `print`. Voici quelques exemples à essayer ci-dessous:
    
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

- As-tu compris? L'opérateur `%` imprime le reste d'une division. Par exemple, 15 ÷ 6 vaut 2 avec un reste de 3. Par conséquent, 15% 6 serait 3. Nous pouvons utiliser cet opérateur pour résoudre le problème de la fin de la liste. Si le `range` dépasse la longueur de la liste, tu peux simplement faire un `%` de la longueur de la liste.

- Jette un œil à l'exemple ci-dessous et lis attentivement le code pour t'assurer que tu peux comprendre comment l'opérateur modulo est utilisé. <iframe src="https://trinket.io/embed/python/c56b5cb705" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>