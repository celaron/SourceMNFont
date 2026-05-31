import re
from itertools import chain

reverse_lookup = {}


def add_lookup(char, component):
    if component not in reverse_lookup:
        reverse_lookup[component] = set()
    reverse_lookup[component].add(char)


with open("decomp/decomp.txt", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip()
        for match in re.finditer("[!@][^!@]+", line):
            if match.group()[0] == "!":
                continue
            for component in match.group()[1:]:
                add_lookup(line[0], component)

with open("decomp/variants.txt", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip()
        var, standard = line.split("\t")
        # infinite recursion fix
        if standard == "𤦡":
            continue
        add_lookup(var, standard)


for k, v in reverse_lookup.items():
    reverse_lookup[k] = sorted(v)


def lookup_chars(component, charset=None):
    def _lookup_chars(component):
        try:
            if component not in reverse_lookup:
                return [component]
            return [component] + list(
                chain(*[_lookup_chars(c) for c in reverse_lookup[component]])
            )
        except RecursionError:
            raise RecursionError(f"RecursionError: {component}")

    all_chars = sorted(set(_lookup_chars(component)))
    if charset is None:
        return all_chars
    else:
        return [c for c in all_chars if c in charset]


if __name__ == "__main__":
    print(lookup_chars("雨"))
