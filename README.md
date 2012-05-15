# Who is Don?

Don is the friendly Robot at What Cheer.

For [Big Omaha 2012](http://www.bigomaha.com/) we built Small Talk, a chat application that only conference attendees could use.  To add some fun we built Don, a robot you could chat with.

This is the guts of Don, on display for all to see.

# How do I boot him up?

    $ python app.py

or 

    $ foreman start

# How do I put him on Heroku?

    $ heroku apps:create --stack=cedar
    $ heroku ps:scale web=1
    $ heroku addons:add redistogo:nano
    $ git push heroku master

# How do I make him smarter?

Edit (or add) brain files.  These are regular expression sets.

In the future we hope to make this language a bit simpler and easier to understand for non-programmers.

# Why?

Why not?

# Who?

We are [What Cheer](http://whatcheer.com/), we make fancy websites. And robots.

