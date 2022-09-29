# OCR_insect_labels_to_csv: script to convert OCR collection data from entomological specimens into tsv with Darwin Core terms

This project aims to help speed up digitizing collection data for entomological specimens. It could be used either by researchers working on taxonomic projects or institutions using automated OCR technology to convert the raw OCR data.

The primary challenge is that insect labels are notoriously heterogenous. Currently, the script uses regex patterns to extract the relevant information. Only countries and states in North America are supported but other areas can easily be added. Most date, elevation, and coordinate formats are supported but not all. The most challenging categories to extract are the locality and collector names. All of the information that has not been extracted is put into "Rest" column and can be dealt with manually. 


License
-------

CC0 1.0 Universal.

Contributions
--------------

This script is open source and I welcome any contributions!.

Issues
------

* Countries and their repective states supported: U.S., Canada, Mexico
* The locality is currently extracted based on its normal position after the Country, State, Coordinates ect. but before Collector Names and other collecting information.

