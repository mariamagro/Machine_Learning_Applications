import requests
from bs4 import BeautifulSoup
import csv
import time

# Function to scrape titles, texts of posts, and texts of replies from a forum page
def scrape_forum_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        post_urls = []
        for post_link in soup.find_all('a', class_='thread_title'):
            post_urls.append(post_link['href'])
        return post_urls
    else:
        print("Failed to fetch forum page:", response.status_code)
        return None

# Function to scrape data from a forum post
def scrape_forum_post(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        post_title_element = soup.find('a', class_='bclast')
        post_title = post_title_element.text.strip() if post_title_element else None
        post_text_element = soup.find('td', class_='postbody')
        post_text = post_text_element.get_text(separator='\n', strip=True) if post_text_element else None
        return {"Post Title": post_title, "Post Text": post_text}
    else:
        print("Failed to fetch post data:", response.status_code)
        return None

# Define base URL of the forum
base_url = 'https://forums.somethingawful.com/'

# Define CSV file path
csv_file = 'forum_posts.csv'

# Define CSV fieldnames
fieldnames = ["Post Title", "Post Text"]

# Create CSV file and write header row if it doesn't exist
with open(csv_file, mode='a+', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    if file.tell() == 0:
        writer.writeheader()

    # Iterate over forum pages
    for i in range(167, 634):
        # Define URL of the forum page
        print(i)
        forum_page_url = base_url + 'forumdisplay.php?forumid=273&daysprune=30&perpage=40&posticon=0&sortorder=desc&sortfield=lastpost&pagenumber=%s' % i

        # Scrape post URLs from the forum page
        post_urls = scrape_forum_page(forum_page_url)

        if post_urls:
            # Iterate over post URLs and scrape post data
            for post_url in post_urls:
                # Add base URL to post URL if necessary
                if not post_url.startswith(base_url):
                    post_url = base_url + post_url

                # Scrape data from the post
                post_data = scrape_forum_post(post_url)

                # Write post data to CSV file
                if post_data:
                    writer.writerow({"Post Title": post_data["Post Title"], "Post Text": post_data["Post Text"]})

                # Add a delay between requests to avoid overloading the server
                time.sleep(2)

    print("Post data has been saved to", csv_file)
