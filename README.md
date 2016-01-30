# sublimeAutoCopyRight
Automatically adds configurable copyright info from project settings on save in sublime

## Summary
This plugin allows copy right comments to be inserted into the top of each file as it is saved if it already does not exist. The configurations come from configured project settings in the <?>.sublime-project json file within the "settings" object

## Creating Sublime Project File
The simplest way to create the needed files for your project is to go to Project > Save Project As
This will generate a <your project name>.sublime-project file that is a json file

All you need to do is:

1. Ensure that there is a "settings" object within the <your project name>.sublime-project json file
2. Add a "copyRightInfo" object to the "settings" object
3. Specify the "name", "site", and "licenseText" properties and values to that json file

Here is an example of a <your project>.sublime-project file:

```json
{
    "folders":
    [
        {
            "path": "/Users/jmartin/Desktop/grasptheory/source/grasptheorywebapp"
        }
    ],
    "settings": {
        "copyRightInfo": {
            "name": "John Martin",
            "site": "http://grasptheory.com",
            "licenseText": "Proprietary. You may NOT copy, use, modify, or distribute any piece of this software in any way"
        }
    }
}
'''

## Requirements

