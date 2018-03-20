import re

# alles entfernen außer Wörtern (a-z, A-Z, 0-9 und noch _) und whitespace
re.sub('[^\w\s]','x','abc! de	f')