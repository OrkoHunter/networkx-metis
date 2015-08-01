===========
MetisIPType
===========

``class nxmetis.enums.MetisIPType(enum.IntEnum)``

**Algorithm used during initial partitioning.**

+-----------+---------------------------------------------------------+
| default   | Default method for initial partitioning.                |
+-----------+---------------------------------------------------------+
| grow      | Grow a bisection using a greedy strategy.               |
+-----------+---------------------------------------------------------+
| random    | Compute a bisection at random followed by a refinement. |
+-----------+---------------------------------------------------------+
| edge      | Derive a separator from an edge cut.                    |
+-----------+---------------------------------------------------------+
| node      | Grow a bisection using a greedy node-based strategy.    |
+-----------+---------------------------------------------------------+
