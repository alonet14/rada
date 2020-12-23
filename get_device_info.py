from nidaqmx.system import System


def get_adc_device_name():
    system = System()
    return system.devices.device_names[0]


name_adc_device = get_adc_device_name()
print(name_adc_device)