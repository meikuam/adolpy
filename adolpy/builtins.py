
from adolpy.common import active_function, active_operator, inf, nan, Active

import builtins

@active_function(builtins)
def abs(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    else:
        return nan
