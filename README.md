# vdem-codes

This repo contains the master file information for V-Dem country codes. The country-code pairs are stored in the corresponding CSV file. An R function is also provided to assign these codes.

## To Do
* ~~Organize CSV by code~~
* ~~Check for duplicates~~
* ~~Create a corresponding Stata .do file~~
* Create a script that can be run by (essentially) anybody to update the Stata file on demand whenever the CSV file is updated
    + Currently this is a makefile that relies on R; not sure if there is a more universal solution; maybe? but if this stays on git, then we can probably assume sufficient knowledge to use
