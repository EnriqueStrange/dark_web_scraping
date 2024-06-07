from torpy import TorClient 
from torpy.http.requests import tor_requests_session
from bs4 import BeautifulSoup

def scrape_dark_web(url):
    # Create a Tor client instance
    tor = TorClient()
    # Create a Tor circuit
    with tor.create_circuit(3) as circuit:
        # Create a session using the Tor circuit
        with tor_requests_session(circuit) as session:
            # Perform a GET request to the given URL
            response = session.get(url)
            if response.status_code == 200:
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')
                # Example: Extract all paragraph texts
                paragraphs = soup.find_all('p')
                for p in paragraphs:
                    print(p.get_text())
            else:
                print("Failed to retrieve the page. Status code:", response.status_code)


if __name__ == "__main__":
    url = "http://exampleurl.onion"
    scrape_dark_web(url)

