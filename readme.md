## Yandex Music - Flatpak

This is a Flatpak package for the **native** Linux version of the Yandex Music app.

### Installation

Download the Flatpak bundle from Releases page and install it.

```
flatpak install ./ru.yandex.music.flatpak
```

### Build

```
git clone https://github.com/Salaron/ru.yandex.music
cd ru.yandex.music
flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak-builder --install --user --force-clean --install-deps-from=flathub build ru.yandex.music.yml
```
