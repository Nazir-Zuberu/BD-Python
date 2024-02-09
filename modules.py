# Files that can be imported into other files for usage. The name of every module is stored in the global
# name __name__. A module can contain executable statements as well as function definitions. 

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib2(50)



#### Standard Modules
    
"""
Python comes with a library of standard modules. Some modules are system specific.
For instance 'winreg' is only built into windows operating system. sys is one
module that is built in every interpreter. The variabe sys.ps1 and sys.ps2 can
be used to change the symbol of the interpreter prompt 

"""

import sys

sys.ps1 # returns '>>>'

sys.ps2 # returns '...'

sys.ps1 = 'C>' # Changes the prompt sign to 'C>'




### The dir() function

# It returns the doc string of a module or object. 



#################################################### Packages ######################################################

"""
A package is a collection of modules. A package can be made of modules or sub-packages.

sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

In the above example, we have a package called sound. Within the package are other packages.
__init__ enables python to recognize/ treat directories as packages. 

"""

## Importing the echo module from effects

import sound.effects.echo

## Alternative way to import echo

from sound.effects import echo # importing a module from a subpackage

from sound.effects.echo import echofilter # importing a function from a module




### Intra-package References

# from the surround.py module in effects, the following imports can be made

from . import echo # '.' means from the current directory, import echo
from .. import formats # This means go outside of the current dictory and import the format package/directory
from ..filter import equalizer # This means go outside of the current directory into the filter directory and import equalizer
