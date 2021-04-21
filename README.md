# value-iteration

## Tutorial
Om het value iteration algoritme uit te voeren, kan onderstaand voorbeeld gebruikt worden.
Of zoals in main.py staat.
```python
from grid import Grid
import numpy as np


rewards = np.array([
            [-1, -1, -1, 40],
            [-1, -1, -10, -10],
            [-1, -1, -1, -1],
            [10, -2, -1, -1]
        ])
terminal_states = [(0, 3), (3, 0)]
gamma = 0.9

grid = Grid(rewards, terminal_states, gamma)
grid.run(10, verbose=True)

```
## Beknopte uitleg code
Bij het aanmaken van een nieuwe grid object zijn de parameters rewards, terminal states en
gamma vereist om mee te geven. Binnen de klasse Grid zijn een aantal methodes die ik verder zal
uitleggen.

### init
In de init word het object geïnitialiseerd, de gegeven parameters worden opgeslagen en de values,
greedy-policy worden aangemaakt.
### value-iteration
In deze methode word de value iteration uitgevoerd voor 1 iteratie met de bellman equation. Bij
methode kan de parameter greedy op True gezet worden. Dan zal voor elke state de optimale actie gezocht worden, 
dit word ook wel de greedy-policy genoemd.
### print values
Deze methode weergeeft de values van het grid.
### print greedy
Deze methode weergeeft de greedy-policy van het grid.
### run
Met deze methode kan een run worden uitgevoerd van het value-iteration algoritme, met de parameter amount_iteration
geef je aan voor hoeveel iteraties het value-iteration uitgevoerd moet worden. En om daar na de greedy-policy te
berekenen, word de value-iterarion nog een laatste keer gedraaid met greedy=True. Met de parameter verbose kan worden
aangegeven of de output van de values en greedy-policy naar het scherm geprint moeten worden.
