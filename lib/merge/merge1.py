import random
import os

class merge1:
    def __init__(self, t1, t2):
        self.functionTarget = "[Function-Seed]"
        self.groundTarget = "[Ground-Seed]"
        self.triggerTarget = "[Trigger-Seed]"
        self.whileTarget = "[While-Seed]"
        self.randomTarget = "randomNumber"
        self.randomTargetNew = random.randint(2, 20)

        ## 각 파일의 base path
        self.if_condition_path = "./samples/Level1/Non-Exploitable/if-condition/"
        self.for_loop_path = "./samples/Level1/Non-Exploitable/for-loop/"
        self.while_loop_path = "./samples/Level1/Non-Exploitable/while-loop/"
        self.expolitable_path ="./samples/Level1/Exploitable/"

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
            self.functionTargetNew = open(self.if_condition_path+"functionSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew))
            self.groundTargetNew = open(self.if_condition_path+"groundSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew))
            self.whileTargetNew = ""
            self.triggerTargetNew = open(self.if_condition_path+"triggerSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew))
            self.result = self.exploitableBugSource.replace(self.functionTarget, self.functionTargetNew).replace(self.groundTarget, self.groundTargetNew).replace(self.whileTarget, self.whileTargetNew).replace(self.triggerTarget, self.triggerTargetNew)
        elif(int(t1) == 2):
            self.whileTargetNew = open(self.while_loop_path + "whileSeed.sol").read()
            self.triggerTargetNew = open(self.while_loop_path + "triggerSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew))
            self.functionTargetNew = ""
            self.groundTargetNew = open(self.while_loop_path+"groundSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew))
            self.result = self.exploitableBugSource.replace(self.functionTarget, self.functionTargetNew).replace(self.groundTarget, self.groundTargetNew).replace(self.whileTarget, self.whileTargetNew).replace(self.triggerTarget, self.triggerTargetNew)
        else:
            self.functionTargetNew = ""
            self.groundTargetNew = open(self.for_loop_path+"groundSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew))
            self.whileTargetNew = ""
            self.triggerTargetNew = open(self.for_loop_path+"triggerSeed.sol").read().replace(str(self.randomTarget), str(self.randomTargetNew))
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
