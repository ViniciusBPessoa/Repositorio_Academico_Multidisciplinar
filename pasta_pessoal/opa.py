from google_images_search import GoogleImagesSearch

def download_images(query, limit):
    # Configure API key and cx (context) to use Google Search API
    api_key = 'AIzaSyB_YujZhK9XjedhFd4_rTYCmlMCJcAflFI'
    cx = 'e40530e8ad903413c'

    # Create an instance of GoogleImagesSearch with your credentials
    gis = GoogleImagesSearch(api_key, cx)

    # Set search parameters
    search_params = {
        'q': query,
        'num': limit,
        'safe': 'high',
    }

    # Perform the search
    gis.search(search_params=search_params)

    # Get the URLs of the images found
    image_urls = []
    for image in gis.results():
        image_urls.append(image.url)

    # Download the images to a local directory
    path_to_save = 'path/to/save/images'  # Set the path to the directory where you want to save the images
    gis.download(image_urls, path_to_save)

    # Print the URLs of the images found
    for image_url in image_urls:
        print(image_url)

# Example usage
search_query = "cachorro fofo"
images_limit = 5
download_images(search_query, images_limit)
