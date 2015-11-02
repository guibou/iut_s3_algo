def keyAnagram(value):
    return ''.join(sorted(value))

groups = {}

with open('/usr/share/dict/french') as f:
    for line in f:
        line = line.strip()

        sWord = keyAnagram(line)

        groups.setdefault(sWord, []).append(line)


print(len(groups), "groupes")
print(groups[keyAnagram("tortue")])
