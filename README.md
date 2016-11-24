# envr

Manipulate and transform .env files that are a subset of POSIX - compliant shell
scripts

# Use it

```python
from envr import Envr

# load a file
e = Envr("/app/.env")

# load a stream
o = Envr(None, stream=sys.stdin)

# set keys, get values
e['NEW_KEY'] = e['OLD_KEY'] + e['OTHER_KEY']

# delete key
del e['OLD_KEY']

# save the changes
e.save()

```

# Transforms
```python
# returns an  OrderedDict
e_as_dict = e.dict()

# returns indented json
e_as_json = e.json()

# returns the in memory state, that is as close as possible to the
# original file format, perserving comments and incompatible lines
state = e.env()
state = str(e)

# returns an envr syntax-compatible, POSIX-compliant shell script as a
# string, containing only the variable assignments
e_as_strict_env = e.env(strict=True)
```

# `.env` envr syntax

#  compatible with 

`.env` envr syntax is compatible with

- honcho
- django - environ
- python - dotenv(except for a bug with single quotes)
