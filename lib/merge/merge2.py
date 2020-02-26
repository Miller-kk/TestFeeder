import random
import os
import sys
sys.path.insert(0, "./lib")
import opGenerator as opg

class merge2:
    def __init__(self, t1, t2):
        self.functionTarget = "[Function-Seed]"
        self.groundTarget = "[Ground-Seed]"
        self.triggerTarget = "[Trigger-Seed]"
        self.whileTarget = "[While-Seed]"
        self.randomTarget = "randomNumber"
        self.relOp = "[relativeOp]"
        self.arithOp1 = "[arithOp1]"
        self.arithOp2 = "[arithOp2]"
        self.arithOp3 = "[arithOp3]"
        self.randomTargetNew = random.randint(2, 20)
        self.randomTargetNew2 = random.randint(2,100)

        ## 각 파일의 base path
        self.stage1_path = "./samples/Level2/Non-Exploitable/stage1/"
        self.stage2_path = "./samples/Level2/Non-Exploitable/stage2/"
        self.stage3_path = "./samples/Level2/Non-Exploitable/stage3/"
        self.expolitable_path ="./samples/Level2/Exploitable/"

        if(int(t2) == 1):
            integerOverflowStr = open(self.expolitable_path+"integerOverflow.sol").read()
            self.integration(t1,integerOverflowStr)
        elif(int(t2) == 2):
            integerUnderflowStr = open(self.expolitable_path+"integerUnderflow.sol").read()
            self.integration(t1,integerUnderflowStr)
        elif(int(t2) == 3):
            reentrancyStr = open(self.expolitable_path+"reentrancy.sol").read()
            self.integration(t1,reentrancyStr)
        elif(int(t2) == 4):
            self.badrandomness = ""
        else:
            selfdestructStr = open(self.expolitable_path+"selfdestruct.sol").read()
            self.integration(t1,selfdestructStr)
    

    def integration(self, t1, src):
        self.exploitableBugSource = src
        if(int(t1) == 1):
            (relIndex,relOp) = opg.relOpGen()
            self.relOpNew = relOp
            self.arithOp1New = opg.arithOpGen(relIndex)
            self.functionTargetNew = ""
            self.groundTargetNew = open(self.stage1_path+"groundSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew)).replace(str(self.randomTarget)+"2", str(self.randomTargetNew2)).replace(self.arithOp1,self.arithOp1New)
            self.whileTargetNew = ""
            self.triggerTargetNew = open(self.stage1_path+"triggerSeed.sol").read().replace(self.relOp, self.relOpNew)
            self.result = self.exploitableBugSource.replace(self.functionTarget, self.functionTargetNew).replace(self.groundTarget, self.groundTargetNew).replace(self.whileTarget, self.whileTargetNew).replace(self.triggerTarget, self.triggerTargetNew)
        elif(int(t1) == 2):
            (relIndex,relOp) = opg.relOpGen()
            self.relOpNew = relOp
            self.arithOp1New = opg.arithOpGen(relIndex)
            self.arithOp2New = opg.arithOpGen(relIndex)
            self.whileTargetNew = ""
            self.triggerTargetNew = open(self.stage2_path+"triggerSeed.sol").read().replace(self.relOp, self.relOpNew)
            self.functionTargetNew = ""
            self.groundTargetNew = open(self.stage2_path+"groundSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew)).replace(str(self.randomTarget)+"2", str(self.randomTargetNew2)).replace(self.arithOp1,self.arithOp1New).replace(self.arithOp2,self.arithOp2New)
            self.result = self.exploitableBugSource.replace(self.functionTarget, self.functionTargetNew).replace(self.groundTarget, self.groundTargetNew).replace(self.whileTarget, self.whileTargetNew).replace(self.triggerTarget, self.triggerTargetNew)
        else:
            (relIndex,relOp) = opg.relOpGen()
            self.relOpNew = relOp
            self.arithOp1New = opg.arithOpGen(relIndex)
            self.arithOp2New = opg.arithOpGen(relIndex)
            self.arithOp3New = opg.arithOpGen(relIndex)
            self.functionTargetNew = ""
            self.groundTargetNew = open(self.stage3_path+"groundSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew)).replace(str(self.randomTarget)+"2", str(self.randomTargetNew2)).replace(self.arithOp1,self.arithOp1New).replace(self.arithOp2,self.arithOp2New).replace(self.arithOp3,self.arithOp3New)
            self.whileTargetNew = ""
            self.triggerTargetNew = open(self.stage3_path+"triggerSeed.sol").read().replace(self.relOp, self.relOpNew)
            self.result = self.exploitableBugSource.replace(self.functionTarget, self.functionTargetNew).replace(self.groundTarget, self.groundTargetNew).replace(self.whileTarget, self.whileTargetNew).replace(self.triggerTarget, self.triggerTargetNew)

    
    def resultPrint(self):
        print("========================================Result========================================")
        print("\n")
        print("==============================Original Exploitable Source==============================")
        print(self.exploitableBugSource)
        print("\n")
        print("==============================Original Non-Exploitable Source==============================")
        print("#functionSeed")
        print(self.functionTargetNew)
        print("\n")
        print("#groundSeed")
        print(self.groundTargetNew)
        print("\n")
        print("#triggerSeed")
        print(self.triggerTargetNew)
        print("\n")
        print("#whileSeed")
        print(self.whileTargetNew)
        print("\n")

        print("==============================Combination==============================")
        print(self.result)
