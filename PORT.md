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
