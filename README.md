# cookify

## This little hobby project allows users to turn the article about a dish they've pinned on pintrest into an easy to read recipe with step by step instructions

### Minimum Requirements
* On successful login to pintrest from cookify, create user (if no user exists) and generate associated token auth
* Parse pins, saving recipe and instructions
    ** Initially just launch a subprocess
    ** Long term save list of urls, then parse on task scheduler
* User can search for recipes and select on to be cooked
* Once saved, it will be put into a "meal plan" and the ingredients added to a "shopping list"
* User should be able to add, remove or edit items from the shopping list

