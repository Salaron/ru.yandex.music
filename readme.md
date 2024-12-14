## Yandex Music

<!-- собранный на коленке -->

A Flatpak package for the **native** Linux version of the Yandex Music app.

### Installation

WIP

### Notes

- Unlike the official Windows version, this package uses a newer version of Electron to add Wayland support, so expect bugs.
- Mpris support out of the box.
- DevTools enabled by default.
- Tray icon works.

### Build

#### Install required dependencies

##### Fedora

```bash
sudo dnf install flatpak flatpak-builder node npm python3
```

#### Build package

```bash
flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak-builder --install --user --force-clean --install-deps-from=flathub build ru.yandex.music.yml
```

### How to update Electron version

Install flatpak-node-generator:

```bash
git clone https://github.com/flatpak/flatpak-builder-tools /tmp/flatpak-builder-tools
cd /tmp/flatpak-builder-tools/node
pip install .
```

Update Electron and generate new `generated-sources.json`:

```bash
npm upgrade electron --package-lock-only
flatpak-node-generator npm package-lock.json
```