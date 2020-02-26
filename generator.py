import sys
sys.path.insert(0, "./lib");
sys.path.append("./lib/merge")
from solc import compile_source, compile_files, link_code
import printLib as pl
import figletLib as fl
import merge1 as m1
import merge2 as m2
import merge3 as m3
import solcCompile as solc

fl.figletCli()
level = pl.levelCli()

if(int(level) == 3):
    nonExBug = pl.nonExploitableCli_Level3()
    exBug = pl.exploitableCli();
    l3m = m3.merge3(nonExBug,exBug)
    l3m.resultPrint()
    solc.solcCompile(l3m.result)
elif(int(level) == 2):
    exBug = pl.exploitableCli();
    nonExBug = pl.complexityCli()
    l2m = m2.merge2(nonExBug,exBug)
    l2m.resultPrint()
    solc.solcCompile(l2m.result)
else:
    exBug = pl.exploitableCli()
    nonExBug = pl.nonExploitableCli()
    l1m = m1.merge1(nonExBug,exBug)
    l1m.resultPrint()
    solc.solcCompile(l1m.result)

print("Generating Level : [" + level + "]")
print("Non-Exploitable Bug : ["+nonExBug+"]")
print("Exploitable Bug : ["+exBug+"]")

