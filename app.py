from flask import Flask, request, redirect
import time

from dao.shorter_dao import ShorterDAO

app = Flask('Shorter')

# Store the mapping from short URLs to original URLs
shorter_dao = ShorterDAO()
url_mapping = {}


@app.route('/shorten', methods=['POST'])
def shorten_url():
    # Get the original URL and the desired expiration time
    original_url = request.form.get('url')
    expiration_time = int(request.form.get('expiration_time'))

    # Generate a unique short URL
    current_timestamp = int(time.time())
    short_url = hex(current_timestamp)[2:]

    # Store the mapping in the url_mapping dictionary
    url_mapping[short_url] = (original_url, current_timestamp + expiration_time)

    return short_url


@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
    # Check if the short URL is in the mapping
    if short_url not in url_mapping:
        return "URL not found", 404

    # Check if the URL has expired
    original_url, expiration_timestamp = url_mapping[short_url]
    current_timestamp = int(time.time())
    if current_timestamp > expiration_timestamp:
        del url_mapping[short_url]
        return "URL has expired", 404

    # Redirect the user to the original URL
    return redirect(original_url)


if __name__ == '__main__':
    app.run()
