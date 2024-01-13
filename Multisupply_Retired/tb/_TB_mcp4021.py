import sys
sys.path.append('../lib')
from mcp4021 import MCP4021

pot = MCP4021(18)

pot.set(63)
