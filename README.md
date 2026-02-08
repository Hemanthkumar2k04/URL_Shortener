# URL Shortener
A simple URL shortening service that converts long URLs into short, shareable links.

### What It Does
Takes a long URL like:

> https://www.youtube.com/watch?v=9342uju934&ab_channel=Something

And gives you:
> http://192.168.0.250:3000/n

When someone clicks the short link, they're automatically redirected to the original URL.

### Why?
Long URLs are:
- Hard to share
- Look messy
- Difficult to remember

Short URLs solve this.

### How It Works
Creating a Short URL

- Store the original URL in PostgreSQL database
- Generate a unique short code using Base62 encoding (converts number IDs into short strings like n, xP)
- Return the short URL to the user

Using a Short URL

1. Check Redis cache first (fast memory) for the short code

2. If not in cache, look up in PostgreSQL database

3. Save to Redis for next time

4. Redirect user to the original URL

### Tech Stack
<b>PostgreSQL</b> - Permanent storage for URLs

<b>Redis</b> - Fast caching layer for frequently accessed links

<b>Base62 Encoding</b> - Converts numeric IDs to short alphanumeric codes

### Key Features
⚡ Fast redirects using Redis caching

🔗 Short, clean URLs

📊 Scalable architecture (cache → database pattern)

🎯 Simple and reliable


<b>Simple. Fast. Efficient.</b>
