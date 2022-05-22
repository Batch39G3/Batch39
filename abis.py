from distutils.command import build



def abis():
  s=""" 
  [
    {
      "constant": true,
      "inputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "candidates",
      "outputs": [
        {
          "name": "name",
          "type": "string"
        },
        {
          "name": "voteCount",
          "type": "uint256"
        },
        {
          "name": "region",
          "type": "string"
        },
        {
          "name": "party",
          "type": "string"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "verif_lst",
      "outputs": [
        {
          "name": "voted",
          "type": "uint256"
        },
        {
          "name": "adhaar",
          "type": "string"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "electionName",
      "outputs": [
        {
          "name": "",
          "type": "string"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "name": "voters",
      "outputs": [
        {
          "name": "authorized",
          "type": "bool"
        },
        {
          "name": "voted",
          "type": "bool"
        },
        {
          "name": "vote",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "candidateName",
          "type": "string"
        },
        {
          "indexed": false,
          "name": "voteCount",
          "type": "uint256"
        },
        {
          "indexed": false,
          "name": "region",
          "type": "string"
        },
        {
          "indexed": false,
          "name": "party",
          "type": "string"
        }
      ],
      "name": "ElectionResult",
      "type": "event"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_adharr",
          "type": "string"
        }
      ],
      "name": "aadhar_user",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_adharr",
          "type": "string"
        }
      ],
      "name": "get_adhaar_status",
      "outputs": [
        {
          "name": "",
          "type": "string"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "name",
          "type": "string"
        },
        {
          "name": "region",
          "type": "string"
        },
        {
          "name": "party",
          "type": "string"
        }
      ],
      "name": "addCandidate",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "person",
          "type": "address"
        }
      ],
      "name": "authorize",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_cname",
          "type": "string"
        },
        {
          "name": "_region",
          "type": "string"
        },
        {
          "name": "_party",
          "type": "string"
        }
      ],
      "name": "vote",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "get_no_candidates",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "end",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]
  
  """
  return s


