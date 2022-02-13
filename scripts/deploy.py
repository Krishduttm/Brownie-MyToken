from brownie import MyToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def deploy_token():
    account = get_account()
    token = MyToken.deploy(initial_supply, {"from": account})
    print(token.name())


def main():
    deploy_token()
