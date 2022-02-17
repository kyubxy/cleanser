from genericpath import isfile
import sys
import os
import pathlib

args = sys.argv

path = args[1] 

# read bad words
words = []
files = ["custom", "words"]
extensions = []
supp = []

# load project settings
cfile = os.path.join (path, ".cleanse")

# check .gitignore
def checkGitIgnore():
    if (not isfile (".gitignore")):
        return True

    with (open (".gitignore", "r")) as f:
        for l in f:
            line = l.strip()
            if ".cleanse" in line:
                return True

    print ("[ERROR]: .cleanse exists but has not been found in the .gitignore, the program " +
        "cannot proceed unless you add .clenase to the .gitignore, use -i to suppress this error")
    return False

# read file
def readConfig():
    mode = None

    with open (cfile, "r") as f:
        i = 0
        for l in f:
            i += 1
            line = l.strip()

            if len(line) == 0:
                continue

            # comments
            if line[0] == "#":
                continue

            # headers
            if line == "!extensions":
                mode = "ext"
                continue
            elif line == "!words":
                mode = "words"
                continue
            elif line == "!suppress":
                mode = "supp"
                continue
            else:
                if line[0] == "!":
                    print (f"[CONFIG]: no such header {line} exists, is this a typo?")
                    continue

            # reading
            if mode == "ext":
                extensions.append (line)
                continue
            elif mode == "words":
                words.append (line)
                continue
            elif mode == "supp":
                supp.append(line)
                continue

            print (f"[CONFIG]: line {line} on line {i} was not read properly and was subsequently skipped")

if isfile (cfile):
    if (not checkGitIgnore()):
        exit(0)

    readConfig()
else:
    print ("[INFO] no .cleanse file in root, please see the repo wiki page on writing per project config files")

# load bad words
for filename in files:
    with open (filename+".txt", "r") as f:
        for l in f:
            line = l.strip()

            # comments
            if (line[0] == "#"):
                continue

            words.append (line)

# read files
def checkFile(file):
    issues = []
    i = 0
    with open (file, "r") as f:
        for line in f:
            i += 1
            for word in line.split(): 
                if word in words and not word in supp:
                    issues.append ((word, i, file))
    return issues

issues = []


for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        p = pathlib.Path (os.path.join(dirpath, filename))

        # ignore files with the wrong extension
        if not p.suffix in extensions:
            continue

        print (f"| reading {p}...")

        issues.extend(checkFile(p))


# reporting
hasIssues = len(issues) > 0

if hasIssues:
    print ("potential issues:")
    for (word, line, file) in issues:
        print (f"[WORD]: in {file} on line {line}, word '{word}' may be offensive")
else:
    print ("no issues, code is clean")
