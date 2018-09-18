
#This is a Python Statics Site Generator

top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()

#Making home html sandwich file
content = open('content/mid_home.html').read()
home_html = top_template + content + bottom_template
open('home.html', 'w+').write(home_html)

#Making blog html sandwich file
content = open('content/mid_blog.html').read()
blog_html = top_template + content + bottom_template
open('blog.html', 'w+').write(blog_html)

#Making work html sandwich file
content = open('content/mid_work.html').read()
work_html = top_template + content + bottom_template
open('work.html', 'w+').write(work_html)

#Making about html sandwich file
content = open('content/mid_about.html').read()
about_html = top_template + content + bottom_template
open('about.html', 'w+').write(about_html)

#Making contact html sandwich file
content = open('content/mid_contact.html').read()
contact_html = top_template + content + bottom_template
open('contact.html', 'w+').write(contact_html)






