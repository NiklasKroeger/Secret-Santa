#!/usr/bin/python

import argparse
import random
import os

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--print-names', action='store_true',
        dest='printNames', default=False, help='print names to terminal')
parser.add_argument('-d', '--dry-run', action='store_true', dest='dryRun',
        default=False, help='don\'t write output files')

def drawSecretSanta(names, invalidpairs):
    ok = False
    while not ok:
        try:
            # shuffle the names a bit more
            random.shuffle(names)
            pairings = {} 
            availablenames = list(names)
            curinvalid = {} 
            # cheat and make windows compatible copy of the names here
            for person in names:
                curinvalid[person]=set(invalidpairs.get(person,set()))
                curinvalid[person].add(person)
            # draw the names
            for person in names:
                pairings[person] = random.choice(list(set(availablenames).difference(curinvalid.get(person,set()))))
                availablenames.remove(pairings[person])
                curinvalid[pairings[person]].add(person) # eliminate A=>B, B=>A possibilites
            ok = True
        except IndexError:
            continue
    return pairings


if __name__ == "__main__":
    args = parser.parse_args()
    names=['A', 'B', 'C', 'D', 'E']
    invalidpairs={  'A': set(['B']),
                    'B': set(['A', 'C'])}

    pairings = drawSecretSanta(names, invalidpairs)
    for key,val in pairings.items():
        if args.printNames:
            print(key + " => " + val)
        if not args.dryRun:
            if os.path.exists("%s.txt" % key):
                os.remove("%s.txt" % key)
            f = open("%s.txt" % key, "w+", encoding = "utf-8")
            f.write("Hello %s.\nYou will buy a present for %s.\nHave fun!\n" % (key, val))
            try:
                with open("hints/%s.txt" %val, encoding = "utf-8") as hintfile:
                    f.write("\n%s has given this hint for his/her present:\n" %val)
                    f.write(hintfile.read())
                    hintfile.close()
            except:
                f.write("\n%s has not given a hint...\n" %val)
            f.close()

    print("Done. Don't forget to run unix2dos on the files!")

