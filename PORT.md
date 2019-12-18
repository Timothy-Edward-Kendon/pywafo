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

## ImportError: cannot import name 'PiecewisePolynomial' from 'scipy.interpolate'

```grep -rli 'PiecewisePolynomial' * | xargs -i@ sed -i 's/PiecewisePolynomial/PPoly/g' @```

## from scipy.misc.common import pade

```grep -rli 'scipy.misc.common' * | xargs -i@ sed -i 's/scipy.misc.common/scipy.interpolate/g' @```

# Final steps

By this point you should be able to import wafo, but with 2 user warnings

* C:\Appl\Anaconda3\lib\site-packages\wafo\spectrum\core.py:35: UserWarning: Compile the c_library.pyd again!
  warnings.warn('Compile the c_library.pyd again!')
* C:\Appl\Anaconda3\lib\site-packages\wafo\spectrum\core.py:40: UserWarning: Compile the cov2mod.pyd again!
  warnings.warn('Compile the cov2mod.pyd again!')

## Recompilation of c_library.pyd

1. Navigate to ```wafo/source/c_codes```. 
2. ```python setup.py build_src build_ext --inplace --compiler=mingw32```
3. Copy resulting pyd to ```wafo/```

## Recompilation of cov2mod.pyd 

1. Navigate to ```wafo/source/mreg```
2. Create file compile_cov2mod.py

``` # Based on compile_all
import os

def compile_all():   
    print('='*75)
    print('compiling cov2mod')
    print('='*75)
    
 
    files = ['dsvdc','mregmodule', 'intfcmod']
    compile1_format = 'gfortran -fPIC -c %s.f'
    format1 = '%s.o ' * len(files)
    for file in files:
        os.system(compile1_format % file)
    file_objects = format1  % tuple(files)
        
    os.system('f2py -m cov2mod  -c %s cov2mmpdfreg_intfc.f --compiler=mingw32' % file_objects)
     
    
if __name__=='__main__':
    compile_all()
```

3. ```python compile_cov2mod.py``` and copy resulting pyd to ```wafo/```

# TODO

Update repository files
