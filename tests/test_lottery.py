# .019
# 190000000000000000
# Lottery import so that we can use the contract data
# Accounts import so that we can use the accounts in the brownie mainnet
# Importing the config so that we can use anything
from brownie import Lottery, accounts, config, network
from web3 import Web3


def test_get_entrance_fee():
    # Use brownie accounts
    account = accounts[0]
    #
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )

    assert lottery.getEntrenceFee() > Web3.toWei(0.018, "ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.022, "ether")
