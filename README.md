# LinkPage
I made a syntax to generate HTML for a list of hyperlinks.

This project started out because I had an HTML page where I was storing a bunch of relevant links in one place. Mostly because it was hard to keep track
of all of the Zoom links for my courses, but then I started adding a bunch of other relevant links. Then I bookmarked the local file from my web browser and
it's pretty much a website to consolidate my links, although it's not accessible outside of my computer.

Unfortuantely, it became cumbersome to directly edit the HTML page when I wanted to add or update links. So I decided it would be fun and a good exercise
to create a syntax that would be easy to edit and a script that would generate the HTML for me. The syntax is as follows:

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

The source file has a `.source` extension and will compile into a file of the same name with a `.html` extension. You can optionally have a `.css` file,
as long as it has the same name as the source file.

Compile to html with `python3 compile.py SourceFileName.source` and it will output `SourceFileName.html`
