# Composite Actions on Github

## Introduction

Most of the time when using workflows some steps are duplicated on other
worflows.

When the time come to update those steps, we need to take care about all
different aerea where steps has been duplicated.

It would be more convinient to have a common place where a single update can
rule them all.

## How can we organize this central place ?

Inside a github organisation, when you have multiple repositories and you want
to share actions between all those repositories.

- Create a central repository
- Clone the repository
- Create the expected layout
`mkdir -p .github/workflows/actions`

- Move in this directory
`cd .github/workflows/actions`

For Each composite actions you want to create : 

- Create a directory (this will be the name of the action)
`mkdir mycoolaction`

- Create an action.yml file inside this directory.
