pragma solidity ^0.4.2;
pragma experimental ABIEncoderV2;

/*
Election contract that allows the owner to issue voting rights
to anybody and also end the election and announce results
*/
contract election {

    struct Candidate {
        string name;
        uint voteCount;
        string region;
        string party;
    }

    struct Voter {
        bool authorized;
        bool voted;
        uint vote;
    }
 ////////////////////////////////////////////////////////////////////////////  

/////////////////////////////////////////////////////////////////////////////
  uint number=0;
  struct verify{
        uint voted;
        string adhaar;
        }
verify [] public verif_lst;


/// add user if he has not voted
  function aadhar_user(string _adharr) ownerOnly public {
      uint a;
      for (uint i=0;i<verif_lst.length;i++){
        if (keccak256(bytes(verif_lst[i].adhaar)) == keccak256(bytes(_adharr))){
                    a=1;
  }}
  if (a!=1){
    verif_lst.push(verify(1,_adharr));
  }
  }
//get user status 


  function get_adhaar_status(string _adharr) ownerOnly public view returns (string) {
    uint a;
      for (uint i=0;i<verif_lst.length;i++){
        if (keccak256(bytes(verif_lst[i].adhaar)) == keccak256(bytes(_adharr))){
                    a=1;
  }}
   if (a==1){
    return "You Have already Voted";
  }
  else{
    return "Not Voted";
  }

      }



    //////////////////////////////////////////////////////////////////////////////////////
    

    address public owner;
    string public electionName;

    mapping(address => Voter) public voters;
    Candidate[] public candidates;

    event ElectionResult(string candidateName, uint voteCount,string region,string party);

    modifier ownerOnly() {
        require(msg.sender == owner);
        _;
    }

    function election() public {
        owner = msg.sender;
        
    }

    function addCandidate(string name,string region,string party) ownerOnly public {
        candidates.push(Candidate(name, 0,region,party));
    }

    function authorize(address person) ownerOnly public {
        voters[person].authorized = true;
    }

    function vote(string _cname,string _region,string _party) public {
        //make sure voter is authorized and has not already voted
                
        require(!voters[msg.sender].voted);
        require(voters[msg.sender].authorized);
        uint  voteIndex=0;
                
        //get index
        for (uint i=0; i < candidates.length; i++){
                if(keccak256(bytes(candidates[i].region)) == keccak256(bytes(_region))){
                  if(keccak256(bytes(candidates[i].name)) == keccak256(bytes(_cname))){
                    if(keccak256(bytes(candidates[i].party)) == keccak256(bytes(_party))){
                      voteIndex=i;}
                  }}
         }
       
        voters[msg.sender].vote = voteIndex;
        voters[msg.sender].voted = true;

        //increase candidate vote count by 1
       
        candidates[voteIndex].voteCount += 1;
    }
    
         //////////////////////////////////////////////////////////
function get_no_candidates() view public returns (uint) {
        return candidates.length;
}

function end() ownerOnly public {
        //announce each candidates results
        for(uint i=0; i < candidates.length; i++) {

            emit ElectionResult(candidates[i].name, candidates[i].voteCount,candidates[i].region,candidates[i].party);
        }

        //destroy the contract
        selfdestruct(owner);
    }
}