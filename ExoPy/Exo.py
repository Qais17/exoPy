import numpy as np
tableauA = np.arange(0, 100, 3)
print(tableauA)

import numpy as np
TableauB = np.sin((tableauA**2)*(np.pi/2))
print(TableauB)

import numpy as np
var = np.max(TableauB)
print(var)

import numpy as np
ui = np.argwhere(TableauB == var)
print(ui)

len(ui)