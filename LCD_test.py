import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()
# TODO: temperature sensor file
temp_sensor_file = open("/sys/bus/w1/devices/28-030297795d50/w1_slave", "rt")

while True:
	# mylcd.lcd_display_string(“TEXT TO PRINT”, ROW, COLUMN)

	temperature = int(temp_sensor_file.read().split("t=")[-1]) / 1000
	temp_sensor_file.seek(0)

	mylcd.lcd_clear()
	mylcd.lcd_display_string('Temperature:', 2, 3)
	mylcd.lcd_display_string('{} deg C'.format(temperature), 3, 3)
	sleep(1)