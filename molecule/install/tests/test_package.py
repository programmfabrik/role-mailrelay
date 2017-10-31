import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    assert host.package('mailutils').is_installed
    assert host.package('postfix').is_installed
    assert host.package('lib-sasl2-modules')
