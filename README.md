# text2html

Automatically translate plain text to html blog with Python.

## Introduction

`html` is a powerful language for writing and publishing blogs. However, not everyone knows its gramma clearly. For example, little Wendy want to publish blogs on my website, but she knows little about `html`. This is exactly where this idea comes from. With this program, everyone is able to write html blogs with markdown rules.

## Features

- Automatically extract title, author, date and place information.
- Automatically translate section names to html headers (# -> <h></h> pairs).
- Automatically translate paragraphs to html paragraphs ( -> <p></p> pairs).
- Automatically translate images to html images ($ -> <img>).
- Automatically translate empty lines to html line breaks ('\n' -> <br>)
- Automatically embed blog body in a complete html file.

## How to Use

Write blogs in plain text with markdown rules (see the following example).

```
This is the Title // title

Apr 1st, 2018 // date

Peking University // place

Wendy // name

# Section 1 // section name

Some text. // paragraph

## Subsection 1 // subsection name

Some more text. // paragraph

## Subsection 2 // subsection name

Some more text. // paragraph

# Section 2 // section name

$ image.jpg // insert an image

// should have an empty line in the end of the blog
```
Save this file with arbitary name (for example `some-name.txt`), then use the following command to translate this plain text file to html blog file:
``` python
text2html("some-name.txt", "Wendy's Blogs")

```
where the second variable indicates the blogs folder name.

After then, if everything goes smoothly, you should get an `html` file named `some-name.html`.