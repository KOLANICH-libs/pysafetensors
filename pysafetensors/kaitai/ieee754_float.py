# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Ieee754Float(KaitaiStruct):
    """An extremily widespread format of floating-point numbers used in most of hardware implementations of floating-point numbers.
    Unfortunately not all the standardized formats are supported natively in hardware, programming languages and software, especially in old ones. For example Kaitai Struct itself doesn't support anything except `f4` and `f8` natively.
    This is an implementation of these formats purely in Kaitai Struct. It makes no guarantees of precision, correctness, efficiency or anything else. It is just something that is better than nothing.
    This file contains common logic converting integers representing different parts of floating point numbers into a floating point number implemented in your language. Typically it is `f8`.
    In order to use this, parse the parts of your floating point number and create an instance with a `pos` and `type` (at the time of this format creation KS had no support for typed value instances), passing the parsed parts, their bit-sizes and exponent bias as params.
    """
    def __init__(self, bias, fraction_bit_size, biased_exponent_bit_size, sign, biased_exponent, fraction, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.bias = bias
        self.fraction_bit_size = fraction_bit_size
        self.biased_exponent_bit_size = biased_exponent_bit_size
        self.sign = sign
        self.biased_exponent = biased_exponent
        self.fraction = fraction
        self._read()

    def _read(self):
        pass

    @property
    def is_nan(self):
        if hasattr(self, '_m_is_nan'):
            return self._m_is_nan

        self._m_is_nan =  ((self.biased_exponent_is_special) and (self.fraction != 0)) 
        return getattr(self, '_m_is_nan', None)

    @property
    def exponent(self):
        if hasattr(self, '_m_exponent'):
            return self._m_exponent

        self._m_exponent = ((self.biased_exponent - self.bias) + (1 if self.is_denorm else 0))
        return getattr(self, '_m_exponent', None)

    @property
    def is_denorm(self):
        if hasattr(self, '_m_is_denorm'):
            return self._m_is_denorm

        self._m_is_denorm = self.biased_exponent == 0
        return getattr(self, '_m_is_denorm', None)

    @property
    def mantissa(self):
        if hasattr(self, '_m_mantissa'):
            return self._m_mantissa

        self._m_mantissa = ((0 if self.is_denorm else 1) + ((self.fraction * 1) / (1 << self.fraction_bit_size)))
        return getattr(self, '_m_mantissa', None)

    @property
    def value(self):
        if hasattr(self, '_m_value'):
            return self._m_value

        self._m_value = (-(self.modulus) if self.sign else self.modulus)
        return getattr(self, '_m_value', None)

    @property
    def is_inf(self):
        if hasattr(self, '_m_is_inf'):
            return self._m_is_inf

        self._m_is_inf =  ((self.biased_exponent_is_special) and (self.fraction == 0)) 
        return getattr(self, '_m_is_inf', None)

    @property
    def only_ones_biased_exponent(self):
        if hasattr(self, '_m_only_ones_biased_exponent'):
            return self._m_only_ones_biased_exponent

        self._m_only_ones_biased_exponent = ((1 << self.biased_exponent_bit_size) - 1)
        return getattr(self, '_m_only_ones_biased_exponent', None)

    @property
    def pow(self):
        if hasattr(self, '_m_pow'):
            return self._m_pow

        self._m_pow = ((1 << self.exponent) if self.exponent >= 0 else (1 / (1 << -(self.exponent))))
        return getattr(self, '_m_pow', None)

    @property
    def biased_exponent_is_special(self):
        if hasattr(self, '_m_biased_exponent_is_special'):
            return self._m_biased_exponent_is_special

        self._m_biased_exponent_is_special = self.biased_exponent == self.only_ones_biased_exponent
        return getattr(self, '_m_biased_exponent_is_special', None)

    @property
    def modulus(self):
        if hasattr(self, '_m_modulus'):
            return self._m_modulus

        self._m_modulus = (self.mantissa * self.pow)
        return getattr(self, '_m_modulus', None)


