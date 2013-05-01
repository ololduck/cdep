# `cdep`

`cdep` is a very simple c depency parser. It generates dot syntax on `stdout`.

## Installation

I am assuming `~/bin` is in your `$PATH`.


```sh

wget -O ~/bin/cdep.py https://github.com/paulollivier/cdep/raw/master/cdep.py
chmod +x ~/bin/cdep.py
```

## Usage

General syntax:

```sh

cdep.py [pathtorootdir1 [...]] | dot -Tpng -o deps.png
```

Samples:

```sh

cdep.py dev/c/my_awesome_c_project | dot -Tpng -o dependencies.png
```

or

```sh

cd dev/c/my_awesome_c_project
cdep.py | dot -Tpng -o dependencies.png
```

You can then open the image with your preferred image viewer.

For more options about image format, please consult `dot`'s manpage.

## Uninstall

```sh

rm ~/bin/cdep.py
```

## LICENSE

Do whatever the fuck you want. Just made this to have a break in a C project.
