# Binary Waterfall for Linux

Linux installer for **Binary Waterfall**, a raw data media player originally created by Ella Jameson ([nimaid](https://github.com/nimaid)).

## Download

[**Download Binary Waterfall 3.7.0-1 for Linux (.deb, amd64)**](https://github.com/NursePandaz/binary-waterfall-linux/releases/download/v3.7.0-1/binary-waterfall_3.7.0-1_amd64.deb)

The installer is approximately 85 MB and targets Debian/Ubuntu-based distributions, including Linux Mint, on 64-bit Intel/AMD (amd64 / x86-64) computers. It is not an ARM package.

See [all releases](https://github.com/NursePandaz/binary-waterfall-linux/releases) for available downloads.

## Installation

1. Download the `.deb` installer above.
2. Open a terminal in the folder containing the downloaded file. If your browser saved it to Downloads:

   ```bash
   cd ~/Downloads
   ```

3. Install the package:

   ```bash
   sudo apt install ./binary-waterfall_3.7.0-1_amd64.deb
   ```

   Enter your password when prompted. APT will install any required dependencies available from your configured repositories.

4. Launch Binary Waterfall:

   ```bash
   binary-waterfall
   ```

Alternatively, open the downloaded `.deb` file with your distribution's package installer and choose **Install**.

### Uninstall

```bash
sudo apt remove binary-waterfall
```

## Credits and attribution

**Original creator: [nimaid](https://github.com/nimaid).** All credit for the original Binary Waterfall application belongs to nimaid and the upstream contributors.

- [Original Binary Waterfall source and documentation](https://github.com/nimaid/binary-waterfall)
- [Original project on itch.io](https://nimaid.itch.io/binary-waterfall)

This repository distributes the Linux installer; the original application is developed in the upstream project linked above.

The [upstream attribution instructions](https://github.com/nimaid/binary-waterfall#attribution) require credit when you use Binary Waterfall to make videos or other projects, including commercial projects. Include this statement in your video description or project references:

```text
Made with the help of Binary Waterfall:
https://github.com/nimaid/binary-waterfall
```

## Source and build instructions

See [BUILDING.md](BUILDING.md) for upstream source and Python build steps. **The exact modified source and packaging scripts for this 3.7.0-1 installer are not yet available here.** The automatic GitHub source archives contain repository documentation, not the application source.

## License

Binary Waterfall's upstream [GNU GPL version 3 license](LICENSE) is preserved in this repository. Original author: **Ella Jameson ([nimaid](https://github.com/nimaid))**. Dependencies retain their respective licenses. See [source availability](BUILDING.md#source-locations) for the current source gap.

## Verify your download

Run this in the folder containing the installer:

```bash
sha256sum binary-waterfall_3.7.0-1_amd64.deb
```

Expected SHA-256:

```text
ed4e3a95ffa38527b4d932aa961096e6c2b5839b6695dc7a4b7628ef5e4a9c9e
```

## Compatibility and testing

- Package architecture: amd64 (64-bit Intel/AMD).
- Original target: Linux Mint 22 / Ubuntu 24.04.
- Package metadata and SHA-256 have been inspected. A fresh installation, physical audio playback, and export tests for this exact installer have not been performed during this publication work.
- Tests reported for the separate 3.7.0-2 rebuild do not validate this 3.7.0-1 installer.

## Troubleshooting and support

- **Wrong architecture:** this installer requires amd64; it is not an ARM package.
- **Dependency installation errors:** use the `sudo apt install ./...deb` command above so APT can resolve the package's declared dependencies.
- **App does not open:** run `binary-waterfall` in a terminal and include the error text in an issue.
- **Audio/export problems:** the package declares FFmpeg, PulseAudio integration, and GStreamer plugins as dependencies. Include your distribution/version and whether the problem affects playback or export when reporting it.

[Report a Linux packaging issue](https://github.com/NursePandaz/binary-waterfall-linux/issues). Include the installer version, distribution/version, architecture, steps to reproduce, and relevant error text; remove personal file paths or other private details before posting.
