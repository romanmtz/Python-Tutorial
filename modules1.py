#modules is the concept of using different files to separate code
#the main use is to use functions that are useful through many different programs

import modules2 #import all functions from modules2 file
from modules2 import sum #import only the sum function from modules2
from package.modules3 import example2
# OR import package.modules3 *this is less desirable since to call the function the syntax would be package.module3.example2()

print(modules2.example())
print(modules2.sum(2,2))
print(example2())
