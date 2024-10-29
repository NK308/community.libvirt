HAS_LIBVIRT = True
try:
    import libvirt
except ImportError:
    HAS_LIBVIRT = False
HAS_XML = True
try:
    import lxml
except ImportError:
    HAS_XML = False

