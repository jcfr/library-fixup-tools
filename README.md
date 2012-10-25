Library Fixup Tools
===================

Overview
--------

Think of `library-fixup-tools` as a collection of scripts allowing to diagnostic issue related to MacOSX
packaging.

Usage
-----

Quick examples:

    $ ~/Dashboards/list_unfixed_libraries.py --library-directory ./_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.2.0-rc1-2012-10-24-macosx-amd64/Slicer.app/Contents/lib/Slicer-4.2/

    Analysis summary
     Total: 363 libraries
     Unfixed: 0 libraries

Simple.

Note also that passing the `--verbose` option will provide you with more details:

    $ ~/Dashboards/list_unfixed_libraries.py --library-directory ./_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.2.0-rc1-2012-10-24-macosx-amd64/Slicer.app/Contents/lib/Slicer-4.2/

    $ ~/Dashboards/list_unfixed_libraries.py --library-directory ./_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.2.0-rc1-2012-10-24-macosx-amd64/Slicer.app/Contents/lib/TclTk/ --verbose
    Found 0 files walking [./_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.2.0-rc1-2012-10-24-macosx-amd64/Slicer.app/Contents/lib/TclTk/] using [*.so] pattern
    Found 6 files walking [./_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.2.0-rc1-2012-10-24-macosx-amd64/Slicer.app/Contents/lib/TclTk/] using [*.dylib] pattern

    Analysis summary
     Total: 6 libraries
     Unfixed: 2 libraries

    List of unfixed libraries
     ./_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.2.0-rc1-2012-10-24-macosx-amd64/Slicer.app/Contents/lib/TclTk/lib/libtcl8.4.dylib
     ./_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.2.0-rc1-2012-10-24-macosx-amd64/Slicer.app/Contents/lib/TclTk/lib/libtk8.4.dylib

The option `--extra-verbose`

Installation
------------

1. [Download the script](https://raw.github.com/jcfr/library-fixup-tools/master/ list_unfixed_libraries.py).
2. Place it on your path. (I like to use `~/bin`)
3. Set it to be executable. (`chmod 755 ~/bin/list_unfixed_libraries.py`)


Contributing
------------

Once you've made your great commits:

1. [Fork][fk] library-fixup-tools
2. Create a topic branch - `git checkout -b my_branch`
3. Push to your branch - `git push origin my_branch`
4. Create an [Issue][is] with a link to your branch
5. That's it!


Meta
----

* Code: `git clone git://github.com/jcfr/library-fixup-tools.git`
* Home: <http://jcfr.github.com>
* Bugs: <http://github.com/jcfr/library-fixup-tools/issues>

License
-------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

[fk]: http://help.github.com/forking/
[is]: http://github.com/jcfr/HeaderToolkitDependencyWalker/issues
[itk]: http://itk.org
[vtk]: http://vtk.org
[ctk]: http://commontk.org

