# Generated by rpcgen.py from portmap.x on Sat Nov 16 15:25:09 2019
import sys,os
sys.path.append(os.path.dirname(__file__))
from typing import Any, List, Optional, Union
from vxi11aio.xdr import portmap_const as const, portmap_type as types
import xdrlib
from xdrlib import Error as XDRError

class nullclass(object):
    pass

class PORTMAPPacker(xdrlib.Packer):
    def __init__(self, check_enum:bool=True, check_array:bool=True) -> None:
        xdrlib.Packer.__init__(self)
        self.check_enum = check_enum
        self.check_array = check_array

    pack_int = xdrlib.Packer.pack_int
    pack_uint = xdrlib.Packer.pack_uint
    pack_unsigned = xdrlib.Packer.pack_uint
    pack_hyper = xdrlib.Packer.pack_hyper
    pack_uhyper = xdrlib.Packer.pack_uhyper
    pack_float = xdrlib.Packer.pack_float
    pack_double = xdrlib.Packer.pack_double
    pack_quadruple = xdrlib.Packer.pack_double
    pack_bool = xdrlib.Packer.pack_bool
    pack_opaque = xdrlib.Packer.pack_opaque
    pack_string = xdrlib.Packer.pack_string
    def pack_mapping(self, data: types.mapping) -> None:
        if hasattr(self, 'filter_mapping'):
            data = getattr(self, 'filter_mapping')(data)
        if data.prog is None:
            raise TypeError('data.prog == None')
        self.pack_uint(data.prog)
        if data.vers is None:
            raise TypeError('data.vers == None')
        self.pack_uint(data.vers)
        if data.prot is None:
            raise TypeError('data.prot == None')
        self.pack_uint(data.prot)
        if data.port is None:
            raise TypeError('data.port == None')
        self.pack_uint(data.port)

    def pack_pmaplist(self, data: types.pmaplist) -> None:
        if hasattr(self, 'filter_pmaplist'):
            data = getattr(self, 'filter_pmaplist')(data)
        if data.map is None:
            raise TypeError('data.map == None')
        self.pack_mapping(data.map)
        if data.next is None:
            raise TypeError('data.next == None')
        self.pack_pmaplist(data.next)

    def pack_call_args(self, data: types.call_args) -> None:
        if hasattr(self, 'filter_call_args'):
            data = getattr(self, 'filter_call_args')(data)
        if data.prog is None:
            raise TypeError('data.prog == None')
        self.pack_uint(data.prog)
        if data.vers is None:
            raise TypeError('data.vers == None')
        self.pack_uint(data.vers)
        if data.proc is None:
            raise TypeError('data.proc == None')
        self.pack_uint(data.proc)
        if data.args is None:
            raise TypeError('data.args == None')
        self.pack_opaque(data.args)

    def pack_call_result(self, data: types.call_result) -> None:
        if hasattr(self, 'filter_call_result'):
            data = getattr(self, 'filter_call_result')(data)
        if data.port is None:
            raise TypeError('data.port == None')
        self.pack_uint(data.port)
        if data.res is None:
            raise TypeError('data.res == None')
        self.pack_opaque(data.res)

class PORTMAPUnpacker(xdrlib.Unpacker):
    def __init__(self, data:bytes, check_enum:bool=True, check_array:bool=True) -> None:
        xdrlib.Unpacker.__init__(self, data)
        self.check_enum = check_enum
        self.check_array = check_array

    unpack_int = xdrlib.Unpacker.unpack_int
    unpack_uint = xdrlib.Unpacker.unpack_uint
    unpack_unsigned = xdrlib.Unpacker.unpack_uint
    unpack_hyper = xdrlib.Unpacker.unpack_hyper
    unpack_uhyper = xdrlib.Unpacker.unpack_uhyper
    unpack_float = xdrlib.Unpacker.unpack_float
    unpack_double = xdrlib.Unpacker.unpack_double
    unpack_quadruple = xdrlib.Unpacker.unpack_double
    unpack_bool = xdrlib.Unpacker.unpack_bool
    unpack_opaque = xdrlib.Unpacker.unpack_opaque
    unpack_string = xdrlib.Unpacker.unpack_string
    def unpack_mapping(self) -> types.mapping:
        data = types.mapping()
        data.prog = self.unpack_uint()
        data.vers = self.unpack_uint()
        data.prot = self.unpack_uint()
        data.port = self.unpack_uint()
        if hasattr(self, 'filter_mapping'):
            data = getattr(self, 'filter_mapping')(data)
        return data

    def unpack_pmaplist(self) -> types.pmaplist:
        data = types.pmaplist()
        data.map = self.unpack_mapping()
        data.next = self.unpack_pmaplist()
        if hasattr(self, 'filter_pmaplist'):
            data = getattr(self, 'filter_pmaplist')(data)
        return data

    def unpack_call_args(self) -> types.call_args:
        data = types.call_args()
        data.prog = self.unpack_uint()
        data.vers = self.unpack_uint()
        data.proc = self.unpack_uint()
        data.args = self.unpack_opaque()
        if hasattr(self, 'filter_call_args'):
            data = getattr(self, 'filter_call_args')(data)
        return data

    def unpack_call_result(self) -> types.call_result:
        data = types.call_result()
        data.port = self.unpack_uint()
        data.res = self.unpack_opaque()
        if hasattr(self, 'filter_call_result'):
            data = getattr(self, 'filter_call_result')(data)
        return data

