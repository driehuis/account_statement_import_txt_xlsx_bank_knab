# Bank statement import definitions for KNAB bank

This Statement Sheet definition is intended to be used with the OCA account_statement_import_txt_xlsx module.

Use "Zoeken en downloaden", select your desired period and "Bij- en afschrijvingen". Click "Zoeken". Then select Excel format to download.
The downloaded file contains an extraneaous record "KNAB EXPORT" when downloading in CSV format, so this record must be removed priot to import if you prefer to use CSV format. 

Last I checked, KNAB did not include previous and current balance in the download. Therefore, it is essential that you verify the download with your statement after importing. Unfortunately, the only format that does include the balance is the MT940 format, for which no importer is available in OCA for Odoo 14.

# Production notes

The Statement Sheet Definition has been created and tested in the Odoo 14 user interface to the account_statement_import_txt_xlsx module. It was then exported to an XML file using the xr-export-statement-sheet-mapping.py script.
