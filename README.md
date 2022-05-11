# CompNum

### Purpose:

A module to allow calculation using complex numbers in Python.  Note: this was made as an exercise,  complex numbers are already a native numeric type in Python so this module is not only completely redundant but likely less efficient.

### Included Functionality:

- Instantiation from cartesian or polar coordinates

- Addition

- Subtraction

- Multiplication

- True Division

- Equality/Non-Equality

- Polar Coordinate Conversion

- Exponentiation
  - For now, exponentiation is only capable of raising to integer powers greater or equal to zero

### Never Coming:

- Greater than or lesser than comparisions

- Modular Division

- Floor Division

### Note:

CompNum objects can generally accept integer or float types in mathematical operations (i.e. addition, multiplication, power, etc.) provided that the complex number is listed first. Unfortunately, due to the implementation approach I took, addition and multiplication are non-communitive. To be safe, if you are performing an operation where you have to operate on an int or a float, create a new CompNum object using said int or float and then perform the operation.
