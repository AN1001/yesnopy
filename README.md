## yesnopy- a package by Arnav N

Simpilfies vailidating user input and return True/False based on a list of expected inputs. Also accounts for extra whitespace and capitalisation

## Installation

```bash
pip install yesnopy
```

## Usage

```python
from yesnopy import yesnopy as yn

if yn.returnDecision(inputMessage="", forceValidInput=False, defaultValue=False):
  doSomething()

# Or just RD (if you prefer concise notation)
if yn.RD(inputMessage="", forceValidInput=False, defaultValue=False):
  doSomething()
```

inputMessage [STRING]: what to display when asking a question

forceVaildInput [BOOL]: Keep asking until user inputs valid input?

defaultValue [ANY]: If all else fails what should the function return? (can be string, number etc...)

```python
userWantsCake = yn.returnDecision(inputMessage="Do you want cake? ", True)

if userWantsCake:
  print("Returned True")
else:
  print("Returned False")

```
```bash
Do you want cake? gibB432ish
Do you want cake? asdbajksdf
Do you want cake? yeah
Returned True
```
```bash
Do you want cake? gibB432ish
Do you want cake? asdbajksdf
Do you want cake? nah
Returned False
```

Example of using default:
```python
userWantsCake = yn.returnDecision("Do you want cake? ", False, "ERROR")

if userWantsCake:
  print("Returned True")
elif not userWantsCake:
  print("Returned False")
elif userWantsCake=="ERROR":
  print("Something went wrong...") 

```
```bash
Do you want cake? I dont know?
Something went wrong...
```
Please do note: if forceValidInput is set to True the program will continue until it can output a True or a False value, hence defaultValue will not be returned 

## All possible inputs


yesnopy accepts a wide range of inputs, all of them are listed here:

WILL RETURN TRUE:

'y','yes','1','true','yep','allright','alright','verywell','ofcourse','byallmeans','sure','certainly','absolutely','indeed','affirmative','agreed','roger','aye','ayeaye','yeah','yah','yep','yup','uh-huh','okay','ok','okey-dokey','okey-doke','achcha','righto','righty-ho','surely'

WILL RETURN FALSE:

'n','no','0','nope','false','not','noindeed','absolutelynot','mostcertainlynot','ofcoursenot','undernocircumstances','bynomeans','notatall','negative','never','notreally','nothanks','nae','nope','nah','notonyourlife','noway','nofear','notonyournelly','nosiree','naw'

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

MIT

