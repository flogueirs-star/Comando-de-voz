[app]

title = Comando de Voz
package.name = comandovoz
package.domain = org.trmartins

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,RECORD_AUDIO

android.api = 35
android.minapi = 23

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
