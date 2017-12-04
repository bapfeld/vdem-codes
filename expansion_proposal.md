---
title: Massive Expansion Proposal
---
# Notes from Skype Call
## Things to take into consideration
* Different levels
* Potentially have some names that refer to different things
* Data may appear more granular than yearly
* We have polygons for the world starting in 1789 and for Europe starting at 0

## Metadata
* Want to track where we got the information
* Want to track where the original sources got the information

# My Idea
We conceptualize the division of the world as branching nodes over time. These nodes can split, rejoin, merge, and continue into the present. Each node represents a political entity that exists or existed at some point in time.

## Data Organization
There should be a master level file that lists every single node with a common name, a unique code, and references to its data files.

There are two type of data files we need: name synonym files and node relationship files.

Name synonym files are lists of synonymous names for a given entity. It is possible that multiple entities could share a synonym file.

Node relationship files are unique files that contain a time series of data points for a given node. Each includes a list of all superior and inferior nodes associated with that node at any given time as well as its political designation (i.e. country vs subnational unit vs municipality vs...)--- e.g. you could know all of the states and territories that were in the US in 1837; conversely, you could use it to track control of Texas over time.

## Using the database
Given a political unit entry, search all synonym files for a match; if only one, return a master level code; if none, return an error; if multiple, require additional input (year) [how does this help?]

Automatically generating a history of each political entity.

## Code Considerations
I think the first step of processing names it to canonicalize them in some way --- all lowercase, remove accents, etc. [Is that going to be a concern at subnational levels?]

# Problems to deal with
* Do synonym files have to be unique or can entities share them?
* If this were extended to the city level, there's going to be a LOT of duplication of names, etc. How do we deal with parsing names but also returning correct codes?
* Does this even accomplish what we want?
* Is there duplication of information here? Is it too complex to easily keep updated?
* What I'm describing here is really suited for SQL, I think...time to learn SQL and db connections in R/Python?
* I don't think unique master level codes need to be additive (e.g. state is country + provincial codes), but they do need to be systematic and probably need to give some indicatino of the administrative level in question. (e.g. all state/province level units are "2-xxxx")
* Is this really an expandable system, or do we need to start with all the nodes pre-defined? [I think it is expandable, but see issue about with complexity of updating]

# Alternative Idea
After talking with John some more, it sounds like the above may be too complex for a variety of reasons.

Instead, what we really need is two things: software to translate different coding/naming schemes and a master data repository. The software wouldn't just parse names and return our codes, it could also return a subset of our codes based on a desired coding scheme (e.g. user says they want countries from COW definitions, so we give our corresponding codes for that subset).

So is this really a project about understanding the overlap of different country definitions?
