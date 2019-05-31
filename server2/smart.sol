pragma solidity ^0.5.1;
pragma experimental ABIEncoderV2;

contract Owned {
    address public owner;


    constructor () public {
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender ==owner);
        _;
    }

    function transferOwnership(address newOwner) public  returns (address) {
        owner = newOwner;
        return owner;
    }

    function getOwner() public view returns (address) {
        return owner;
    }

}

contract FileHashStorage is Owned {
    struct File {
        address copyWriter;
        address owner;
        string name;
        uint size;
        uint price;
    }
    mapping(string => File) private files;
    mapping(address => string[]) private fileOwners;
    mapping(address => string[]) private fileCopy;
    //string[] public owners;
    //uint public ownerID = 0;

    /*
    owners = ["Jung", "Park", ...]
    fileOwners["Jung"] = ["0xABCD1234", "0xDEAD4321"] // Hashed file
    files["0xABCD1234"] = {
      name: "test_file.pdf",
      size: 154000 // Bytes
    }
    */




    function upload( string memory fileHash, string memory fileName, uint filePrice, uint fileSize) onlyOwner public {
      //  ownerID++;
        //owners.push(personName);
        File memory f = File(msg.sender,msg.sender, fileName, filePrice, fileSize);
        files[fileHash] = f;
        fileOwners[msg.sender].push(f.name);
        fileCopy[msg.sender].push(f.name);
    }

    function checkExist(string memory fileHash)  public view returns (bool) {
        if (files[fileHash].size > 0) {
            return true;
        }
        return false;
    }

    function trans(string memory fileHash)  public  returns (bool){
        address payable copyW;
        address payable owner2;
        uint price2;
        // (,owner2,copyW,,price2)=getFileInfo(fileHash);
        copyW=address(uint160(files[fileHash].copyWriter));
        owner2=address(uint160(files[fileHash].owner));
        price2=files[fileHash].price;

        uint256 bal = (msg.sender).balance;

        require(bal>=price2,"false");
        address payable to = owner2;
        address payable to2 = copyW;
        to.transfer(price2/2);
        to2.transfer(price2/2);
        files[fileHash].owner=msg.sender;

        return true;

    }


    // function getOwnerName(uint id)  public view returns (string memory) {
    //     return owners[id];
    // }

    function getFileInfo(string memory fileHash)  public view returns (string memory,address,address, uint, uint) {
        return (files[fileHash].name, files[fileHash].owner,files[fileHash].copyWriter, files[fileHash].size, files[fileHash].price);
    }
}
