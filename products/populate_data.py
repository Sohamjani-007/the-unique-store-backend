import pandas as pd
from products.models import Product


# sample_products = [
#     {'name': 'FABSPORTS USB Rechargeable Fancy Laser Lights, for Bicycles, Scooters, Skateboard etc Ideal Kids Gift, Accessories for Cycling, Safety Tail Light for Bicycle, Pack of 1', 'category': 'light', 'price': 1299.99, 'image': "https://m.media-amazon.com/images/I/71Qb30AHXzL._SX679_.jpg", "link" : "https://amzn.to/3xGUBYK"},
#     {'name': 'Goodscity Garment Steamer for Clothes, Steam Iron Press, Vertical & Horizontal Steaming up to 22g/min, 1200 Watt, 250 ml Water tank & 30 sec Fast Heating (GC 111), 12 month Warranty', 'category': 'electrics', 'price': 2199.99, 'image': "https://m.media-amazon.com/images/I/51hooqrZcmL._SX679_.jpg", 'link': 'https://amzn.to/4bDZMGK'},
#     {'name': 'Snazzy Acrylic Jewelry Box 3 Drawers, Velvet Jewelry Organizer, Earring Rings Necklaces Bracelets Display Case Gift for Women, Girls (Gray)', 'category': 'jewelry', 'price': 1225.99, 'image': "https://m.media-amazon.com/images/I/51KSBQ4+V3L._SX300_SY300_.jpg", "link": "https://amzn.to/3WiRpMs"},
#     {'name': 'OCEANEVO Velvet Jewellery Box for Women, Travel Earrings Organiser Box, Portable Jewellery Box Organisers for Rings, Earrings, Bracelets, Necklaces - 16 x 11 x 5 CM - Beige - 2 Layer', 'category': 'jewelry', 'price': 899.99, 'image': "https://m.media-amazon.com/images/I/71eUMughOLL._SX679_.jpg", "link": "https://amzn.to/4ctm9zM"},
#     {'name': 'NEOUTH Hanging Chandelier Glass Crystals Prisms for Window Suncatchers Chandelier Parts Rainbow Maker Pendants (89mm/3.5in)', 'category': 'crystal-diamond-suncatcher', 'price': 699.99, 'image': "https://m.media-amazon.com/images/I/81c-7sz8SsL._SX679_.jpg", "link": "https://amzn.to/4cV6NDU"},
#     {'name': 'JELLEX Magnetic Wrist Band with 3 Strong Magnets for Holding Screws, Nails, Drill Bits, Metal Tools', 'category': 'handy-tools', 'price': 299.99, 'image': "https://m.media-amazon.com/images/I/41wtKB+HtVL.jpg", "link": "https://amzn.to/4eOwQ1o"},
# ]
#
# #Add more products as needed
#
# def populate_product_data():
#     for product_data in sample_products:
#         Product.objects.update_or_create(**product_data)




# Load the Excel file
file_path = '/home/rithika/Downloads/mock_product_data.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Check the structure of your DataFrame
print(df.head())


def populate_product_data_by_pandas():
    """
    # Call the function to populate the product data
    populate_product_data_by_pandas()
    """
    # Iterate over the DataFrame rows
    for _, row in df.iterrows():
        import pdb;pdb.set_trace()
        product_data = {
            'name': row['name'],
            'category': row['category'],
            'price': row['price'],
            'image': row['image'],
            'link': row['link']
        }
        Product.objects.update_or_create(
            name=product_data['name'],
            defaults=product_data
        )


