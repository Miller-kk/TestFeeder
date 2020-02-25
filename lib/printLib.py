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
    exploitableBug = input("please pick Number Of Exploitable Side Vulnerability : ")
    return exploitableBug

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
    print("[2] DoubleShiftSizeOverflow")
    print("[3] ExpExponentCleanup")
    print("[4] NestedArrayFunctionCallDecoder")
    print("[5] SkipEmptyStringLiteral")
    print("[6] HighOrderByteCleanStorage")
    print("[7] Hidden State Update")
    print("[8] OneOfTwoConstructorsSkipped")
    print("[9] Uninitialised Struct")
    nonExploitableBug = input("Please Pick Number Of Non-Exploitable Side Vulnerability :")
    return nonExploitableBug

