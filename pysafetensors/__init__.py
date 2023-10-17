from pathlib import Path
import typing
from warnings import warn

warn("We have moved from M$ GitHub to https://codeberg.org/KFmts/pysafetensors , read why on https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo .")

from .kaitai.safetensors import Safetensors
from .numpy import toNumPy

__all__= ("load",)

def load(d: typing.Union[Path, bytes], convertorFunc = toNumPy):
	if isinstance(d, Path):
		d = d.read_bytes()

	st = Safetensors.from_bytes(d)
	return st.header.metadata, {t.header.name: convertorFunc(t) for t in st.tensors.data} 
