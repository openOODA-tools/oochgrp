Name:           oochgrp
Version:        0.1.0
Release:        1%{?dist}
Summary:        Updates primary and auxiliary group associations for filesystem paths.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oochgrp
Source0:        oochgrp-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oochgrp is a sovereign, capability-bounded GROUP CHANGER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oochgrp
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oochgrp-uninstall

%files
/usr/bin/oochgrp
/usr/bin/oochgrp-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
