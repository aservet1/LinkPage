# LinkSyntax
I made a syntax to generate HTML for a list of hyperlinks.

This project started out because I had an HTML page where I was storing a bunch of relevant links in one place. It was mostly to keep track
of all of the Zoom links for my online courses at the start of the pandemic, but then I started adding a bunch of other relevant links.
I bookmarked the local file from my web browser and it became a really convenient way to find stuff without clicking through several web pages,
especially with my then-incredibly-slow $150 laptop that I couldn't even run Gmail on; I needed to open it with the legacy HTML version.

It became cumbersome to directly edit the HTML page when I wanted to add or update links. So I decided it would be fun and a good exercise
to create a syntax that would be easy to edit and a script that would generate the HTML for me. This made it a lot easier to look through
and edit instead of parsing the unnecessary words and symbols of HTML code.

The syntax is as follows:

```
Page Title <$>

Section 1 Title
  item1 :: url for item 1
  item2 :: url for item 2
<$>

Section 2 Title
  item1 :: url for item 1
  item2 :: url for item 2
<$>
```

The `<$>` indicates the end of each section.
Whitespace at the beginning and end of each line is ignored, so use whatever whitespace you'd like to format. Just make sure each entry is on a separate line.

The source file has a `.source` extension and will compile into a `.html` file of the same name. You can optionally have a `.css` file of the same name. I used
to set the background color and link colors. You can use it for whatever you want though, just like any CSS file that you would include in an HTML file.

My example file is called `CourseLinks.source` but you can name it anything you want, as long as it has a `.source` extension.

Compile to html with `python3 compile.py SourceFileName.source` and it will output `SourceFileName.html`.

I also have a handy script, `./edit.sh` which opens up the source file in a text editor and compiles it once you close it. If you know how to, you
can even set up a desktop icon to run the script, so editing your list is as simple as clicking on the button.

Bookmark the local file location in your browser and you can click right to it whenever you want.

## Dependencies
Python 3.6+
