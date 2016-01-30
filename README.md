# sublimeAutoCopyRight
Automatically adds configurable copyright info from project settings on save in sublime

## Summary
This plugin allows copy right comments to be inserted into the top of each file as it is saved if it already does not exist. The configurations come from configured project settings in the <?>.sublime-project json file within the "settings" object

## Creating Sublime Project File
The simplest way to create the needed files for your project is to go to Project > Save Project As
This will generate a <your project name>.sublime-project file that is a json file


## Requirements

You will need to perform two steps:

1. Install the plugin
2. Create or verify you have project settings
3. Add the "copyRightInfo" configurations to your project settings
4. Start using the plugin!

### Install the Plugin
In Sublime, click Tools > New Plugin. Copy and paste the code within this repository's sublimeAutoCopyRight.py file. Save it and name it "sublimeAutoCopyRight.py"


### Create or verify you have project settings


### Add the "copyRightInfo" configurations to your project settings

1. Ensure that there is a "settings" object within the <your project name>.sublime-project json file which will be at the root of your project
2. Add a "copyRightInfo" object to the "settings" object
3. Specify the "name", "site", and "licenseText" properties and values to that json file

Here is an example of a <your project>.sublime-project file:

```json
{
    "folders":
    [
        {
            "path": "/Users/John/some/path"
        }
    ],
    "settings": {
        "copyRightInfo": {
            "name": "John Martin",
            "site": "http://johndavidfive.com",
            "licenseText": "alkdfj adlfkja dslkjas dflk jasdflja sdlfjasdfyasofdlj asldfjkasdlkfj alsdfjlasdkjf las"
        }
    }
}
```

### Start using the plugin!

If everything is good... you should be able to open a file within your project and save it and the copyright info should be injected on the first line of your file.
If it does not, then open the sublime console and try again and monitor the messages. The most likely error is that you did not specify all values in the json.
On Mac, hit ctrl + ~ to open the console



