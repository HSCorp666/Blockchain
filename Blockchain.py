from Block import Block
import datetime
import random

blockChain = [Block.genesis_block()]
print("Genesis block created.")
print(f"Genesis block hash: {blockChain[-1].hash}")
print(f"Genesis block created at: {blockChain[-1].timestamp}")

try:
	block_amount = int(input("Enter block amount:-> "))
except ValueError:
	print("\nBlock amount must be integer.")


for block in range(1, block_amount + 1):
	_block = Block(blockChain[-1].hash, "NULL", datetime.datetime.now())
	blockChain.append(_block)

	print(f"\nBlock {block} has been created.")
	print(f"Block {block} hash: {blockChain[-1].hash}")
	print(f"Block {block} previous hash: {blockChain[-1].prev_hash}")
	print(f"Block {block} created at: {blockChain[-1].timestamp}")
