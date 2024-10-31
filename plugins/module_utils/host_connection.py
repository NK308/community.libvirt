from ansible_collections.community.libvirt.plugins.module_utils.import_check import HAS_VIRT, HAS_XML
if HAS_VIRT:
    import libvirt
else:
    raise ImportError


def create_connection(uri, module):
    cmd = "uname -r"
    rc, stdout, stderr = module.run_command(cmd)
    if "xen" in stdout:
        conn = libvirt.open(None)
    elif "esx" in uri:
        auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_NOECHOPROMPT], [], None]
        conn = libvirt.openAuth(uri, auth)
    else:
        conn = libvirt.open(uri)
    if not conn:
        raise Exception("hypervisor connection failure")
     return conn
