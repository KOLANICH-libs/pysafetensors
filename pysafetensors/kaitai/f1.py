# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import ieee754_float
class F1(KaitaiStruct):
    """see the doc for `ieee754_float`."""
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.sign = self._io.read_bits_int_be(1) != 0
        self.biased_exponent = self._io.read_bits_int_be(4)
        self.fraction = self._io.read_bits_int_be(3)

    @property
    def value(self):
        if hasattr(self, '_m_value'):
            return self._m_value

        _pos = self._io.pos()
        self._io.seek(0)
        self._m_value = ieee754_float.Ieee754Float(-2, 3, 4, self.sign, self.biased_exponent, self.fraction, self._io)
        self._io.seek(_pos)
        return getattr(self, '_m_value', None)


