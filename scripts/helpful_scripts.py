from brownie import network, config, accounts, MockV3Aggregator, Contract


FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


# When passing an index we will just load the accounts array
# If we pass and ID were going to be use accounts.load
def get_account(index=None, id=None):
    # accounts[0]
    # accounts.add("env")
    # accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


contract_to_mock = {"eth_usd_price_feed": MockV3Aggregator,
"vrf_coordinator": ???}


def get_contract(contract_name):
    """This functino wll grab the contract addresses from the brownie config
    if defined, otherwise, it will deploy a mock version of that contract, and return
    that mock contract

        Args:
            contract_name (string)

        Returns:
            brownie.netwokr.contract.ProjectContractct: The most recent
            deploy version of the contracts
            MockV3Aggregator[-1]
    """
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <= 0:
            # MockV3Aggregator.length
            deploy_mocks()
        contract = contract_type[-1]
        # MockV3Aggregator[-1]: same thing as grabbing the most recent mock deployment
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        # address
        # ABI
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
        # MockV3Aggregator.abi
    return contract


DECIMALS = 8
INITIAL_VALUE = 20000000


def deploy_mocks(decimals=DECIMALS, initial_value=INITIAL_VALUE):
    account = get_account()
    MockV3Aggregator.deploy(decimals, initial_value, {"from": account})
    print("Deployed")
