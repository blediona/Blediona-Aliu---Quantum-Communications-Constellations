import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

try:
    import pykep
except ImportError:
    sys.path.insert(0, os.path.join(ROOT, "vendor", "compat_fallback"))

sys.path.insert(0, os.path.join(ROOT, "vendor", "original"))
from constellations_udp import udp
x = udp.example()
print("x = ", x)
print("fitness =", udp.fitness(x))