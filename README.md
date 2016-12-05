# envr

Manipulate and transform .env files.

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

```sh
# reads standard input, transforms it with Envr.env(strict=True), and writes
# the result to standard output
cat script.sh | python -m envr
```

# `.env` envr syntax

`.env` syntax is a subset of POSIX shell scripts.

Each parseable line of the file contains a variable assignment of the form:
```
VARIABLE_NAME=VALUE COMMENT
```

`NAME` must match `[a-zA-Z0-9_]+`.

`VALUE` must match `[^"']` if enclosed by one pair of any character in the set `["']`; otherwise it must match `[^\s"']`.

`COMMENT` may be omitted, and if present must begin with a `#` after the space separating it from `VALUE`.

#  compatible with

`.env` envr syntax is compatible as a subset of `.env` files for

- honcho
- django-environ
- python-dotenv (except for a bug with single quotes)
- [docker-compose](https://docs.docker.com/compose/env-file/)
