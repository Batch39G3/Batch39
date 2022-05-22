const electionss = artifacts.require("election");

module.exports = function (deployer) {
  deployer.deploy(electionss);
};
