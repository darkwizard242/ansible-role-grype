[![build-test](https://github.com/darkwizard242/ansible-role-grype/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-grype/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-grype/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-grype/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/grype) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-grype&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-grype) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-grype&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-grype) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-grype&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-grype) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-grype?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-grype?color=orange&style=flat-square)

# Ansible Role: grype

Role to install (_by default_) [grype](https://github.com/anchore/grype) on **Debian/Ubuntu** and **EL** systems. A vulnerability scanner for container images and filesystems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
grype_app: grype
grype_desired_state: present
grype_version: 0.77.1
grype_os: linux
grype_arch: amd64

# For Debian/Ubuntu Family
grype_debian_url: "https://github.com/anchore/{{ grype_app }}/releases/download/v{{ grype_version }}/{{ grype_app }}_{{ grype_version }}_{{ grype_os }}_{{ grype_arch }}.deb"

# For EL Family
grype_el_url: "https://github.com/anchore/{{ grype_app }}/releases/download/v{{ grype_version }}/{{ grype_app }}_{{ grype_version }}_{{ grype_os }}_{{ grype_arch }}.rpm"
```

### Variables table:

Variable            | Description
------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
grype_app           | Defines the app to install i.e. **grype**
grype_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.
grype_version       | Defined to dynamically fetch the desired version to install. Defaults to: **0.77.1**
grype_os            | Defines os type. Used for obtaining the correct type of binaries based on OS type. Defaults to: **linux**
grype_arch          | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **amd64**
grype_debian_url    | Defines URL to download the 'deb' package from for Debian/Ubuntu family systems.
grype_el_url        | Defines URL to download the 'rpm' package from for EL family systems.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **grype**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.grype
```

For customizing behavior of role (i.e. specifying the desired **grype** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.grype
  vars:
    grype_version: 0.27.3
```

For customizing behavior of role (i.e. different os architecture of **grype** package like arm64) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.grype
  vars:
    grype_arch: "arm64"
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-grype/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev)
