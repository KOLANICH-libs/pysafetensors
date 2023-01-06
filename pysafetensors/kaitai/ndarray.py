# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import f2le
from . import f16le
from . import f10le
from . import f1
from . import f16be
from . import f32le
from . import f12be
from . import f12le
from . import f10be
from . import f2be
from . import f32be
from .ndarray_descriptor import NdarrayDescriptor

class Ndarray(KaitaiStruct):
    def __init__(self, descriptor, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.descriptor = descriptor
        self._read()

    def _read(self):
        self.data_initial = Ndarray.NdarrayInternal(-1, self._io, self, self._root)

    class Array(KaitaiStruct):
        def __init__(self, idx, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.idx = idx
            self._read()

        def _read(self):
            self.data = []
            for i in range(self._root.descriptor.shape[self.idx]):
                _on = self._root.descriptor.item_type
                if _on == NdarrayDescriptor.ItemType.f32le:
                    self.data.append(f32le.F32le(self._io))
                elif _on == NdarrayDescriptor.ItemType.u2le:
                    self.data.append(self._io.read_u2le())
                elif _on == NdarrayDescriptor.ItemType.f12me:
                    self.data.append(f12le.F12le(self._io))
                elif _on == NdarrayDescriptor.ItemType.u2be:
                    self.data.append(self._io.read_u2be())
                elif _on == NdarrayDescriptor.ItemType.f12le:
                    self.data.append(f12le.F12le(self._io))
                elif _on == NdarrayDescriptor.ItemType.f2le:
                    self.data.append(f2le.F2le(self._io))
                elif _on == NdarrayDescriptor.ItemType.s4me:
                    self.data.append(self._io.read_s4le())
                elif _on == NdarrayDescriptor.ItemType.s2me:
                    self.data.append(self._io.read_s2le())
                elif _on == NdarrayDescriptor.ItemType.u4me:
                    self.data.append(self._io.read_u4le())
                elif _on == NdarrayDescriptor.ItemType.u8le:
                    self.data.append(self._io.read_u8le())
                elif _on == NdarrayDescriptor.ItemType.f10me:
                    self.data.append(f10le.F10le(self._io))
                elif _on == NdarrayDescriptor.ItemType.sc1:
                    self.data.append(self._io.read_s1())
                elif _on == NdarrayDescriptor.ItemType.f2me:
                    self.data.append(f2le.F2le(self._io))
                elif _on == NdarrayDescriptor.ItemType.f8me:
                    self.data.append(self._io.read_f8le())
                elif _on == NdarrayDescriptor.ItemType.f12be:
                    self.data.append(f12be.F12be(self._io))
                elif _on == NdarrayDescriptor.ItemType.f8be:
                    self.data.append(self._io.read_f8be())
                elif _on == NdarrayDescriptor.ItemType.u4be:
                    self.data.append(self._io.read_u4be())
                elif _on == NdarrayDescriptor.ItemType.f16le:
                    self.data.append(f16le.F16le(self._io))
                elif _on == NdarrayDescriptor.ItemType.f10le:
                    self.data.append(f10le.F10le(self._io))
                elif _on == NdarrayDescriptor.ItemType.s4le:
                    self.data.append(self._io.read_s4le())
                elif _on == NdarrayDescriptor.ItemType.s2le:
                    self.data.append(self._io.read_s2le())
                elif _on == NdarrayDescriptor.ItemType.f10be:
                    self.data.append(f10be.F10be(self._io))
                elif _on == NdarrayDescriptor.ItemType.f32be:
                    self.data.append(f32be.F32be(self._io))
                elif _on == NdarrayDescriptor.ItemType.s8le:
                    self.data.append(self._io.read_s8le())
                elif _on == NdarrayDescriptor.ItemType.u1:
                    self.data.append(self._io.read_u1())
                elif _on == NdarrayDescriptor.ItemType.s8be:
                    self.data.append(self._io.read_s8be())
                elif _on == NdarrayDescriptor.ItemType.s4be:
                    self.data.append(self._io.read_s4be())
                elif _on == NdarrayDescriptor.ItemType.f4le:
                    self.data.append(self._io.read_f4le())
                elif _on == NdarrayDescriptor.ItemType.f8le:
                    self.data.append(self._io.read_f8le())
                elif _on == NdarrayDescriptor.ItemType.u4le:
                    self.data.append(self._io.read_u4le())
                elif _on == NdarrayDescriptor.ItemType.u8me:
                    self.data.append(self._io.read_u8le())
                elif _on == NdarrayDescriptor.ItemType.f2be:
                    self.data.append(f2be.F2be(self._io))
                elif _on == NdarrayDescriptor.ItemType.f16me:
                    self.data.append(f16le.F16le(self._io))
                elif _on == NdarrayDescriptor.ItemType.f4be:
                    self.data.append(self._io.read_f4be())
                elif _on == NdarrayDescriptor.ItemType.u8be:
                    self.data.append(self._io.read_u8be())
                elif _on == NdarrayDescriptor.ItemType.s2be:
                    self.data.append(self._io.read_s2be())
                elif _on == NdarrayDescriptor.ItemType.s1:
                    self.data.append(self._io.read_s1())
                elif _on == NdarrayDescriptor.ItemType.s8me:
                    self.data.append(self._io.read_s8le())
                elif _on == NdarrayDescriptor.ItemType.f1:
                    self.data.append(f1.F1(self._io))
                elif _on == NdarrayDescriptor.ItemType.u2me:
                    self.data.append(self._io.read_u2le())
                elif _on == NdarrayDescriptor.ItemType.f16be:
                    self.data.append(f16be.F16be(self._io))
                elif _on == NdarrayDescriptor.ItemType.f4me:
                    self.data.append(self._io.read_f4le())
                elif _on == NdarrayDescriptor.ItemType.f32me:
                    self.data.append(f32le.F32le(self._io))



    class NdarrayInternal(KaitaiStruct):
        def __init__(self, idx, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.idx = idx
            self._read()

        def _read(self):
            self.data = []
            for i in range((self._root.descriptor.shape[self.idx] if self.idx >= 0 else 1)):
                _on = self.idx == self._root.dims_m_2
                if _on == False:
                    self.data.append(Ndarray.NdarrayInternal((self.idx + 1), self._io, self, self._root))
                elif _on == True:
                    self.data.append(Ndarray.Array(self.idx, self._io, self, self._root))



    @property
    def dims_m_2(self):
        if hasattr(self, '_m_dims_m_2'):
            return self._m_dims_m_2

        self._m_dims_m_2 = (len(self._root.descriptor.shape) - 2)
        return getattr(self, '_m_dims_m_2', None)

    @property
    def data(self):
        if hasattr(self, '_m_data'):
            return self._m_data

        self._m_data = self.data_initial.data[0].data
        return getattr(self, '_m_data', None)


