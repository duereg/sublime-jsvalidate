#JsValidate for Sublime Text 2

Check your JavaScript for syntax errors: [Esprima](http://esprima.org/) with everyone's favorite text editor: [Sublime Text 2](http://www.sublimetext.com/2)

**Prerequisites:** [Esprima](http://github.com/ariya/esprima) and [Sublime Package Control](http://wbond.net/sublime_packages/package_control/installation)

**Mac OS X:** Installing node with homebrew or macports is assumed. The path to esprima is hardcoded in this plugin as `/usr/local/bin:/opt/local/bin`. There is no reliable way to get the path from your environment.

**Linux:** Make sure esprima is in your environment path.

**Windows:** Installing node with the Windows Installer from nodejs.org is assumed.

##Install esprima with npm

    npm install -g esprima

##Install JsValidate with Package Control in Sublime Text 2

1. `command`-`shift`-`P` *or* `control`-`shift`-`P` in Linux/Windows*
2. type `install p`, select `Package Control: Install Package`
3. type `Js Validation`, select `JS Validation Using Esprima`

**Note:** Without Sublime Package Control, you could manually clone to Packages directory as 'JsValidate', exactly.

##Run JsValidate on an active JavaScript file in Sublime Text 2

- `control`-`shift`-`V` *or Tools/Contextual menus or the Command Palette*
- `F4` jump to next error row/column
- `shift`-`F4` jump to previous error row-column

**Note:** The `control`-`shift`-`V` shortcut changes the Build System on the current file to JsValidate, then Builds to run JsValidate on the file. You could alternatively set the Build System to Automatic and `command`-`B`/`control`-`B`/`F7`, but only on files that end with .js.

##Run JsValidate on save

Install [SublimeOnSaveBuild](https://github.com/alexnj/SublimeOnSaveBuild)
