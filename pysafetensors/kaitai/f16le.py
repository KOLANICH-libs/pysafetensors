# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import ieee754_float
class F16le(KaitaiStruct):
    """see the doc for `ieee754_float`.
    64fl 32fm 16fh 8el s7eh
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.frac_lo = self._io.read_u8le()
        self.frac_mid = self._io.read_u4le()
        self.frac_hi = self._io.read_u2le()
        self.biased_exponent_lo = self._io.read_u1()
        self.sign = self._io.read_bits_int_be(1) != 0
        self.biased_exponent_hi = self._io.read_bits_int_be(7)

    @property
    def fraction(self):
        if hasattr(self, '_m_fraction'):
            return self._m_fraction

        self._m_fraction = ((((self.frac_hi << 32) | self.frac_mid) << 64) | self.frac_lo)
        return getattr(self, '_m_fraction', None)

    @property
    def biased_exponent(self):
        if hasattr(self, '_m_biased_exponent'):
            return self._m_biased_exponent

        self._m_biased_exponent = ((self.biased_exponent_hi << 8) | self.biased_exponent_lo)
        return getattr(self, '_m_biased_exponent', None)

    @property
    def value(self):
        if hasattr(self, '_m_value'):
            return self._m_value

        _pos = self._io.pos()
        self._io.seek(0)
        self._m_value = ieee754_float.Ieee754Float(262143, 112, 15, self.sign, self.biased_exponent, self.fraction, self._io)
        self._io.seek(_pos)
        return getattr(self, '_m_value', None)


