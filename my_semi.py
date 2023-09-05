#

# Define a function to generate a random temperature reading

# Define a function to test the temperature sensor
def test_temperature_sensor():
    temperature = {}
    min , max = -50,150
    if temperature < -20 or temperature > 120:
        print(f"Error: Out of range temperature reading detected: {temperature}")
    elif temperature < 0:
        print(f"Warning: Below freezing temperature reading detected: {temperature}")
    elif temperature > 100:
        print(f"Warning: High temperature reading detected: {temperature}")
    else:
        print(f"Temperature reading within acceptable range: {temperature}")

# Run the temperature sensor test
test_temperature_sensor()


