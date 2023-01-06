# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class NdarrayDescriptor(KaitaiStruct):

    class Endianness(IntEnum):
        machine = 0
        le = 1
        be = 2

    class Category(IntEnum):
        uint = 0
        sint = 1
        ieee754 = 2
        string = 3

    class ItemType(IntEnum):
        u1 = 0
        u2me = 1
        u4me = 2
        u8me = 3
        s1 = 8
        s2me = 9
        s4me = 10
        s8me = 11
        f1 = 16
        f2me = 17
        f4me = 18
        f8me = 19
        f16me = 20
        f32me = 21
        f10me = 22
        f12me = 23
        uc1 = 25
        ustr = 26
        u2le = 65
        u4le = 66
        u8le = 67
        s2le = 73
        s4le = 74
        s8le = 75
        f2le = 81
        f4le = 82
        f8le = 83
        f16le = 84
        f32le = 85
        f10le = 86
        f12le = 87
        sc1 = 89
        sstr = 90
        u2be = 129
        u4be = 130
        u8be = 131
        s2be = 137
        s4be = 138
        s8be = 139
        f2be = 145
        f4be = 146
        f8be = 147
        f16be = 148
        f32be = 149
        f10be = 150
        f12be = 151
    def __init__(self, item_type, shape, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.item_type = item_type
        self.shape = shape
        self._read()

    def _read(self):
        pass

    class EncodeType(KaitaiStruct):
        def __init__(self, endianness, category, log2size_or_special, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.endianness = endianness
            self.category = category
            self.log2size_or_special = log2size_or_special
            self._read()

        def _read(self):
            pass

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = KaitaiStream.resolve_enum(NdarrayDescriptor.ItemType, ((((0 if  ((self.log2size_or_special == 0) and (self.category.value < 3))  else self.endianness.value) << 6) | (self.category.value << 3)) | self.log2size_or_special))
            return getattr(self, '_m_value', None)


    class DecodeType(KaitaiStruct):
        def __init__(self, value, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.value = value
            self._read()

        def _read(self):
            pass

        @property
        def category(self):
            if hasattr(self, '_m_category'):
                return self._m_category

            self._m_category = KaitaiStream.resolve_enum(NdarrayDescriptor.Category, ((self.value.value >> 3) & 7))
            return getattr(self, '_m_category', None)

        @property
        def log2size_or_special(self):
            if hasattr(self, '_m_log2size_or_special'):
                return self._m_log2size_or_special

            self._m_log2size_or_special = (self.value.value & 7)
            return getattr(self, '_m_log2size_or_special', None)

        @property
        def endianness(self):
            if hasattr(self, '_m_endianness'):
                return self._m_endianness

            self._m_endianness = KaitaiStream.resolve_enum(NdarrayDescriptor.Endianness, (self.value.value >> 6))
            return getattr(self, '_m_endianness', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            if self.category.value < 3:
                self._m_size = (10 if self.log2size_or_special == 6 else (12 if self.log2size_or_special == 7 else (1 << self.log2size_or_special)))

            return getattr(self, '_m_size', None)

        @property
        def special(self):
            if hasattr(self, '_m_special'):
                return self._m_special

            if self.category.value >= 3:
                self._m_special = self.log2size_or_special

            return getattr(self, '_m_special', None)



