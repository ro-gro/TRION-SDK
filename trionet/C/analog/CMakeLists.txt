#
# Project DEWETRON TRION SDK - analog examples
#

add_executable(TN_OneAnalogChannel
  TN_OneAnalogChannel/tn_one_analog_channel.c
  )
  TRIONET_SampleBuildSettings(TN_OneAnalogChannel "analog")

