pragma solidity ^0.4.24;
contract exponential {
    
    mapping(address => uint256) balanceOf;
    
    [Ground-Seed]

    constructor(uint256 init) {
        balanceOf[msg.sender] = init;
    }
    
    function tryNumber(uint256 _amount, uint256 _num) public returns (bool) {
            if (f() != 0){ 
                [Trigger-Seed]
                return true;
            }else{
                return false;
            }
    }
    
    function f() public pure returns(uint8 x) {
        uint8 y = uint8(2) ** uint8(8);
        return 0 ** y; // Non-Exploitable Bug
    }

    [Function-Seed]
    
}