from ansible_collections.community.libvirt.plugins.module_utils.import_check import HAS_VIRT, HAS_XML
if HAS_VIRT:
    import libvirt
else:
    raise ImportError


class LibvirtObject(object):
    def __init__(self, wrapped, parent, module):
        self.obj = wrapped
        self.parent = parent
        self.module = module

    @classmethod
    def get_all(cls, parent):
        raise NotImplementedError

    @classmethod
    def get_by_name(cls, name, parent):
        raise NotImplementedError

    @classmethod
    def define_from_xml(self, xml, parents):
        pass

    def get_status(self):
        raise NotImplementedError

    def get_xml(self):
        raise NotImplementedError

    def get_uuid(self):
        return obj.UUIDString()

    def start(self):
        obj.create()

    def stop(self):
        obj.stop()

    @property
    def autostart(self):
        return obj.autostart()

    @autostart.setter
    def autostart(self, value):
        obj.setAutostart(value)

