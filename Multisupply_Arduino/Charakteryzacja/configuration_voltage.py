from lib.supply_board import MCP4022        as Stimulus
from lib.supply_board import INA219_Voltage as MeterUnderTest
from lib.rigol        import RigolVoltage   as MeterReference

stimulus_range = range(0,64,1)

'#brng=0 pg=0 badc=0xf sadc=0xf'
#brng=1 pg=0 badc=0xf sadc=0xf