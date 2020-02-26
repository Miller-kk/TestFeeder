pragma solidity ^0.4.3;

contract higherorderclean {
	uint48 public challengeCoin = 0;
	uint48 public random;

function higherorderclean() {
    random = uint48(now/10) % 10;
}

function challenge(uint48 _num) payable public returns (bool) {
    challengeCoin--;
    if(random < 10) {
        random = uint48(now/10);
        return true;
    }else {
        return false;
    }
}

}