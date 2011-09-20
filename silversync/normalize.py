from silversync.client import Sync
from credentials import username, password, passphrase
import pprint

def main():
    s = Sync(username, password, passphrase)
    meta = s.get_meta()
    assert meta['storageVersion'] == 5

    passwords = s.passwords()
    # pprint.pprint(passwords)
    normalized = {}
    for entry in passwords:
        user = entry['username']
        if user not in normalized:
            normalized[user] = set()
        normalized[user].add(entry['password'])
    pprint.pprint(normalized)   

