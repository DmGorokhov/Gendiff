## The semantic JSON and YAML compare tool
\
[![Actions Status](https://github.com/DmGorokhov/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/DmGorokhov/python-project-50/actions)
[![Github Actions Status](https://github.com//DmGorokhov/python-project-50/workflows/Python%20CI/badge.svg)](https://github.com//DmGorokhov/python-project-50/actions/pyci.yaml)
[![Maintainability](https://api.codeclimate.com/v1/badges/c3a3a47e719879b49eb3/maintainability)](https://codeclimate.com/github/DmGorokhov/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c3a3a47e719879b49eb3/test_coverage)](https://codeclimate.com/github/DmGorokhov/python-project-50/test_coverage)

### About:
Gendiff is cli-utility for comparing two files JSON or YAML formats. Also it can be used as a library. Difference between two files displaying in console output in two formats at option: stylish(by default) or plain. In addition it's possible to dump file with comparison result in JSON format.

### Requirements:

* Python >= 3.10
* Poetry 1.2.2
* Pyyaml >= 6.0
* Make (is used to run a game through console-command)

### How to install:
---
#### With the use of pip:
```
python3 -m pip install --user git+https://github.com/DmGorokhov/python-project-50.git
```

#### Download from git repository:
```
git clone https://github.com/DmGorokhov/python-project-50.git
Make install          # install poetry for dependency management and packaging
Make build            # create package in dist/
Make package-install  # install package
```

### Usage examples:
* Compare two plain *.json files
[![asciicast](https://asciinema.org/a/553733.svg)](https://asciinema.org/a/553733)
* Compare two plain *.yaml files
[![asciicast](https://asciinema.org/a/555851.svg)](https://asciinema.org/a/555851)
* Compare two nested files
[![asciicast](https://asciinema.org/a/569167.svg)](https://asciinema.org/a/569167)
* Plain format of output
[![asciicast](https://asciinema.org/a/569582.svg)](https://asciinema.org/a/569582)
* JSON format of output to file
[![asciicast](https://asciinema.org/a/570346.svg)](https://asciinema.org/a/570346)