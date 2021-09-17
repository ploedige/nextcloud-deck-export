# nextcloud-deck-export

This code is a fork of the [keitalbame/nextcloud-deck-export-import](https://github.com/keitalbame/nextcloud-deck-export-import)

The functionality was reduced to only output the deck content to a json file.

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
   * urlFrom
   * authFrom
   * outFile
4. Run python script
   ```
   python nextcloud-deck-export-import.py
   ```
