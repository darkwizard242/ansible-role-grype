import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'grype'
PACKAGE_BINARY = "/usr/local/bin/grype"


def test_grype_package_installed(host):
    """
    Tests if grype package is in installed state.
    """
    assert host.package(PACKAGE).is_installed


def test_grype_binary_exists(host):
    """
    Tests if grype binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_grype_binary_file(host):
    """
    Tests if grype binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_grype_binary_which(host):
    """
    Tests the output to confirm grype's binary location.
    """
    assert host.check_output('which grype') == PACKAGE_BINARY
