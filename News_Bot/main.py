from newsapi import NewsApiClient
import pycountry

# Get your API key from newsapi.org and paste it below
newsapi = NewsApiClient(api_key="YOUR_API_KEY")

def get_country_code(country_name):
    """Get the country code from the country name using pycountry."""
    try:
        country = pycountry.countries.search_fuzzy(country_name)
        if country:
            return country[0].alpha_2
        else:
            return None
    except LookupError:
        return None

def display_articles(articles):
    """Display the articles with improved readability."""
    if articles:
        for article in articles:
            source = article["source"]["name"]
            title = article["title"]
            description = article["description"]
            published_at = article["publishedAt"]

            print("Source: ", source)
            print("Title: ", title)
            print("Description: ", description)
            print("Published At: ", published_at)
            print("--------------------------------------")
    else:
        print("No articles found.")

want_to_search_again = True

while want_to_search_again:
    # Get the country name from the user as input
    input_country = input("Country: ")
    country_code = get_country_code(input_country)

    if not country_code:
        print("Invalid country name. Please try again.")
        continue

    # Display available categories and get the user's choice
    print("Which category are you interested in?")
    print("1. Business")
    print("2. Entertainment")
    print("3. General")
    print("4. Health")
    print("5. Science")
    print("6. Technology")

    category_choice = input("Enter the category number: ")

    if category_choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid category choice. Please try again.")
        continue

    # Fetch top headlines based on the user's choice
    category_mapping = {
        "1": "business",
        "2": "entertainment",
        "3": "general",
        "4": "health",
        "5": "science",
        "6": "technology"
    }
    category = category_mapping[category_choice]

    top_headlines = newsapi.get_top_headlines(
        category=category,
        language="en",
        country=country_code.lower(),
    )

    # Display the articles
    Headlines = top_headlines["articles"]
    display_articles(Headlines)

    # Prompt the user to search again or exit
    option = input("Do you want to search again? (Yes/No): ")
    if option.lower() != "yes":
        want_to_search_again = False
