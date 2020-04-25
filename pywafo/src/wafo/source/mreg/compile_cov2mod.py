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