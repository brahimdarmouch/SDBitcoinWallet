import os, binascii, hashlib, base58, ecdsa
import bech32

def ripemd160(x):
	d = hashlib.new('ripemd160')
	d.update(x)
	return d

def hexPrvToWif(hexPrv, compressed):
	suffix = ""
	if compressed:
		suffix = "01"
	fullkey = '80' + hexPrv + suffix
	sha256a = hashlib.sha256(binascii.unhexlify(fullkey)).hexdigest()
	sha256b = hashlib.sha256(binascii.unhexlify(sha256a)).hexdigest()
	return base58.b58encode(binascii.unhexlify(fullkey+sha256b[:8])).decode()

def wifToPrvHex(wif) :
	byte_str = binascii.hexlify(base58.b58decode(wif))
	byte_str_drop_last_4bytes = byte_str[0:-8]
	byte_str_drop_first_byte = byte_str_drop_last_4bytes[2:].decode()
	return byte_str_drop_first_byte if len(byte_str_drop_first_byte) == 64 else byte_str_drop_first_byte[:-2]

def prvToPub(hexPrv, compressed):
	sk = ecdsa.SigningKey.from_string(binascii.unhexlify(hexPrv.encode()), curve=ecdsa.SECP256k1)
	vk = sk.get_verifying_key()
	if compressed:
		from ecdsa.util import number_to_string
		order = vk.pubkey.order
		x_str = binascii.hexlify(number_to_string(vk.pubkey.point.x(), order))
		sign = '02' if vk.pubkey.point.y() % 2 == 0 else '03'
		return (sign.encode() + x_str).decode()
	return '04' + binascii.hexlify(vk.to_string()).decode()

def p2pkh_address(pub): # starts with 1
	hash160 = ripemd160(hashlib.sha256(binascii.unhexlify(pub)).digest()).digest()
	publ_addr_a = b"\x00" + hash160
	checksum = hashlib.sha256(hashlib.sha256(publ_addr_a).digest()).digest()[:4]
	return base58.b58encode(publ_addr_a + checksum).decode()

def p2sh_address(pub): # starts with 3
	hash160 = ripemd160(hashlib.sha256(binascii.unhexlify(pub)).digest()).digest()
	publ_addr_a = b'\x00\x14' + hash160 # bytes.fromhex("0014")
	script = ripemd160(hashlib.sha256(publ_addr_a).digest()).digest()
	return base58.b58encode_check(b"\x05" + script).decode()

def bech32_address(pub): # starts with bc1
	keyhash = hashlib.new("ripemd160", hashlib.sha256(binascii.unhexlify(pub)).digest()).digest()
	return bech32.encode('bc', 0, keyhash)

hexPrv = binascii.hexlify(os.urandom(32)).decode()
## If you already have the private key as WIF and you want the full info about wallet, you can uncomment this line below
# hexPrv = wifToPrvHex("KycYaZeRPvpYUH2SaAWKYvW8KgMepXY1iTuMJRSyNPQeoBpsBMwy")

Upub = prvToPub(hexPrv, False)
Cpub = prvToPub(hexPrv, True)

print("======================= [ BITCOIN PRIVATE KEYS ] =======================")
print("Hex Private Key         : ", hexPrv)
print("Decimal Private Key     : ", int(hexPrv, 16))
print("Uncompressed Private Key: ", hexPrvToWif(hexPrv, False))
print("Compressed Private Key  : ", hexPrvToWif(hexPrv, True))
print("======================== [ BITCOIN PUBLIC KEYS ] ========================")
print("Uncompressed Public Key : ", Upub)
print("Compressed Public Key   : ", Cpub)
print("=========================== [ BITCOIN ADDRESS ] ===========================")
print("Uncompressed Address    : ", p2pkh_address(Upub))
print("Compressed Address      : ", p2pkh_address(Cpub))
print("P2SH Address            : ", p2sh_address(Cpub))
print("BECH32 Address          : ", bech32_address(Cpub))