azcopy
======

This role install azcopy binary from microsoft repository.

[AzCopy](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) is a command-line utility that you can use to copy blobs or files to or from a storage account.

[![Build Status](https://github.com/eduardolmedeiros/ansible-role-azcopy/workflows/Molecule/badge.svg)](https://github.com/eduardolmedeiros/ansible-role-azcopy/actions?query=workflow%3AMolecule)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-eduardolmedeiros.azcopy-blue.svg)](https://galaxy.ansible.com/eduardolmedeiros/azcopy)

Requirements
------------
No special requirements.


Role Variables
--------------

All "standards" variables are defined on defaults/main.yml.
If you want to replace or change some variable, please change on playbook level.

```
| variable           | description              |
|--------------------|--------------------------|
| azcopy_pkg_deps    | package dependencies     |
| azcopy_tmp_install | temp installation folder |
| azcopy_bin_path    | installation path        |
| azcopy_pkg_url     | azcopy source url        |
| azcopy_sha256      | sha256 sum               |
```

Dependencies
------------

N/A

Example Playbook
----------------
```
    - hosts: servers
      roles:
         - eduardolmedeiros.azcopy
```

License
-------

BSD

Author Information
------------------

[Eduardo Medeiros](https://www.emedeiros.me/)
