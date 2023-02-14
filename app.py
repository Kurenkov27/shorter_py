import datetime

from flask import Flask, render_template, request, redirect

from dao.shorter_dao import ShorterDAO

app = Flask('Shorter')

# Create Data Access Object to db
shorter_dao = ShorterDAO()
url_mapping = {}
# Update the mapping from db short URLs to original URLs
shorter_dao.update_map(url_mapping)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', short_url=None)
    # Get the original URL and the desired expiration time
    original_url = request.form.get('url')
    expiration_days = int(request.form.get('days'))

    # Generate a unique short URL
    expiration_date_time = datetime.datetime.now() + datetime.timedelta(days=expiration_days)
    current_timestamp = int(expiration_date_time.timestamp())
    short_url = hex(current_timestamp)[2:]

    # Store the mapping in the database
    shorter_dao.add_url_to_db(
        short_url=short_url,
        original_url=original_url,
        expiration_date=expiration_date_time.strftime('%Y-%m-%d %H:%M:%S.%f'),
    )

    # Store the mapping in the url_mapping dictionary
    url_mapping[short_url] = (original_url, expiration_date_time)

    #return f'Your URL: {request.base_url + short_url}'
    return render_template('url_window.html', short_url=request.base_url + short_url)


@app.route('/<short_url>/', methods=['GET'])
def redirect_url(short_url):
    # Check if the short URL is in the mapping
    if short_url not in url_mapping:
        return "URL not found", 404

    # Check if the URL has expired
    original_url, expiration_date_time = url_mapping[short_url]
    current_day_time = datetime.datetime.now()
    if current_day_time > expiration_date_time:
        del url_mapping[short_url]
        return "URL has expired", 404

    # Redirect the user to the original URL
    return redirect(original_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
