"""hibakezeles tesz"""

def parseline(line):
    """parse one config line. The config format is key=value."""
    line = line.strip()
    key, value = line.split("=")
    return key.strip(), int(value)

filename = "correct2.conf"
variables = {}

for l in open(filename).readlines():
    k, v = parseline(l)
    variables[k] = v

print (variables)
#
#

