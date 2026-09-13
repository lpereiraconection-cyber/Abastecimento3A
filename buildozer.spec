[app]
# (str) Title of your application
title = Abastecimento 3A
# (str) Package name
package.name = abastecimento3a
# (str) Package domain (needed for android/ios packaging)
package.domain = com.kartazen
# (str) Source code where main.py live
source.dir = .
# (str) Main filename
source.main = main.py
# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas
# (list) List of inclusions using pattern matching
# source.include_patterns = assets/*,images/*.png
# (str) Application version
version = 1.0
# (list) List of requirements
requirements = python3,kivy
# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait
# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

[buildozer]
# (int) Log level (0 = error only, 1 = error + warning, 2 = error + info, 3 = error + debug)
log_level = 2
# (bool) Warn about obsolete buildozer.spec options
warn_on_root = 1

[android]
# (str) Android app theme, optional
android.api = 35
android.minapi = 23
android.ndk = 27c
android.accept_sdk_license = True
# Required permission to open external links
android.permissions = INTERNET
# If the device doesn't have a browser capable of handling the URL, this is still harmless.

# Uncomment and set after creating an original icon:
# icon.filename = %(source.dir)s/icon.png

[android.gradle_dependencies]

[buildozer]
log_level = 2
warn_on_root = 1
