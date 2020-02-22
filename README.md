# azcopy

[![Build Status](https://github.com/eduardolmedeiros/ansible-role-azcopy/workflows/build/badge.svg)](https://github.com/eduardolmedeiros/ansible-role-azcopy/actions?query=workflow%3Abuild)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-eduardolmedeiros.azcopy-blue.svg)](https://galaxy.ansible.com/eduardolmedeiros/azcopy)

This role install azcopy binary from microsoft repository.

[AzCopy](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) is a command-line utility created and maintained by [Microsoft](https://www.microsoft.com) that you can use to copy blobs or files to or from a storage account.

## Requirements

* This role requires a CentOS, Ubuntu, Debian, or Red Hat Enterprise Linux distribution.
* Ansible 2.7 or higher.

## Role Variables

All "standards" variables are defined on defaults/main.yml.
If you want to replace or change some variable, please change on playbook level.

```
| variable           | description              | default        |
|--------------------|--------------------------|----------------|
| azcopy_pkg_deps    | package dependencies     | unzip          |
| azcopy_tmp_install | temp installation folder | /tmp/azcopy    |
| azcopy_bin_path    | installation path        | /usr/local/bin |
| azcopy_pkg_url     | azcopy source url        |                |
| azcopy_sha256      | sha256 sum               |                |
```

## Dependencies

N/A

## Example Playbook

```
    - hosts: servers
      roles:
         - eduardolmedeiros.azcopy
```

## License

MIT

## Author Information

[Eduardo Medeiros](https://www.emedeiros.me/)
