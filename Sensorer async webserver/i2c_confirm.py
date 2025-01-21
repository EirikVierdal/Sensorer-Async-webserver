from machine import I2C, Pin

# Skann I2C(0) (AHT20)
i2c_aht = I2C(0, scl=Pin(17), sda=Pin(16))
devices_aht = i2c_aht.scan()
print("I2C(0) devices found:", [hex(device) for device in devices_aht])

# Skann I2C(1) (BME280)
i2c_bme = I2C(1, scl=Pin(15), sda=Pin(14))
devices_bme = i2c_bme.scan()
print("I2C(1) devices found:", [hex(device) for device in devices_bme])
