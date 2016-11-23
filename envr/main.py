from six import iteritems
from collections import OrderedDict
import json
import re


class EnvFile:

    _line_format = r"^[ \t]*(?P<key>{:s})=" + \
        r"(?P<value>['\"]?[^'\"\n]{{0,}}['\"]?)[ \t]*(?P<comment>#.*)?$"
    _key_format = r"[A-z0-9_]+"
    _parse_regex = re.compile(_line_format.format(_key_format))
    _quotemarks = r"'\""

    def __init__(self, path):
        self.path = path
        with open(self.path, "r") as f:
            self.lines = f.read().splitlines()

    def __getitem__(self, key):
        r = self._line_regex(key)
        for line in self.lines:
            match = r.match(line)
            if match is not None:
                break
        else:
            raise KeyError(key)

        value = self._unquote(match.group('value'))
        return value

    def __setitem__(self, key, value):
        for q in self._quotemarks:
            if q in value:
                raise ValueError

        r = self._line_regex(key)
        replace_value_fn = self._replace_value_fn(value)
        for i, line in enumerate(self.lines):
            (replaced_line, num) = r.subn(replace_value_fn, line)
            if num == 1:
                self.lines[i] = replaced_line
                break
        else:
            self.lines += [self._var_format(key, value)]

    def __delitem__(self, key):
        r = self._line_regex(key)
        for line in self.lines:
            match = r.match(line)
            if match is not None:
                break
        else:
            raise KeyError

        self.lines.remove(line)

    def __iter__(self):
        for line in self.lines:
            match = self._parse_regex.match(line)
            if match is None:
                continue

            k, v = match.group('key'),  match.group('value')

            v = self._unquote(v)

            yield k, v

    def save(self):
        with open(self.path, "w") as f:
            f.write(self.env())

    def dict(self):
        return OrderedDict(self)

    def json(self):
        return json.dumps(self.dict(), indent=2)

    def env(self):
        return str("\n".join(self.lines))

    @classmethod
    def _replace_value_fn(cls, value):
        def __f(match):
            return cls._var_format(match.group('key'),
                                   value,
                                   match.group('comment'))
        return __f

    @classmethod
    def _var_format(cls, key, value, comment=""):
        value = cls._quotemarks[0] + value + cls._quotemarks[0]
        if comment is None:
            comment = ""
        elif comment != "":
            comment = " " + comment
        return "{:s}={:s}{:s}".format(str(key), str(value), comment)

    @classmethod
    def _line_regex(cls, key):
        return re.compile(cls._line_format.format(key))

    @classmethod
    def _unquote(cls, v):
        v.strip()

        if v[-1] != v[0]:
            return v

        for q in cls._quotemarks:
            if v[0] == q:
                v = v[1:-1]
                break

        return v
