# Generated by rpcgen.py from vxi11.x on Sat Nov 16 15:27:03 2019
device_abort = 1
create_link = 10
device_write = 11
device_read = 12
device_readstb = 13
device_trigger = 14
device_clear = 15
device_remote = 16
device_local = 17
device_lock = 18
device_unlock = 19
device_enable_srq = 20
device_docmd = 22
destroy_link = 23
create_intr_chan = 25
destroy_intr_chan = 26
device_intr_srq = 30
DEVICE_TCP = 0
DEVICE_UDP = 1
Device_AddrFamily = {
    0 : 'DEVICE_TCP',
    1 : 'DEVICE_UDP',
}
DEVICE_ASYNC = 0x0607B0
DEVICE_ASYNC_VERSION = 1
DEVICE_CORE = 0x0607AF
DEVICE_CORE_VERSION = 1
DEVICE_INTR = 0x0607B1
DEVICE_INTR_VERSION = 1
