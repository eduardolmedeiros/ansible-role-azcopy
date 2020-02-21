azcopy
======

This role install azcopy binary from microsoft repository.

[AzCopy](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) is a command-line utility that you can use to copy blobs or files to or from a storage account.

Requirements
------------
N/A


Role Variables
--------------

All "standards" variables are defined on defaults/main.yml.
If you want to replace or change some variable, please change on playbook level.

```
| variable           | description              | mandatory |
|--------------------|--------------------------|-----------|
| azcopy_pkg_deps    | package dependencies     | yes       |
| azcopy_tmp_install | temp installation folder | yes       |
| azcopy_bin_path    | installation path        | yes       |
| azcopy_pkg_url     | azcopy source url        | yes       |
| azcopy_sha256      | sha256 sum               | yes       |
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

GPLv3

Author Information
------------------

[Eduardo Medeiros](https://www.emedeiros.me/)
