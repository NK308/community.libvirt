from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.libvirt.plugins.module_utils.pools import LibvirtConnection as PoolConnection
from libvirt import virConnect, virStoragePool, virStorageVol
from typing import overload, Optional

ENTRY_COMMANDS: list[str]
ENTRY_COMMANDS: list[str]

ENTRY_STATE_ACTIVE_MAP: dict[int, str]
ENTRY_STATE_AUTOSTART_MAP: dict[int, str]
ENTRY_STATE_PERSISTENT_MAP: dict[int, str]
ENTRY_STATE_INFO_MAP: dict[int, str]

ENTRY_BUILD_FLAGS_MAP: dict
ENTRY_DELETE_FLAGS_MAP: dict


class LibvirtConnection:
    module: AnsibleModule
    conn: virConnect
    poolid: str
    poolConn: PoolConnection
    pool: virStoragePool

    @overload
    def find_entry(self, entryid: str) -> virStorageVol: ...
    def find_entry(self, entryid: int = -1) -> list[virStorageVol]: ...

    def create(self, entryid: str, xml: str): ...
    def create_from(self, entryid: str, xml: str, to_clone: str): ...
    def delete(self, entryid: str): ...
    def wipe(self, entryid: str, mode): ...

    def get_status(self, entryid: str) -> str: ...
    def get_status2(self, entry: virStorageVol) -> str: ...
    def get_uuid(self, entryid: str) -> str: ...
    def get_xml(self, entryid: str) -> str: ...
    def get_info(self, entryid: str) -> str: ...
