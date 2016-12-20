#!/usr/bin/env python

from envr import Envr
import sys

e = Envr(stream=sys.stdin)

sys.stdout.write(e.env(strict=True))
sys.stderr.write(e.env(strict=True, quoted=False))
