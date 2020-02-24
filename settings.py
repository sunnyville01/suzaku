# Bittrex
bittrex_ignore = set(['AERGO', 'ANKR', 'BTT', 'BTU', 'CRO', 'CTXC', 'DENT', 'DRGN', 'ELF', 'FSN', 'GRIN', 'HST', 'HXRO', 'IOST', 'IOTX', 'JNT', 'MEDX', 'META', 'NCASH', 'NKN', 'NPXS', 'ONG', 'ONT', 'OST', 'PAL', 'PI', 'PINK', 'PTON', 'QNT', 'SERV', 'SLT', 'TRAC', 'TTC', 'VITE', 'XDN', 'ZIL', 'FAIR', 'LMC', 'BTC', 'USDT', 'DYN'])
bittrex_ignore_custom = set(['NAV', 'EXCL', 'DTB', 'NXC', 'BITS', 'CANN', 'ITM', 'TKS', 'THC', 'LUN', 'NEOS', 'TIX'])
bittrex_ignore = bittrex_ignore.union(bittrex_ignore_custom)
binance_ignore = set(["BCC", "HSR", "SALT", "SUB", "ICN", "MOD", "VEN", "WINGS", "TRIG", "CHAT", "RPX", "CLOAK", "BCN", "TUSD", "PAX", "USDC", "BCHSV", ])

# Bittrex
bittrex_coins = set(['1ST', '2GIVE', 'ABY', 'ADA', 'ADT', 'ADX', 'AEON', 'AERGO', 'AID', 'AMP', 'ANKR', 'ANT', 'APX', 'ARDR', 'ARK', 'AUR', 'BAT', 'BAY', 'BCH', 'BCPT', 'BFT', 'BITB', 'BITCNY', 'BITS', 'BKX', 'BLK', 'BLOCK', 'BLT', 'BNT', 'BOXX', 'BRK', 'BRX', 'BSD', 'BSV', 'BTC', 'BTM', 'BTS', 'BTT', 'BTU', 'BURST', 'BYC', 'CANN', 'CBC', 'CLOAK', 'CMCT', 'COVAL', 'CRB', 'CRO', 'CRW', 'CTXC', 'CURE', 'CVC', 'DASH', 'DCR', 'DCT', 'DENT', 'DGB', 'DGD', 'DMD', 'DMT', 'DNT', 'DOGE', 'DOPE', 'DRGN', 'DTA', 'DTB', 'DYN', 'EBST', 'EDG', 'EDR', 'EFL', 'EGC', 'ELF', 'EMC', 'EMC2', 'ENG', 'ENJ', 'ENRG', 'ETC', 'ETH', 'EXCL', 'EXP', 'FAIR', 'FCT', 'FLDC', 'FLO', 'FSN', 'FTC', 'FUN', 'GAM', 'GAME', 'GBG', 'GBYTE', 'GEO', 'GLC', 'GNO', 'GNT', 'GO', 'GOLOS', 'GRC', 'GRIN', 'GRS', 'GTO', 'GUP', 'HMQ', 'HST', 'HXRO', 'HYDRO', 'IGNIS', 'IHT', 'INCNT', 'IOC', 'ION', 'IOP', 'IOST', 'IOTX', 'JNT', 'KMD', 'KORE', 'LBA', 'LBC', 'LMC', 'LOOM', 'LRC', 'LSK', 'LTC', 'LUN', 'MAID', 'MANA', 'MCO', 'MEDX', 'MEME', 'MER', 'MET', 'META', 'MFT', 'MLN', 'MOBI', 'MOC', 'MONA', 'MORE', 'MTL', 'MUE', 'MUSIC', 'MYST', 'NAV', 'NBT', 'NCASH', 'NEO', 'NEOS', 'NGC', 'NKN', 'NLC2', 'NLG', 'NMR', 'NPXS', 'NXC', 'NXS', 'NXT', 'OCN', 'OK', 'OMG', 'OMNI', 'ONG', 'ONT', 'OST', 'PAL', 'PART', 'PAX', 'PAY', 'PI', 'PINK', 'PIVX', 'PMA', 'POLY', 'POT', 'POWR', 'PPC', 'PRO', 'PTC', 'PTON', 'PTOY', 'QNT', 'QRL', 'QTUM', 'QWARK', 'RADS', 'RCN', 'RDD', 'REP', 'RFR', 'RISE', 'RLC', 'RVN', 'RVR', 'SALT', 'SBD', 'SC', 'SEQ', 'SERV', 'SHIFT', 'SIB', 'SLR', 'SLS', 'SLT', 'SNGLS', 'SNT', 'SOLVE', 'SPC', 'SPHR', 'SPND', 'SRN', 'STEEM', 'STORJ', 'STORM', 'STRAT', 'SWT', 'SYNX', 'SYS', 'THC', 'TIX', 'TKS', 'TRAC', 'TRST', 'TRX', 'TTC', 'TUBE', 'TUSD', 'TX', 'UBQ', 'UKG', 'UP', 'UPP', 'USD', 'USDS', 'USDT', 'VEE', 'VIA', 'VIB', 'VITE', 'VRC', 'VRM', 'VTC', 'WAVES', 'WAX', 'WINGS', 'XCP', 'XDN', 'XEL', 'XEM', 'XHV', 'XLM', 'XMG', 'XMR', 'XMY', 'XNK', 'XRP', 'XST', 'XVG', 'XWC', 'XZC', 'ZCL', 'ZEC', 'ZEN', 'ZIL', 'ZRX'])
bittrex_coins = bittrex_coins - bittrex_ignore

