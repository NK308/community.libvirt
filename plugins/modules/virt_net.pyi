from typing import overload, Optional

import libvirt
from libvirt import virConnect, virNetwork
from ansible.module_utils.basic import AnsibleModule

ENTRY_STATE_ACTIVE_MAP: dict[int, str]
ENTRY_STATE_AUTOSTART_MAP: dict[int, str]
ENTRY_STATE_PERSISTENT_MAP: dict[int, str]


class EntryNotFound(Exception):
    ...


class LibvirtConnection:
    module: AnsibleModule
    conn: virConnect

    def __init__(self, uri: str, module: AnsibleModule): ...

    @overload
    def find_entry(self, entryid: str) -> virNetwork: ...
    def find_entry(self, entryid: int) -> list[virNetwork]: ...

    def create(self, entryid: str): ...

    def modify(self, entryid: str, xml: str): ...

    def destroy(self, entryid: str): ...

    def undefine(self, entryid: str): ...

    def get_status(self, entryid: str) -> str: ...
    def get_status2(self, entry: virNetwork) -> str: ...
    def get_uuid(self, entryid: str) -> str: ...
    def get_xml(self, entryid: str) -> str: ...

    def get_forward(self, entryid: str) -> str: ...
    def get_domain(self, entryid: str) -> str: ...
    def get_macaddress(entryid: str) -> str: ...
    def get_autostart(self, entryid: str) -> bool: ...

    def get_bridge(self, entryid: str) -> str: ...
    def get_persistent(self, entryid: str) -> str: ...

    def get_dhcp_leases(self, entryid): ...

    def define_from_xml(self, entryid: str, xml: str): ...


class VirtNetwork:
    module: AnsibleModule
    uri: str
    conn: LibvirtConnection

    def __init__(self, uri: str, module: AnsibleModule): ...

    def get_net(self, entryid: str) -> virNetwork: ...

    def list_nets(self, state: Optional[str]) -> list[virNetwork]: ...

    def state(self) -> list[str]: ...

    def autostart(self, entryid: str): ...
    def get_autostart(self, entryid: str) -> bool: ...
    def set_autostart(self, entryid: str, state: bool): ...

    def define(self, entryid: str, xml: str): ...
    def create(self, entryid: str): ...
    def modify(self, entryid: str, xml: str): ...

    def start(self, entryid: str): ...
    def stop(self, entryid: str): ...
    def destroy(self, entryid: str): ...
    def undefine(self, entryid: str): ...

    def status(self, entryid: str) -> str: ...
    def get_xml(self, entryid: str) -> str: ...
    def info(self, entryid: str) -> str: ...
    def facts(self, name: Optional[str] = None, facts_mode: str = 'facts') -> dict: ...

