import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_unzip_is_installed(host):
    unzip = host.package("unzip")
    assert unzip.is_installed


def test_azcopy_file(host):
    f = host.file('/usr/local/bin/azcopy')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
