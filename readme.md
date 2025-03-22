## Yandex Music

A Flatpak package for the **native** Linux-version of the Yandex Music app.

```
flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak-builder --install --user --force-clean --install-deps-from=flathub build ru.yandex.music.yml
```