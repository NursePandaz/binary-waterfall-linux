# Source and build status

## Source locations

Original application: [nimaid/binary-waterfall](https://github.com/nimaid/binary-waterfall), by Ella Jameson (nimaid).

The exact modified source and packaging scripts for the published `3.7.0-1_amd64.deb` have not yet been recovered and committed here. Upstream source alone is not a verified reproduction of this Linux installer. GitHub's automatically generated source ZIP/tar archives currently contain this repository's documentation, not the application source.

An earlier development session produced a separate `3.7.0-2` rebuild and source archive. That is a different build and must not be presented as the source for the published `3.7.0-1` installer.

## Building upstream Python distributions

These commands describe a conventional Python source/wheel build of the upstream application, not a rebuild of this repository's Debian installer. They have not been run or validated for this release.

```bash
git clone https://github.com/nimaid/binary-waterfall.git
cd binary-waterfall
# Check out the upstream revision you intend to build.
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip build
python -m build
```

The upstream project uses setuptools and declares its dependencies in `pyproject.toml`. Desktop/Qt runtime libraries and FFmpeg may also be needed to run the application. Record the chosen commit, Python version, and dependency versions for any build you distribute.

## Reproducing the Linux installer

Pending recovery of the exact Linux source, patches, dependency versions, and packaging scripts. No reproducible `.deb` build command is claimed at this time.

## License and source distribution

The upstream license is preserved verbatim in [LICENSE](LICENSE). Retain upstream copyright and attribution notices. Adding a license copy or an upstream link does not supply the missing modified source or establish a complete source distribution for the installer.
