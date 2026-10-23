# Binary Waterfall for Linux

A raw data media player originally created by **Ella Jameson ([nimaid](https://github.com/nimaid))**.
This repository contains the original application source with documented Linux changes,
Debian packaging, and tests. The upstream **GPL v3** license is preserved in [LICENSE](LICENSE).

## Download and install

[**Download 3.7.0-3 (.deb)**](https://github.com/NursePandaz/binary-waterfall-linux/releases/download/v3.7.0-3/binary-waterfall_3.7.0-3_all.deb)

Target: Linux Mint 22 / Ubuntu 24.04 with Python 3.12. Only x86-64 has been tested.
APT installs system dependencies, so an internet connection may be needed during installation.

```bash
cd ~/Downloads
sudo apt install ./binary-waterfall_3.7.0-3_all.deb
binary-waterfall
```

Alternatively open the downloaded package with your distribution's package installer.

Uninstall:

```bash
sudo apt remove binary-waterfall
```

## Source, build and verification

[Build instructions](BUILDING.md) · [Linux changes and upstream revision](UPSTREAM.md) · [Test results](TESTING.md)

The installer contains the application Python source directly. Every installed application
source/resource file is checked against this repository with `packaging/linux/verify-payload.py`.
The release tag and source archive identify the source for the installer.

Download `SHA256SUMS` from the [release page](https://github.com/NursePandaz/binary-waterfall-linux/releases/tag/v3.7.0-3),
place it next to the downloaded assets, and check them with:

```bash
sha256sum --ignore-missing -c SHA256SUMS
```

**Version distinction:** this new 3.7.0-3 release replaces the older 3.7.0-1 frozen installer.
It does not claim to reproduce that older binary. The missing 3.7.0-2 archive is not used.

## Troubleshooting

Run `binary-waterfall` in a terminal to capture startup errors. Use APT for installation
so dependencies are resolved. Python 3.13+ is not supported by this release.
Physical audio playback has not been verified; see [testing limitations](TESTING.md).

[Report Linux packaging issues](https://github.com/NursePandaz/binary-waterfall-linux/issues)
with your package version, distribution, architecture, reproduction steps and error text.
Remove private information before posting.

## Credits and license

Original author: **Ella Jameson (nimaid)** and upstream contributors.

- [Original source and documentation](https://github.com/nimaid/binary-waterfall)
- [Original itch.io page](https://nimaid.itch.io/binary-waterfall)
- [GPL v3 license](LICENSE)

Linux changes dated October 22, 2026 are described in [UPSTREAM.md](UPSTREAM.md).
System dependencies retain their respective licenses. GPL v3 permits commercial use;
this repository adds no noncommercial restriction.

The upstream README requests the following attribution in videos or projects made with Binary Waterfall:

```text
Made with the help of Binary Waterfall:
https://github.com/nimaid/binary-waterfall
```
