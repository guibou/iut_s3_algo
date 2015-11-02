# Implementation d'arbre binaire et de hashmap

Implementation commune arbre / hash:

- insert(tree, value) insert une valeur
- search(tree, valeu) retourne True si la valeur est dans l'arbre.
- empty() retourne un vide. Pour les arbre c'est un arbre avec un 0 dedans. (C'est arbitraire).

Variantes arbres :

- simple : arbre binaire non auto balancé. Insertion et recherche au pire en O(n).
- avlSlow : arbre binaire auto balancé. Recherche en O(log n), mais insertion en O(n log n) car il faut recalculer les poids.
- avlQuick : arbre binaire auto balancé rapide. Recherche en O(log n) et insertion en O(log n) car les poids sont mis en cache.
- avlGeneric : pareil que avlQuick, met permet de stocker une valeur arbitraire. L'arbre est cependant réalisé en utilisant la fonction "key" passée en paramètre de insert et search. Cette solution est plus génerique car elle permet de stocker des valeurs arbitraires, et ainsi de faire des dictionnaires. Par example, un dictionnare avec un couple clé valeur sous la forme d'un tuple (clé, valeur). On stocke comme valeur le couple, mais un utilise seulement la clé pour construire l'arbre. Cette implementation est un peu plus lente, car l'abstraction a un prix en python.

(Utilisez un diff pour voir la difference entre les fichiers)

Variantes hash :

- simpleHash : hash avec collisions gerés par sous liste de taille max == 5.

Tests :

python test_perf.py nomImplementation nbElements

Examples :

```
λ manta iut_s3_algo → λ git master* → python test_perf.py simple 100
Insertion Time: 0.001085519790649414
Search time: 2.4275858402252197

λ manta iut_s3_algo → λ git master* → python test_perf.py avlSlow 100
Insertion Time: 0.008957147598266602
Search time: 0.21849584579467773
λ manta iut_s3_algo → λ git master* → python test_perf.py avlSlow 1000
Insertion Time: 0.47202134132385254
Search time: 0.26246070861816406
λ manta iut_s3_algo → λ git master* → python test_perf.py avlSlow 2000
Insertion Time: 1.8082711696624756
Search time: 0.29181599617004395
λ manta iut_s3_algo → λ git master* → python test_perf.py avlSlow 3000
Insertion Time: 4.207085609436035
Search time: 0.3092992305755615

λ manta iut_s3_algo → λ git master* → python test_perf.py avlQuick 3000
Insertion Time: 0.04126572608947754
Search time: 0.3173637390136719
λ manta iut_s3_algo → λ git master* → python test_perf.py avlQuick 30000
Insertion Time: 0.4610917568206787
Search time: 0.37822937965393066
λ manta iut_s3_algo → λ git master* → python test_perf.py avlQuick 300000
Insertion Time: 5.859313249588013
Search time: 0.4247891902923584

λ manta tree → λ git master* → python test_perf.py avlGeneric 10000
Insertion Time: 0.16910457611083984
Search time: 0.8418979644775391

λ manta iut_s3_algo → λ git master* → python test_perf.py simpleHash 1000000
Insertion Time: 1.2083923816680908
Search time: 0.04334592819213867
```
