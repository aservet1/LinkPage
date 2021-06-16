# LinkSyntax
I made a syntax to generate HTML for a list of hyperlinks.

This project started out because I had an HTML page where I was storing a bunch of relevant links in one place. It was mostly to keep track
of all of the Zoom links for my online courses at the start of the pandemic.
I bookmarked the local file from my web browser and it became a convenient way to find stuff without clicking through a bunch of web pages,
especially with my then-incredibly-slow laptop that took at least a minute to load Gmail unless I used the old HTML version.

It became cumbersome to directly edit the HTML page when I wanted to add or update links. So I decided it would be fun and a good exercise
to create a syntax that would be easy to edit and a program that would generate the HTML for me. This made it a lot easier to look through
and edit instead of parsing the unnecessary words and symbols of HTML code.

## Example

```
CourseLinks <$>

Personal
    Github			:: https://github.com/aservet1
<$>

jRAPL
    Slack			:: https://app.slack.com/client/T01RWDJKNHY/C01RFLY4WQ7
    Liu Zoom Room		:: https://binghamton.zoom.us/my/yu.david.liu
    Github			:: https://github.com/aservet1/jRAPL
    Overleaf Paper		:: https://www.overleaf.com/project/5e8bed3318eddd0001296834
    GreenSoftwareLab Github	:: https://github.com/greensoftwarelab
<$>

CS447 - High Performance Computing
    Zoom		:: https://binghamton.zoom.us/j/97137731406
    Piazza		:: https://piazza.com/class/kj3g1vwdbav5pl
    Website		:: https://www.cs.binghamton.edu/%7Ekchiu/cs447/
<$>
```

![image](https://user-images.githubusercontent.com/54599694/122161024-f5ad4680-ce3e-11eb-8c4d-944036618587.png)

Whitespace at the beginning and end of each line is ignored, so use whatever whitespace you'd like to format. Just make sure each entry is on a separate line.


## Files Involved

The source file has a `.source` extension and will compile into a `.html` file of the same name. The HTML is machine generated, so it's not formatted nicely for human eyes to see or edit. If you want to change the file, either edit the `.source` or `compile.py` if you want to do some fundamental change to the structure.

You can optionally have a `.css` file of the same name. I used to set the background color and link colors. You can use it for whatever you want though, just like any CSS file that you would include in an HTML file.

My example file is called `CourseLinks.source` but you can name it anything you want, as long as it has the `.source` extension.


## Usage

Edit the entries of the `.source` file according to the syntax above.

Compile to html with `python3 compile.py SourceFileName.source` and it will write to `SourceFileName.html`.

I also have a handy Bash script, `./edit.sh` which opens up the source file in a text editor and compiles it when you're done. It's only a few lines, so you can easily edit it to pick your own file names or text editor. If you know how to, you can set up a Desktop icon to run the script, so editing your list is as simple as clicking on an icon. A few ways to do that are described [here](https://askubuntu.com/questions/299052/how-to-execute-sh-script-from-a-desktop-shortcut).

Bookmark the local file path in your browser and you can click right to it whenever you want.

## Dependencies
Python 3.6+
