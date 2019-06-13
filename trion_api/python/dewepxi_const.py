# Copyright DEWETRON GmbH 2013
#
# File containing all externally used constants
#


#--------------------------------
# Command ID for i32
#--------------------------------

# Update Parameter Value
PARAM_BUFFER_START_POS            = 0x0510  # Get
PARAM_BUFFER_END_POS              = 0x0511  # Get
PARAM_BUFFER_CLEAR_ERROR          = 0x0512  # Set

PARAM_BUFFER_TOTAL_MEM_SIZE       = 0x0513  # Get
PARAM_BUFFER_ONE_BLOCK_SIZE       = 0x0514  # Get
PARAM_BUFFER_ONE_SCAN_SIZE        = 0x0515  # Get

PARAM_ASYNC_POLLING_TIME          = 0x0553  # Set dword ms
PARAM_ASYNC_FRAME_SIZE            = 0x0554  # Set

PARAM_TIME_OUT                    = 0x0a01  # Set dword
PARAM_LAST_ERROR                  = 0x0a02  # Get

#---------------------------
# param update
#---------------------------
CMD_OPEN_BOARD                    = 0x0001  # Set
CMD_CLOSE_BOARD                   = 0x0002  # Set
CMD_RESET_BOARD                   = 0x0003  # Set
CMD_START_ACQUISITION             = 0x0004  # Get / Set
CMD_STOP_ACQUISITION              = 0x0005  # Set
CMD_CURRENT_POSITION              = 0x000A  # Get

CMD_UPDATE_PARAM_ALL              = 0x0010  # Set
CMD_UPDATE_PARAM_ACQ_ALL          = 0x0011  # Set
CMD_UPDATE_PARAM_CHN_ALL          = 0x0012  # Set
CMD_UPDATE_PARAM_ACQ              = 0x0013  # Set
CMD_UPDATE_PARAM_MUX              = 0x0014  # Set
CMD_UPDATE_PARAM_INTSIG0          = 0x0015  # Set
CMD_UPDATE_PARAM_INTSIG1          = 0x0016  # Set
CMD_UPDATE_PARAM_AI               = 0x0017  # Set
CMD_UPDATE_PARAM_CNT              = 0x0018  # Set
CMD_UPDATE_PARAM_DI               = 0x0019  # Set
CMD_UPDATE_PARAM_BOARD_CNT        = 0x001A  # Set
CMD_UPDATE_PARAM_CAN              = 0x001B  # Set
CMD_UPDATE_PARAM_ACQ_TIMING       = 0x001E  # Set
CMD_UPDATE_PARAM_UART             = 0x0052  # Set
CMD_TIMING_STATE                  = 0x001F  # Set
CMD_SETSENSORBALLANCE             = 0x0020  # Set
CMD_UPDATE_PARAM_AREF             = 0x0021  # Set
CMD_TIMING_TIME                   = 0x0022  # Get


CMD_ASYNC_POLLING_TIME            = 0x001C  # Set
CMD_ASYNC_FRAME_SIZE              = 0x001D  # Set

CMD_GET_UART_STATUS               = 0x0030  # Get
CMD_ACQ_STATE                     = CMD_START_ACQUISITION	# Get

CMD_PXI_LINE_STATE                = 0x0040    #  Get

# Command ID for i32's read function
CMD_BUFFER_START_POINTER		= 0x0020		# Get
CMD_BUFFER_END_POINTER			= 0x0021		# Get
CMD_BUFFER_CLEAR_ERROR			= 0x0022		# Set

CMD_BUFFER_AVAIL_NO_SAMPLE		= 0x0025		# Get
CMD_BUFFER_ACT_SAMPLE_POS		= 0x0026		# Get
CMD_BUFFER_FREE_NO_SAMPLE		= 0x0027		# Set
# for buffer handling and Wrap Around
CMD_BUFFER_TOTAL_MEM_SIZE		= 0x0028		# Get
CMD_BUFFER_ONE_BLOCK_SIZE		= 0x0029		# Get
CMD_BUFFER_ONE_SCAN_SIZE		= 0x002A		# Get

CMD_BUFFER_BLOCK_SIZE              = 0x0102      # Set
CMD_BUFFER_BLOCK_COUNT             = 0x0107      # max 64
CMD_GETDATA_TIME_OUT		   = 0x0a01      # Get

CMD_UPDATE_PARAM_ACQ_ROUTE         = 0x0103  # Set

#for setting/Getting the internal calibration source
#depreciated - use string access functions instead
CMD_INT_REF_VAL				 = 0x0201		#	Set / Get
CMD_REF_MODE				 = 0x0202		#	Set / Get
CMD_UPDATE_PARAM_INTCAL			 = 0x0205		#	Set

