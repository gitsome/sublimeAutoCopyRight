# Sublime Auto Copyright [BETA]
Automatically adds configurable copyright info from project settings on save to the very top of each file in Sublime Text.

## Warning
No legal advice is given here. The use of this plugin does not give any legal guarentees of protection. Use at your own risk. The goal is to provide a starting point for others to customize their legal language for their own projects.

## Summary
This plugin allows copyright comments to be inserted into the top of each file as it is saved if it already does not exist. The configurations come from configured project settings in the <?>.sublime-project json file within the "settings" object

If you have not created a \<your project name\>.sublime-project json file or you have not specified the "copyRightInfo" object then this plugin will not affect your project. This provides a lot of flexibility in modifying your copyright text on a per-project basis.

## Creating Sublime Project File
The simplest way to create the needed files for your project is to go to Project > Save Project As
This will generate a \<your project name\>.sublime-project file that is a json file


## Steps to Intall and Use

You will need to perform just a few simple steps:

### 1. Install the Plugin
In Sublime, click Tools > New Plugin. Copy and paste the code within this repository's sublimeAutoCopyRight.py file. Save it and name it "sublimeAutoCopyRight.py"


### 2. Create/Verify you have the proper project settings


### 3. Add the "copyRightInfo" configurations to your project settings

1. Ensure that there is a "settings" object within the \<your project name\>.sublime-project json file which will be at the root of your project
2. Add a "copyRightInfo" object to the "settings" object
3. Specify the "name", "site", "licenseText", and "allowableExtensions" properties and values to that json file

Here is an example of a \<your project\>.sublime-project file:

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
            "licenseText": "alkdfj adlfkja dslkjas dflk jasdflja sdlfjasdfyasofdlj asldfjkasdlkfj alsdfjlasdkjf las",
            "allowableExtensions": ["js", "css"]
        }
    }
}
```

### 4. Start using the plugin!

If everything is good... you should be able to open a file within your project and save it and the copyright info should be injected on the first line of your file.
If it does not, then open the sublime console and try again and monitor the messages. The most likely error is that you did not specify all values in the json.
On Mac, hit ctrl + ~ to open the console


## Future Enhancements

* Would love some help compiling a new file with just a list of license links and text that people can use in the project settings



