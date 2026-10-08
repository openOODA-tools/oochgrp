# oochgrp: Sovereign GROUP CHANGER

<div align="center">

```
================================================================================
                                oochgrp
               Sovereign openOODA GROUP CHANGER
================================================================================
```

**Sovereign GROUP CHANGER**  
*Updates primary and auxiliary group associations for filesystem paths with systemd-tmpfiles synthesis.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openOODA-tools.github.io/oochgrp/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oochgrp-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openOODA-tools.github.io/oochgrp/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openOODA-tools.github.io/oochgrp/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oochgrp-uninstall
# or: curl -fsSL https://openOODA-tools.github.io/oochgrp/uninstall.sh | bash
```

---

## 2. CLI Usage

```
oochgrp 0.2.0 (openOODA sovereign files & navigation)
usage: oochgrp [OPTION]... GROUP FILE...
  or:  oochgrp [OPTION]... --reference=RFILE FILE...

Change the group of each FILE to GROUP.

Options:
  -c, --changes          like verbose but report only when a change is made
  -f, --silent, --quiet  suppress most error messages
  -v, --verbose          output a diagnostic for every file processed
  -R, --recursive        operate on files and directories recursively
      --reference=RFILE  use RFILE's group rather than specifying a GROUP
  -h, --no-dereference   affect symbolic links instead of any referenced file
      --dry-run          simulate group changes without disk writes
      --tmpfiles         synthesize declarative systemd-tmpfiles rules
      --demo             run demonstration scenarios with synthetic fixtures
      --json             output formatted as JSON Lines
      --help             display this help and exit
      --version          output version information and exit
      --mcp              run as Model Context Protocol stdio server
```

---

## 3. Declarative systemd-tmpfiles Synthesis

Following pure systemd-native server architecture, `oochgrp` can emit declarative rules for `/etc/tmpfiles.d/*.conf`:

```bash
# Generate declarative non-recursive (z) and recursive (Z) rules:
oochgrp --tmpfiles systemd-journal /var/log/audit.log
oochgrp --tmpfiles -R users /srv/shared/workspace
```

Output:
```ini
# /etc/tmpfiles.d/oochgrp.conf - declarative group ownership
# Type Path Mode UID GID Age Argument
z /var/log/audit.log - - systemd-journal - -
```

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oochgrp` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

```bash
oochgrp --mcp
```

### Registered Tools
* **`chgrp_resolve`**: Resolve group name or numeric GID against `/etc/group` database.
* **`chgrp_inspect`**: Inspect filesystem path group ownership and GID.
* **`chgrp_plan`**: Plan group ownership change for path without disk modification.
* **`chgrp_tmpfiles`**: Synthesize declarative systemd-tmpfiles rule for path.
* **`chgrp_audit`**: Audit path group ownership against expected security baseline.

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
