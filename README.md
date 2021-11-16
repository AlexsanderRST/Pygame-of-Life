# Pygame of Life

[![](https://i.ibb.co/Jq1xK9Z/videoframe3.png)](https://youtu.be/-yIbimSpmmI)

The game of life follows this rules:
1. If a cell is alive, it dies if less than 2 neighbors are alive
2. If a cell is alive, it lives if between 2 and 3 neighbors are alive
3. If a cell is alive, it dies if more than 3 neighbors are alive
4. If a cell is not alive, it lives if exactly 3 neighbors are alive

In Python:

```
# rule 1
if cell.alive and neighbs_alive < 2:
    cell.alive = False
# rule 2
if cell.alive and 2 <= neighbs_alive <= 3:
    cell.alive = True
# rule 3
if cell.alive and neighbs_alive > 3:
    cell.alive = False
# rule 4
if not cell.alive and neighbs_alive == 3:
    cell.alive = True
```
