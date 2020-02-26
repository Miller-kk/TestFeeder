pragma solidity ^0.4.24;
contract GuessNumber {
    [Ground-Seed]
    uint public lastPlayed;
    

    struct GuessHistory {
        address player;
        uint256 number; 
        
    }
    
    function GuessNumber(uint256 _num) public payable { 
        require(_num <=10); 
	        GuessHistory guessHistory; 
	        guessHistory.player = msg.sender; 
	        guessHistory.number = _number;
            [Trigger-Seed]
            lastPlayed = now; 
    }
    
    [Function-Seed]
}