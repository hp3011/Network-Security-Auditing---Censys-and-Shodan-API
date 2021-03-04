1) Run censys_query_api.py file for 152.1.0.0/16 and 152.7.0.0/16
   Remember the to change CIDR block ip address in data variable on line 16 and line 64 for different CIDR block.
   Store the variable data to plot the bar graph

2) Run plot_print.py file to plot the data collected from censys_query_api.py.
   All the data is already initialise in plot_print.py

3) Run shodan_api.py: 
   Based on the targeted hosts, add the host to hosts lists to get more information on CVE using Shodan API.