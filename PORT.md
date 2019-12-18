# Porting to Python 3 (Working Document)

## No module named 'scipy.lib'

Change ```scipy.lib``` to ```scipy._lib```

```grep -rli 'scipy.lib' * | xargs -i@ sed -i 's/scipy.lib/scipy._lib/g' @```
