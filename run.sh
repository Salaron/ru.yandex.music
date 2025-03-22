#!/bin/bash

WAYLAND_FLAGS=""
if [[ -e "$XDG_RUNTIME_DIR/$WAYLAND_SOCKET" || -e "$WAYLAND_DISPLAY" ]]; then
    WAYLAND_FLAGS+="--enable-wayland-ime --ozone-platform-hint=wayland"
fi

zypak-wrapper.sh /app/yandexmusic/yandexmusic $WAYLAND_FLAGS "$@"