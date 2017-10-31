import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_etc_mailname(host):
    f = host.file('/etc/mailname')
    assert f.exists

    if host.system_info.distribution == "debian":
        assert f.contains('stretch')
    elif host.system_info.distribution == "ubuntu":
        assert f.contains('xenial')