# Binance
binance_coins = set(['APPC','MTH','ENJ','TRX','POE','GRS','BNB','XVG','ARK','HSR','ICX','BTM','USDT','HCC','PIVX','OAX','DNT','MCO','ICN','ZRX','OMG','WTC','LRC','LLT','YOYO','NEO','STRAT','SNGLS','KNC','BQX','SNM','FUN','LINK','ETH','CTR','SALT','MDA','IOTA','SUB','ETC','MTL','LTC','ENG','AST','DASH','BTG','EVX','REQ','VIB','POWR','QTUM','XRP','MOD','EOS','STORJ','VEN','KMD','RCN','NULS','RDN','XMR','DLT','AMB','BAT','ZEC','BCPT','ARN','GVT','CDT','GXS','SNT','QSP','BTS','LSK','BTC','TNT','FUEL','MANA','BCD','DGD','ADX','ADA','PPT','CMT','XLM','CND','LEND','WABI','SBTC','BCX','WAVES','TNB','GTO','BNT','OST','ELF','AION','SYS','REP','BCN','VIA','NAS','NANO','CLOAK','ETF','NPXS','CVC','IOST','WPR','SC','INS','AGI','XEM','CHAT','IOTX','ZIL','LUN','POA','SKY','RPX','TUSD','BRD','BLZ','DATA','AE','LOOM','GNT','KEY','STEEM','QLC','EON','WAN','NXS','RLC','QKC','STORM','GAS','ONT','THETA','VIBE','NCASH','ZEN','NEBL','EDO','WINGS','NAV','TRIG','BCC','XZC', 'GO', 'DOCK', 'MFT', 'BCHABC', 'DENT', 'PHX', 'PAX', 'HC', 'BCHSV', 'USDC', 'POLY', 'VET', 'MITH', 'RVN', 'DCR', 'ARDR', 'HOT'])

settings = {
    "pct_change_threshold": 20,
    "bittrex_coins": bittrex_coins,
    "bittrex_ignore": bittrex_ignore,
    "binance_coins": binance_coins,
    "binance_ignore": binance_ignore,
    "flush_db": False,
    "exchanges": ["bittrex",],
}
