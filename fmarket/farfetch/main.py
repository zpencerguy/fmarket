from fmarket.farfetch import api
import datetime

date = datetime.datetime.today().strftime('%m-%d-%y')

api = api.Api()
total_pages = api.get_listings()['totalPages']


def run():
    for page in range(1, total_pages + 1):
        print(page)
        api.parse_products(
            api.get_listings(page=page)
        )
    return api.df


if __name__ == 'main':
    run()
    api.df.to_csv('current_farfetch_listings' + date + '.csv')

