import random
import os

class merge3:
    def __init__(self, t1, t2):
        self.functionTarget = "[Function-Seed]"
        self.groundTarget = "[Ground-Seed]"
        self.triggerTarget = "[Trigger-Seed]"
        self.whileTarget = "[While-Seed]"
        self.pragmaTarget = "[Pragma-Seed]"
        self.randomTarget = "randomNumber"
        self.randomTargetNew = random.randint(2, 20)

        
        ## 각 파일의 base path
        self.abi2_path = "./samples/Level3/Non-Exploitable/abiv2/"
        self.exponential = "./samples/Level3/Non-Exploitable/exponential/"
        self.higherorderclean = "./samples/Level3/Non-Exploitable/higherorderclean/"
        self.uninitialize = "./samples/Level3/Non-Exploitable/uninitialize/"
        self.expolitable_path ="./samples/Level3/Exploitable/"

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
            self.randomTargetNew2 = random.randint(2, 100)
            self.randomTargetNew3 = random.randint(2, 100)
            self.randomTargetNew4 = random.randint(2, 20)
            self.functionTargetNew = open(self.abi2_path+"functionSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew)).replace(str(self.randomTarget)+"2", str(self.randomTargetNew2)).replace(str(self.randomTarget)+"3", str(self.randomTargetNew3)).replace(str(self.randomTarget)+"4", str(self.randomTargetNew4))
            self.groundTargetNew = open(self.abi2_path+"groundSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew))
            self.whileTargetNew = ""
            self.pragmaTargetNew = open(self.abi2_path+"pragmaSeed.sol").read()
            self.triggerTargetNew = open(self.abi2_path+"triggerSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew))
            self.result = self.exploitableBugSource.replace(self.functionTarget, self.functionTargetNew).replace(self.groundTarget, self.groundTargetNew).replace(self.whileTarget, self.whileTargetNew).replace(self.triggerTarget, self.triggerTargetNew).replace(self.pragmaTarget,self.pragmaTargetNew)
        elif(int(t1) == 2):
            self.functionTargetNew = open(self.exponential+"functionSeed.sol").read()
            self.groundTargetNew = ""
            self.whileTargetNew = ""
            self.pragmaTargetNew = open(self.exponential+"pragmaSeed.sol").read()
            self.triggerTargetNew = open(self.exponential + "triggerSeed.sol").read()
            self.result = self.exploitableBugSource.replace(self.functionTarget, self.functionTargetNew).replace(self.groundTarget, self.groundTargetNew).replace(self.whileTarget, self.whileTargetNew).replace(self.triggerTarget, self.triggerTargetNew).replace(self.pragmaTarget,self.pragmaTargetNew)
        elif(int(t1) == 3):
            self.functionTargetNew = open(self.higherorderclean+"functionSeed.sol").read()
            self.groundTargetNew = open(self.higherorderclean+"groundSeed.sol").read()
            self.whileTargetNew = ""
            self.pragmaTargetNew = open(self.higherorderclean+"pragmaSeed.sol").read()
            self.triggerTargetNew = open(self.higherorderclean+"triggerSeed.sol").read()
            self.result = self.exploitableBugSource.replace(self.functionTarget, self.functionTargetNew).replace(self.groundTarget, self.groundTargetNew).replace(self.whileTarget, self.whileTargetNew).replace(self.triggerTarget, self.triggerTargetNew).replace(self.pragmaTarget,self.pragmaTargetNew)
        else:
            self.functionTargetNew = ""
            self.groundTargetNew = open(self.uninitialize+"groundSeed.sol").read()
            self.whileTargetNew = open(self.uninitialize+"whileSeed.sol").read()
            self.pragmaTargetNew = open(self.uninitialize+"pragmaSeed.sol").read()
            self.triggerTargetNew = open(self.uninitialize + "triggerSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew))
            self.result = self.exploitableBugSource.replace(self.functionTarget, self.functionTargetNew).replace(self.groundTarget, self.groundTargetNew).replace(self.whileTarget, self.whileTargetNew).replace(self.triggerTarget, self.triggerTargetNew).replace(self.pragmaTarget,self.pragmaTargetNew)
    
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
