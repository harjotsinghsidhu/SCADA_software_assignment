import csv
import json

# load data from csv
# csv filename = input 
data = []
with open('input.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)
        
# Define function to calculate setpoints
def calculate_setpoints(row):
    available_pv_power = float(row['Available PV Power'])
    available_bes_power = float(row['Available BES Power'])
    site_load = float(row['Site Load'])
    utility_export_limit = float(row['Utility Export Limit'])
    utility_interconnection_nameplate = 300
    
    # Calculate solar and battery setpoints
    calculated_solar_setpoint = min(available_pv_power, utility_export_limit, - available_bes_power, utility_interconnection_nameplate - available_bes_power, site_load)
    calculated_battery_setpoint = min(available_bes_power, utility_export_limit - calculated_solar_setpoint, utility_interconnection_nameplate - calculated_solar_setpoint)
    
    return calculated_solar_setpoint, calculated_battery_setpoint
    
    
# Calculate setpoints for each row and update the data
for row in data:
    calculated_solar_setpoint, calculated_battery_setpoint = calculate_setpoints(row)
    row['Calculated Solar Setpoint'] = calculated_solar_setpoint
    row['Calculated Battery Setpoint'] = calculated_battery_setpoint
    
    
# Write the updated data back to the csv file
with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerheader()
    writer.writerows(data)
    
    
# Define a JSON schema for BES and Solar information
json_schema = {
    "BES": {
        "rating": "200 MW",
        "model_number": "ABC123",
        "communication_settings": {
            "protocol": "Modbus",
            "port": 502
        }
    },
    "Solar": {
        "rating": "300 MW",
        "model_number": "DEF456",
        "communication_settings": {
            "protocol": "TCP/IP",
            "port": 8080
        }
    }
}


# Save the JSON schema to file
with open('schema.json', 'w') as json_file:
    json.dump(json_schema, json_file, indent=4)
    



