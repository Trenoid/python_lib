from geocoder import Geocoder

if __name__ == "__main__":
    adress = 'tajikistan'
    print(Geocoder(adress).json)