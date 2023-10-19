# SCADA_software_assignment
SCADA Software Engineer assignment designing a utility-scale system.

Parameters: 
- A utility interconnection nameplate of 300MW.
- 200 MW of Battery Energy Storage (BES)
- 300 MW of Photovoltaic solar
- Both BES and Solar are connected to the same utility interconnection

Design a Power plant controller that commands the combined output of the BES + PV system to remain within the “Utility Export
Limit” and the utility’s interconnection nameplate. Program should be able to read
to/from the table below in a CSV format and write the calculated solar and battery setpoints into
the CSV file.

Define a JSON schema with BES and solar information fields like rating, model number, and
communication settings.

Filter out Network IP address listing based on a wanted subnet.
