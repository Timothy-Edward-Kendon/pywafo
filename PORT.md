# Porting to Python 3 (Working Document)

## Use With Care

Either:

```2to3 --output-dir=python3-version/wafo -W -n python2-version/wafo```

Or for the confident

```2to3 -w wafo```

- The latter failed on some tutorial_scripts.
- print statements were already python3 compatible, but 2to3 will just add extra brackets


## No module named 'scipy.lib'

Change ```scipy.lib``` to ```scipy._lib```

```grep -rli 'scipy.lib' * | xargs -i@ sed -i 's/scipy.lib/scipy._lib/g' @```

## Cannot import name 'futil' from 'wafo.stats'

The futil.py is not part of scipy.stats anymore and is not in wafo.stats.

1. Get fortran file e.g. https://github.com/scipy/scipy-svn/blob/master/scipy/stats/futil.f
2. Compile, e.g. for windows 10 ```f2py -c futil.f -m futil --compiler=mingw32```. Note that if you are using a 64 bit Anaconda on Windows you will need to use a mingw64 build of the binaries e.g. https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/7.2.0/threads-posix/seh/x86_64-7.2.0-release-posix-seh-rt_v5-rev1.7z
3. Copy resulting pyd file to ```wafo.stats```

## ModuleNotFoundError: No module named 'numdifftools'

```conda install numdifftools```

## ImportError: cannot import name 'linspace' from 'numpy.lib.function_base'

```grep -rli 'numpy.lib.function_base' * | xargs -i@ sed -i 's/numpy.lib.function_base/numpy/g' @```

* Only occurs in interpolate.py.

## ImportError: cannot import name 'PiecewisePolynomial' from 'scipy.interpolate'

