pragma solidity ^0.5.5;
pragma experimental ABIEncoderV2;

contract Abiv2 {
    
    uint256[2][2] public tmp_i;
    uint256[2][2] public fin_i;
    bytes temp;
    
    [Ground-Seed]

    function arrayCheck(uint256[2][2] memory a, uint256[2][2] memory b) internal returns (bool) {
        for (uint i=0; i<2; i++){
            for (uint j=0; j<2; j++){
                if (a[i][j] != b[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
     
    function answer() public returns (bool) {
        if (arrayCheck(tmp_i,fin_i)) {
            [Trigger-Seed]
            return true;
        }else {
            return false;
        }
    }
    
    [Function-Seed]

    function initialized(uint256[2][2] calldata s) external returns (uint256[2][2] memory) {
        tmp_i = s;
        temp = abi.encode(tmp_i);
        fin_i = abi.decode(temp, (uint256[2][2]));
        return abi.decode(temp, (uint256[2][2]));
   }

}