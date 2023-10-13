import typing

import numpy as np

from .kaitai.ndarray_descriptor import NdarrayDescriptor

__all__ = ("toNumPy",)

ItemType = NdarrayDescriptor.ItemType
DecodeType = NdarrayDescriptor.DecodeType
Category = NdarrayDescriptor.Category
Endianness = NdarrayDescriptor.Endianness

_endiannesses = {
	Endianness.be: ">",
	Endianness.le: "<",
	Endianness.machine: "=",
}

_cats = {
	Category.uint: "uint",
	Category.sint: "int",
	Category.ieee754: "float",
}

def decodeNumpyIntoEndianAndTypeStr(itemType: ItemType) -> typing.Tuple[str, str]:
	deco = DecodeType(itemType, _io=None)
	return _endiannesses[deco.endianness], _cats[deco.category] + str(deco.size * 8)

def decodeNumpyIntoTypeStr(itemType: ItemType) -> str:
	endiannessStr, typeStr = decodeNumpyIntoEndianAndTypeStr(itemType)
	return endiannessStr + np.sctype2char(typeStr)

def decodeNumpyIntoType(itemType: ItemType):
	return np.dtype(decodeNumpyIntoTypeStr(itemType))

def toNumPy(tensor) -> np.ndarray:
	dtype = decodeNumpyIntoType(tensor.header.descriptor.item_type)
	return np.frombuffer(tensor.flat, dtype=dtype).reshape(tensor.header.descriptor.shape)
