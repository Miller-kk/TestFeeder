def levelCli():
    print("################Level Check################")
    print("[1] Level1")
    print("[2] Level2")
    print("[3] Level3")
    level = input("Please Pick Number Of Generating Level : ")
    return level

def exploitableCli():
    print("\n")
    print("################Exploitable Side Vulnerability################")
    print("[1] IntegerOverflow")
    print("[2] IntegerUnderflow")
    print("[3] Reentrancy")
    print("[4] BadRandomness")
    print("[5] Selfdestruct")
    exploitableBug = input("Please pick Number Of Exploitable Side Vulnerability : ")
    return exploitableBug

def complexityCli():
    print("\n\n")
    print("################Data Dependency Stage################")
    print("How much do you need variable aggregation?")
    print("[1] Stage1")
    print("[2] Stage2")
    print("[3] Stage3")
    stage = input("Please pick Number Of Complexity Stage : ")
    return stage

def nonExploitableCli():
    print("\n\n")
    print("################Non-Exploitable Side Vulnerability################")
    print("[1] If-Condition")
    print("[2] While-Loop")
    print("[3] For-Loop")
    nonExploitableBug = input("Please Pick Number Of Non-Exploitable Side Vulnerability :")
    return nonExploitableBug

def nonExploitableCli_Level3():
    print("\n\n")
    print("################Non-Exploitable Side Vulnerability################")
    print("[1] ABIEncoderV2PackedStorage")
    print("[2] ExpExponentCleanup")
    print("[3] HighOrderByteCleanStorage")
    print("[4] Uninitialised Struct")
    nonExploitableBug = input("Please Pick Number Of Non-Exploitable Side Vulnerability :")
    return nonExploitableBug

