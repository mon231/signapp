# signapp
Corss-Platform script used to sign APK files <br/>
<br />
*NOTE* that you should use this tool for debugging / educational purposes only! <br />
*NOTE* that you must accept the LICENSE of the tools listed in the [requirements](#Requirements) section

## Installation
Simply run:
> pip install signapp --upgrade && signapp_fetch_tools

Make sure to have python scripts folder in your path, <br/>
And use the correct version of pip for python3

## Usage
> signapp -a <original_apk> -o <output_apk>

## Recommended Projects
I'd like to recommend my other projects here, [`buildapp`](https://github.com/mon231/buildapp) and [`apkmod`](https://github.com/mon231/apkpatcher) <br />
[`buildapp`](https://github.com/mon231/buildapp) is used to recompile and resign an apk that was originally decompiled by [`apktool`](https://ibotpeaches.github.io/Apktool/install/) <br />
[`apkmod`](https://github.com/mon231/apkpatcher) is used to inject [frida js-script](https://frida.re/docs/javascript-api/) into an apk

## Requirements
The project uses these tools (can be fetched using `signapp_fetch_tools` after `pip install signapp`):
- android SDK tools ([download build_tools](https://dl.google.com/android/repository/build-tools_r33-windows.zip), [download platform_tools](https://dl.google.com/android/repository/platform-tools_r34.0.1-windows.zip))
    - adb (default at SDK\platform_tools, only required if `-i` flag is used)
    - zipalign (default at SDK\build_tools)
    - apksigner (default at SDK\build_tools)
