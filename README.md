# ALTernative Imagery
Adding alt attributes to your img tags because you're too lazy to do so [#CalHacks3.0](https://devpost.com/software/alternativeimagery)

## What?
Basically a script that will take in some HTML, find all the img tags with no alt text, then use [Microsoft Cognitive Services](https://www.microsoft.com/cognitive-services) to fill those in with a description of the image

## Usage

```bash
mv keys.example.py keys.py
```
Replace ocp-apim-subscription-key in keys.py with your api key for [Microsoft Cognitive Services](https://www.microsoft.com/cognitive-services)

```bash
python main.py siteUrl rootUrl outputFileName.html
```
* siteUrl is the webpage HTML you want to grab
* rootUrl is the base url for which image relative paths are used on the website (normally the homepage)
* outFileName.html is the name of the file that the script will output with the filled in alt texts
 ### Example
  ```bash
	python main.py http://debkbanerji.com/ http://debkbanerji.com/ output.html
	```
