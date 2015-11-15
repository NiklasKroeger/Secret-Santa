# Secret-Santa
Python 3 script for drawing secret santa pairings without anyone knowing all the pairings.

# Usage
```
usage: SecretSanta.py [-h] [-p] [-d]

optional arguments:
  -h, --help         show this help message and exit
  -p, --print-names  print names to terminal
  -d, --dry-run      don't write output files
```

To use the script input the names of all participants into the `names` list:
```
names=['A', 'B', 'C', 'D', 'E']
```
`invalidpairs` can be used to prevent certain drawings (useful if couples take part or some people don't know each other yet):
```
invalidpairs={  'A': set(['B']),
                'B': set(['A', 'C'])}
```
This example means that `A` will never have to get a present for `B`. `B` will never have to get a present for `A` or `C`.

To make the gifting easier it is possible (not necessary) for all participants to give hints what they would like. Those should be saved in a `.txt` file in the `hints` folder with the name of the participant (e.g. `A.txt`).

The drawn pairings will be written to output files. Each participant will get his/her own file named after the participant. It contains the name of the person they should get a gift for as well as the hint this person gave. These files can then be emailed to the correct participant. Here is an example ouput (if a hintfile existed):
```
Hello E.
You will buy a present for A.
Have fun!

A has given this hint for his/her present:
Some hint from A
```
If no hint was given the last two lines would be replaced by `A has not given a hint...`.

Everytime the script is run it overwrites all currently existing outputfiles without further warning.

# Optional arguments
 - `-p`: print the drawn parings to the terminal (useful for debugging)
 - `-d`: dry-run the script without creating output files

# Notes
 - In order to make sure there are proper line endings for windows users the created output files should be converted with unix2dos. Otherwise windows users might just see 1 long, unformatted line in the `.txt` files.
