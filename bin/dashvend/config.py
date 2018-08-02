# set this to the full path to the dashvend respository checkout
DASHVEND_DIR = '/home/stampcoin/dashvend'
# note: also update paths in:
#   bin/.init.d.dashvend
#   bin/_dashvend_control.sh
#   bin/dashvend_screens.screenrc
#   bin/show_screen_number.sh

# after testing, set this to True to use mainnet
MAINNET = True

# **public** mainnet bip32 seed for vending address generation
BIP32_MAINNET_SEED = 'ToEA6jDNwU51aWKVEp7t42nG8FhmUjHdDfayFp5eR88jnLJMEe2GjVMBc6TxbewEALgUMT1FDj7AQYpxqQq5WoQnhwsZehj23cdy9pBXY5SxR5m'  # noqa
# on a secure machine, generate above with pycoin 'ku' command.
# for testing, ku is already installed on this machine during the 'make'
# install pycoin by doing:
# git clone https://github.com/richardkiss/pycoin.git
# cd pycoin ; sudo python setup.py install
# ku -n DASH -s 0p/0 P:<a unique, unpublished 100 character long sentence>
# and use the **public version** output
# for sane passphrase selection see: https://masternode.me/smart_passwords.html

# **public** testnet bip32 seed for vending address generation
BIP32_TESTNET_SEED = 'DRKPuUbMa5buKiQRRCQggBzHV2DHbDLjhFFRdHCRHjvx4jq1BCC1NZ1gDoi3ybD5NPHQfHWuxLXrRNQfyUU74YVhAx9kTmt3X87mjGaHiwGGqoad'  # noqa
# ku -n tDASH -s 0p/0 P:<a unique, unpublished 100 character long sentence>

# require seven (out of ten) masternode locks to accept purchase
IX_LOCK_TRESHOLD = 7
# note: sometimes all ten locks do not fully propagate across the network,
# settings above 9 are not recommended.

# dash value required to trigger sale
VENDING_COST = 0.1
