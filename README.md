# Estruturas de dados

## Objetivos Gerais
Registrar os exemplos das estruturas de dados que estou estudando usando.
- Python
- TDD, 
- Orientação a Objetos
- Clean Code

## Objetivos específicos
- Escrever código python idiomático.
- Escrever teste antes da implementação concreta.
- Escrever código limpo.
- Escrever código orientado a objetos.

## Não é o objetivo
- Sofisticação
- Segurança
- Alto desenpenho

## Ferramentas
- Python==3.9.5
- Poetry==1.1.6
- Pytest==5.4.3

## Lista simplesmente ligada 
### Classe implementada usando o protocolo de sequência básico
#### Métodos disponíveis
- add
- remove
- find

#### Exemplo de uso
```
from single_linked_list import SingleLinkedList

>>> sll = SingleLinkedList()
>>> sll.add(1)
>>> sll.add(2)
>>> sll.add(3)
>>> 
>>> for item in sll:
>>>     print(item)
>>> 
1
2
3
>>> 
>>> sll[1]
1
>>> sll[2]
2
>>> sll
1 -> 2...
>>> sll.find(2)
2
>>> sll.remove(1)
>>>
>>> sll
2...
```

## Fontes
 - [GeeksforGeeks](https://www.geeksforgeeks.org/data-structures)