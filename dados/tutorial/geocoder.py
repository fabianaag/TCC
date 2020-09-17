import geopy
import pandas
from geopy.geocoders import Nominatim, GoogleV3

def main():
    data = pandas.read_csv('census.csv', index_col=None, header=0, sep=",")

    # Métodos para extrair informações de localização

    def get_latitude(location):
        return location.latitude

    def get_longitude(location):
        return location.longitude

    ## Geolocator: nome -> localização 

    geolocator = Nominatim(user_agent='student-application')
    
    # agregar endereço 
    data['helper'] = data['Area_Name'].map(str) + " " + data['Country'].map(str)
    coluna_geolocate = data['helper'].apply(geolocator.geocode)
    data['latitude'] = coluna_geolocate.apply(get_latitude)
    data['longitude'] = coluna_geolocate.apply(get_longitude)
    data.to_csv('geocoding-out.csv')
    
if __name__ == '__main__':
    main()