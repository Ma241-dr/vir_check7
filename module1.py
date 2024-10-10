import sys
import os
print(__file__)

#sys.path.insert(0, r"c:\modul")
#ssys.path.append(r"c:\modul")
import sys
import os

# Add the utils directory to the system path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '', 'modu')))
#sys.path.append(sys.path.absolute(sys.path.join(sys.path.dirname(__file__,".","c:\modul"))))
print(sys.path[0])
import modu


temp = modu.add(6, 7)
print(temp)
print("hello")