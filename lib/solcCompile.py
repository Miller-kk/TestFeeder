from solc import compile_source, compile_files, link_code

def solcCompile(src):
    compiledSource = compile_source(src)
    key = list(compiledSource.keys())
    if(len(key) > 0):
        print("======================================After Compiling Code======================================\n\n")
        print("====================================== ABI Data ================================================")
        print(compiledSource[key[0]]['abi'])
        print("\n\n=================================== Binary Data ============================================")
        print(compiledSource[key[0]]['bin'])
        print("\n\n")
        
    else:
        print("Compiler Error")