# nextcloud-deck-export-import

This code is a fork of the [keitalbame/nextcloud-deck-export-import](https://github.com/keitalbame/nextcloud-deck-export-import)

The script was split up to enable export to a json file and import of that json file.  

__Why in hell would I ever need this functionality?__  
Valid question. I needed it because I fucked up my Nextcloud installation inside a Proxmox VM.
The web GUI took upwards of 30s to load any page.
After two weeks of trial and error trying to figure out the problem I was still unable to fix this issue.
I decided to completely rebuild my Nextcloud installation.
Since the new install is intented to run on the same domain as the old one I needed a way to store the exported data before reimporting into the new installation.

## Before run the script

If you have 2FA configured, you need to temporarly disable it.
Reenable it after import is finished.

## How to run

1. Clone repository
   ```
   git clone https://github.com/keitalbame/nextcloud-deck-export-import.git
   ```
2. Change to folder
   ```
   cd nextcloud-deck-export-import
   ```
3. Adapt variables for your instances:
   * export script:
      - urlFrom
      - authFrom
      - outFile
   * import script:
      - inFile
      - urlTo
      - authTo
4. Run python script
   - export:
      ```
      python nextcloud-deck-export.py
      ```
   - import:
      ```
      python nextcloud-deck-import.py
      ```
