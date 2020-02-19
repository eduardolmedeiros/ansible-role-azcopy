Role Name
=========

A brief description of the role goes here.

Requirements
------------
N/A


Role Variables
--------------

All "standards" variables are defined on defaults/main.yml.
If you want to replace or change some variable, please change on playbook level.

| variable | description | mandatory |
|----------|-------------|-----------|
| azcopy_pkg_deps | package dependencies | yes |
| azcopy_tmp_install | temp installation folder | yes |
| azcopy_pkg_url | azcopy source url | yes |
| azcopy_pkg | azcopy package name | yes |
| azcopy_sha256 |sha256 sum  | yes |

Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ansible-role-azcopy, x: 42 }

License
-------

GPLv3

Author Information
------------------

[Eduardo Medeiros](https://www.emedeiros.me/)
