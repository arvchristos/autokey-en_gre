# Autokey en-gre utility
A tool for those times writing the right things in wrong language.

Ever typed a whole sentence in English instead of your language? Then this tool is for you!

Currently supporting: 
* EN ↔ EL

![](https://raw.githubusercontent.com/arvchristos/autokey-en_gre/master/metadata/galeano.gif)

## Installation
### Requirements
This script is developed for the awesome [autokey]() utility. Therefore, autokey should be installed.

#### Install via pip
```
pip3 install autokey
# or, if you want the latest from this repository,
pip3 install --user git+https://github.com/autokey/autokey
```

#### Install using apt on debian
```
sudo add-apt-repository ppa:sporkwitch/autokey
sudo apt update
sudo apt install autokey-gtk
# Or alternatively, to install the Qt5 based GUI:
sudo apt install autokey-qt
```

For more autokey installation methods navigate to [autokey's repo](https://github.com/autokey/autokey#installation)

### Install en_gre
After installing autokey, open the Autokey utility. Then create a new script using `New->Script` and give it a descriptive name. Afterwards paste the code from the `engre.py` to the script code and define a hotkey for this script to be triggered (e.g. <CTRL> + <ALT> + G).
  
 ## Usage
 1. Write text in wrong layout (easy?).
 2. Select the wrong text previously typed.
 3. Press the defined Hotkey form Autokey.
 4. Celebrate
