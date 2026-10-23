# Binary Waterfall for Linux

Linux installer for **Binary Waterfall**, a raw data media player originally created by [nimaid](https://github.com/nimaid).

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
