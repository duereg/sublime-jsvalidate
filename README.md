#JsValidate for Sublime Text

Check your JavaScript for syntax errors: [Esprima](http://esprima.org/) with everyone's favorite text editor: [Sublime Text 2](http://www.sublimetext.com/2)

**Prerequisites:** [EsValidate](http://github.com/duereg/esvalidate) and [Sublime Package Control](http://wbond.net/sublime_packages/package_control/installation)

**Mac OS X:** Installing node with homebrew or macports is assumed. The path to esvalidate is hardcoded in this plugin as `/usr/local/share/npm/bin:/usr/local/bin:/opt/local/bin`. There is no reliable way to get the path from your environment.

**Linux:** Make sure esvalidate is in your environment path.

**Windows:** Installing node with the Windows Installer from nodejs.org is assumed.

##Install esvalidate with npm

    npm install -g esvalidate

##Install JsValidate with Package Control in Sublime Text 2

1. `command`-`shift`-`P` *or* `control`-`shift`-`P` in Linux/Windows*
2. type `install p`, select `Package Control: Install Package`
3. type `JsValidate`, select `JsValidate`

**Note:** Without Sublime Package Control, you could manually copy this project to your Packages directory as 'JsValidate'.

##Run JsValidate on an active JavaScript file in Sublime Text

- `control`-`shift`-`V` *or Tools/Contextual menus or the Command Palette*
- `F4` jump to next error row/column
- `shift`-`F4` jump to previous error row-column

##Settings

* Navigate to **Preferences > Package Settings > JsValidate > Settings - Default**.
* To preserve custom settings:
  * copy default settings to **Preferences > Package Settings > JsValidate > Settings - User**
  * modify them to your requirements

##Run JsValidate on save

By default, JsValidate does not run on save. To change, simply change the setting `run_on_save` for the project to `true`.

##Error: unknown report format sublime.

Seeing this error means you are using an outdated version of [EsValidate](http://github.com/duereg/esvalidate). Update to the latest version and this error should go away.  
