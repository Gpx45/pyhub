This folder contains a site package file that is created to be shared and installed
You can then distribute have other use this module in their Python setup.

We can use this to create our own methods, functions, etc; and share them
with others. To create a site package distribution file.
create the py files with the functions you want to place in the distribution
package. Then create a setup.py.

Check the files to see structure. This is how you install more functionality
into different setup other than the original.


To install on Windows, make sure that your cl is in admin mode
use the following command in the right directory of the files.

py -3 setup.py sdist

ON OTHER UNIX OS

python3 setup.py sdist

then to install use the pip module

py -3 -m pip install *NAME OF COMPRESSED FILE*

ON OTHER UNIX OS

sudo python3 -m pip install *NAME OF COMPRESSED FILE*