#
CMD_BOARD_ACT_SAMPLE_POS		 = 0x0301		# R		Read Register ADC_SCNT
CMD_BOARD_ADC_DELAY			 = 0x0302		# R		Obtain ADC-Delay (valid only AFTER setting a samplerate)
CMD_BOARD_AFSPAN			 = 0x0303		# R		Query %of Samplerate that is alias free
CMD_CHANNEL_AMPBALLANCE			 = 0x0304		# W		Perform Balancing

#for E2PROM - Access
CMD_BOARD_BASEEEPROM_WRITE		 = 0x0401		# W		Write the BaseEEprom-File to EEProm
CMD_BOARD_CONEEPROM_WRITE		 = 0x0402		# W		Write the ConectorEEprom-File to EEProm



PARAM_NOT_USED  			 = 0x7FFFFC00
PARAM_NOT_KNOWN				 = 0x7FFFF800
PARAM_AUTO				 = 0x7FFFF400
PARAM_OFF				 = 0x7FFFF200

UPDATE_ALL_CHANNELS	                 = 100000
UPDATE_GROUP_CHANNELS       	         = 100001
UPDATE_ALL_BOARDS	        	 = 100010


#Returncodes for CMD_ACQ_STATE
ACQ_STATE_ERROR                          = 0xFFFF
ACQ_STATE_IDLE                           = 0x0000
ACQ_STATE_SYNCED                         = 0x0001
ACQ_STATE_RUNNING                        = 0x0003

#Returncodes for CMD_TIMING_STATE
TIMINGSTATE_LOCKED			 = 0x0001	#Locked
TIMINGSTATE_NOTRESYNCED			 = 0x0002	#NotReSynced
TIMINGSTATE_UNLOCKED			 = 0x0003	#Unlocked
TIMINGSTATE_LOCKEDOOR                    = 0x0004	#OOR
TIMINGSTATE_TIMEERROR			 = 0x0005	#TimeError
TIMINGSTATE_RELOCKOOR			 = 0x0006	#RelockOOR
TIMINGSTATE_NOTIMINGMODE		 = 0xFFFF	#NoTimingMode

#FilterBits for CMD_PXI_LINE_STATE
PXI_LINE_STATE_TRIG0                     = (0x00000001 << 0)
PXI_LINE_STATE_TRIG1                     = (0x00000001 << 1)
PXI_LINE_STATE_TRIG2                     = (0x00000001 << 2)
PXI_LINE_STATE_TRIG3                     = (0x00000001 << 3)
PXI_LINE_STATE_TRIG4                     = (0x00000001 << 4)
PXI_LINE_STATE_TRIG5                     = (0x00000001 << 5)
PXI_LINE_STATE_TRIG6                     = (0x00000001 << 6)
PXI_LINE_STATE_TRIG7                     = (0x00000001 << 7)
PXI_LINE_STATE_LBR0                      = (0x00000010 << 0)
PXI_LINE_STATE_LBR1                      = (0x00000010 << 1)
PXI_LINE_STATE_LBR2                      = (0x00000010 << 2)
PXI_LINE_STATE_LBR3                      = (0x00000010 << 3)
PXI_LINE_STATE_LBR4                      = (0x00000010 << 4)
PXI_LINE_STATE_LBR5                      = (0x00000010 << 5)
PXI_LINE_STATE_LBR6                      = (0x00000010 << 6)
PXI_LINE_STATE_STAR                      = (0x00000080)
PXI_LINE_STATE_LBL0                      = (0x00000100 << 0)
PXI_LINE_STATE_LBL1                      = (0x00000100 << 1)
PXI_LINE_STATE_LBL2                      = (0x00000100 << 2)
PXI_LINE_STATE_LBL3                      = (0x00000100 << 3)
PXI_LINE_STATE_LBL4                      = (0x00000100 << 4)
PXI_LINE_STATE_LBL5                      = (0x00000100 << 5)
PXI_LINE_STATE_LBL6                      = (0x00000100 << 6)
PXI_LINE_STATE_LBL7                      = (0x00000100 << 7)
PXI_LINE_STATE_LBL8                      = (0x00000100 << 8)
PXI_LINE_STATE_LBL9                      = (0x00000100 << 9)
PXI_LINE_STATE_LBL10                     = (0x00000100 << 10)
PXI_LINE_STATE_LBL11                     = (0x00000100 << 11)
PXI_LINE_STATE_LBL12                     = (0x00000100 << 12)
