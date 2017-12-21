# vdem-codes

## Description
We are often faced with the problem of merging data from sources that use different naming conventions for countries and do not have any other underlying identifier that would facilitate the merge. We have developed a rudimentary tool to deal with this problem that relies on a central master CSV file containing pairs of V-Dem codes and country names. The tool contains code for both R and Stata to take an arbitrary input list of country names and return the corresponding codes.

## Differences Between R and Stata Functions
The R function is more robust, more flexible, and marginally faster than its Stata counterpart. First, the user can specify a different input CSV file if a particular project needs one that differs from the master in any way. Second, the function allows the user to specify the name of the country variable in the data (e.g. "Country" vs. "country" vs. "Country Name" etc.). Third, the function will not complete if any country names in the input are not found in the CSV file. It will instead return those names so that they can be added to the master file. Fourth, any changes saved to the master CSV file are immediately available for use by the function without any additional actions.

The Stata .do file is more rudimentary. First, the variable containing country names in the data must be "country". Second, country names that do not appear in the CSV will appear as missing in Stata. Third, and most importantly, changes made to the CSV are not immediately available in the .do file. The tool contains additional code to update the .do file if the master CSV changes, but it requires the user to take additional action (and the user must have both R and GNU Make installed on their machine).

## Future Extensions/Improvements
The master CSV file needs to live in a shared place where any changes or additions are available to all users. This will avoid conflicts when new codes are added and prevent duplication of efforts when new country spellings are encountered.

One potential improvement would be to automate updates to the .do file when the CSV file is updated (or at least make it easier for users to do so without too many dependencies or technical knowledge).

A second potential improvement is to expand the tool dramatically to deal with problems related to country changes over time. The complexities introduced by this change would not be trivial and much more discussion is necessary.


## To Do
* ~~Organize CSV by code~~
* ~~Check for duplicates~~
* ~~Create a corresponding Stata .do file~~
* Create a script that can be run by (essentially) anybody to update the Stata file on demand whenever the CSV file is updated
    + Currently this is a makefile that relies on R; not sure if there is a more universal solution; maybe? but if this stays on git, then we can probably assume sufficient knowledge to use
* Fix the way that R shows country names not found in the file
* Add script to always keep CSV organized by code (and then by alpha)
* Reverse function to assign names based on codes
