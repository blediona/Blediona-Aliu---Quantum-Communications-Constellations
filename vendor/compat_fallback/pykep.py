"""Zëvendësim minimal i pykep: vetëm konstantet dhe funksionet që përdor kodi zyrtar.
Vlerat janë të njëjta me pykep 2.x. Përdoret VETËM kur pykep-u real nuk instalohet."""
import datetime

EARTH_RADIUS = 6378137.0          # rrezja e Tokës në metra
MU_EARTH = 398600441800000.0      # konstantja gravitacionale e Tokës (m^3/s^2)

_JD_MJD2000 = 2451544.5           # data Julian e 1 janarit 2000, ora 00:00 (numërimi i ditëve që përdorin astronomët)


class epoch:
    """epoch ruan një moment kohor si numër ditësh që nga 1 janari 2000, dhe jd e kthen atë në datë Julian."""
    def __init__(self, val, kind="mjd2000"):
        assert kind == "mjd2000"
        self.mjd2000 = float(val)

    @property
    def jd(self):
        return self.mjd2000 + _JD_MJD2000


def epoch_from_iso_string(s):
    """epoch_from_iso_string e kthen një datë si "19491231T000000" në epoch"""
    d = datetime.datetime.strptime(s, "%Y%m%dT%H%M%S")
    ref = datetime.datetime(2000, 1, 1)
    return epoch((d - ref).total_seconds() / 86400.0)