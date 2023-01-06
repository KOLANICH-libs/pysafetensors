# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import ndarray
from . import safe_tensors_parsed_header
from . import ndarray_descriptor
class Safetensors(KaitaiStruct):
    """Serialization format used by HuggingFace to allow safe deserialization of pytorch models.
    To parse it properly you need a parser for JSON.
    
    .. seealso::
       Source - https://github.com/huggingface/safetensors
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.preheader = Safetensors.Preheader(self._io, self, self._root)
        self.header_str = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.preheader.header_size), 0, False)).decode(u"ascii")
        self._raw_tensors = self._io.read_bytes_full()
        _io__raw_tensors = KaitaiStream(BytesIO(self._raw_tensors))
        self.tensors = Safetensors.Tensors(_io__raw_tensors, self, self._root)

    class Tensors(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = []
            for i in range(len(self._root.header.tensors)):
                self.data.append(Safetensors.Tensor(i, self._io, self, self._root))



    class Tensor(KaitaiStruct):
        def __init__(self, idx, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.idx = idx
            self._read()

        def _read(self):
            pass

        @property
        def ndarray(self):
            if hasattr(self, '_m_ndarray'):
                return self._m_ndarray

            io = self._parent._io
            _pos = io.pos()
            io.seek(self.header.offsets.start)
            self._raw__m_ndarray = io.read_bytes(self.size)
            _io__raw__m_ndarray = KaitaiStream(BytesIO(self._raw__m_ndarray))
            self._m_ndarray = ndarray.Ndarray(self.header.descriptor, _io__raw__m_ndarray)
            io.seek(_pos)
            return getattr(self, '_m_ndarray', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = (self.header.offsets.stop - self.header.offsets.start)
            return getattr(self, '_m_size', None)

        @property
        def dims_m_2(self):
            if hasattr(self, '_m_dims_m_2'):
                return self._m_dims_m_2

            self._m_dims_m_2 = (self.header.dimensions - 2)
            return getattr(self, '_m_dims_m_2', None)

        @property
        def header(self):
            if hasattr(self, '_m_header'):
                return self._m_header

            self._m_header = self._root.header.tensors[self.idx]
            return getattr(self, '_m_header', None)

        @property
        def flat(self):
            if hasattr(self, '_m_flat'):
                return self._m_flat

            io = self._parent._io
            _pos = io.pos()
            io.seek(self.header.offsets.start)
            self._m_flat = io.read_bytes(self.size)
            io.seek(_pos)
            return getattr(self, '_m_flat', None)


    class FakeParsedHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tensors = []
            for i in range(0):
                self.tensors.append(Safetensors.FakeParsedHeader.FakeTensorHeader(self._io, self, self._root))


        class FakeTensorHeader(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.name = (self._io.read_bytes(0)).decode(u"utf-8")
                self.offsets = Safetensors.FakeParsedHeader.FakeTensorHeader.Range(self._io, self, self._root)

            class Range(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.start = self._io.read_u8le()
                    self.stop = self._io.read_u8le()


            @property
            def descriptor(self):
                if hasattr(self, '_m_descriptor'):
                    return self._m_descriptor

                _pos = self._io.pos()
                self._io.seek(0)
                self._m_descriptor = ndarray_descriptor.NdarrayDescriptor(NdarrayDescriptor.ItemType.u1, b"\x00", self._io)
                self._io.seek(_pos)
                return getattr(self, '_m_descriptor', None)



    class Preheader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header_size = self._io.read_u8le()


    @property
    def header(self):
        if hasattr(self, '_m_header'):
            return self._m_header

        self._m_header = self.real_parsed_header
        return getattr(self, '_m_header', None)

    @property
    def real_parsed_header(self):
        """to be added
        """
        if hasattr(self, '_m_real_parsed_header'):
            return self._m_real_parsed_header

        _pos = self._io.pos()
        self._io.seek(0)
        self._m_real_parsed_header = safe_tensors_parsed_header.SafeTensorsParsedHeader(self.header_str, self._io)
        self._io.seek(_pos)
        return getattr(self, '_m_real_parsed_header', None)


