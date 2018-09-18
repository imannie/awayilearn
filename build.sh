#!/bin/bash

cat templates/top.html content/mid_home.html templates/bottom.html > docs/home.html
cat templates/top.html content/mid_blog.html templates/bottom.html > docs/blog.html
cat templates/top.html content/mid_about.html templates/bottom.html > docs/about.html
cat templates/top.html content/mid_contact.html templates/bottom.html > docs/contact.html
cat templates/top.html content/mid_work.html templates/bottom.html > docs/work.html


