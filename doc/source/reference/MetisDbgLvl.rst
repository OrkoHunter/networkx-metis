===========
MetisDbgLvl
===========

``class nxmetis.enums.MetisDbgLvl(enum.IntEnum)``

**Amount of progress/debugging information will be printed during the
execution of the algorithms. Can be combined by bit-wise OR.**

+-----------+---------------------------------------------------------+
|default    | Display default statistics.                             |
+-----------+---------------------------------------------------------+
|info       | Print various diagnostic messages.                      |
+-----------+---------------------------------------------------------+
|time       | Perform timing analysis.                                |
+-----------+---------------------------------------------------------+
|coarsen    | Display various statistics during coarsening.           |
+-----------+---------------------------------------------------------+
|refine     | Display various statistics during refinement.           |
+-----------+---------------------------------------------------------+
|ipart      | Display various statistics during initial partitioning. |
+-----------+---------------------------------------------------------+
|moveinfo   | Display detailed information about vertex moves during  |
|           | refinement.                                             |
+-----------+---------------------------------------------------------+
|sepinfo    | Display information about vertex separators.            |
+-----------+---------------------------------------------------------+
|conninfo   | Display information related to the minimization of      |
|           | subdomain connectivity.                                 |
+-----------+---------------------------------------------------------+
|contiginfo | Display information related to the elimination of       |
|           | connected components.                                   |
+-----------+---------------------------------------------------------+
