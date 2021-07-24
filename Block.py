import datetime
import hashlib


class Block:
	def __init__(self, prev_hash: str, data: str, timestamp):
		self.prev_hash = prev_hash
		self.data = data
		self.timestamp = timestamp
		self.hash = self.get_hash()

	@staticmethod
	def genesis_block():
		return Block("0", "0", datetime.datetime.now())

	def get_hash(self):
		header_bin = str(self.prev_hash) + str(self.data) + str(self.timestamp)
		inner_hash = hashlib.sha256(bytes(header_bin.encode())).hexdigest()
		outer_hash = hashlib.sha256(bytes(inner_hash.encode())).hexdigest()
		return outer_hash
