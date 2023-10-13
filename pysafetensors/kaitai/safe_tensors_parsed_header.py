# save it as safe_tensors_parsed_header.py
try:
	from typing import Self
except ImportError:
	from typing_extensions import Self

try:
	import ujson as json
except ImportError:
	import json

from kaitaistruct import KaitaiStruct
from safetensors_schema import validate as validate_safetensors_header_schema

from .ndarray_descriptor import NdarrayDescriptor

_categoriesRemap = {
	"U": NdarrayDescriptor.Category.uint,
	"I": NdarrayDescriptor.Category.sint,
	"F": NdarrayDescriptor.Category.ieee754,
}

class SafeTensor(KaitaiStruct):
	__slots__ = ("name",  "shape", "offsets", "descriptor")

	def __init__(self, item_type: str, shape, offsets: range, _io=None, _parent=None, _root=None):
		self._parent = _parent
		self.name = None
		self.offsets = offsets
		typeLetter = item_type[:1]
		typeBitSize = int(item_type[1:])
		typeByteSize = typeBitSize // 8
		log2size = typeByteSize.bit_length() - 1
		typeCategory = _categoriesRemap[typeLetter]
		#print("typeLetter=", typeLetter, "typeCategory=", typeCategory, "typeByteSize=", typeByteSize, "log2size=",log2size)
		item_type = NdarrayDescriptor.EncodeType(endianness=NdarrayDescriptor.Endianness.le, category=typeCategory, log2size_or_special=log2size, _io=None).value
		#print("item_type=", item_type)
		self.descriptor = NdarrayDescriptor(item_type=item_type, shape=shape, _io=_io, _parent=self, _root=_root)

	@property
	def dimensions(self) -> int:
		return len(self.descriptor.shape)

	@classmethod
	def fromJSON(cls, jsd, _io=None, _parent=None, _root=None) -> Self:
		return SafeTensor(item_type = jsd["dtype"], shape = jsd["shape"], offsets = range(*jsd["data_offsets"]), _io=_io, _parent=_parent, _root=_root)

	def __repr__(self):
		return self.__class__.__name__ + "<" + ", ".join((repr(self.descriptor.item_type), repr(self.descriptor.shape), repr(self.offsets))) + ">"

class SafeTensorsParsedHeader(KaitaiStruct):
	__slots__ = ("metadata", "tensors") 

	def __init__(self, header_str: str, _io=None, _parent=None, _root=None):
		self._parent = _parent
		header = validate_safetensors_header_schema(json.loads(header_str))
		self.metadata = header.get("__metadata__", None)
		try:
			del header["__metadata__"]
		except KeyError:
			pass

		tensors = []
		for k, v in header.items():
			t = SafeTensor.fromJSON(v, _io=_io, _parent=self, _root=_root)
			t.name = k
			tensors.append(t)
		self.tensors = tensors
