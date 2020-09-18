import geopy
import pandas
from geopy.geocoders import Nominatim, GoogleV3

def main():
    data = pandas.read_csv('../2019/bairros_2019.tsv', index_col=None, header=0, sep="\t")

    # Métodos para extrair informações de localização

    def get_latitude(location):
        return location.latitude if location else "-"

    def get_longitude(location):
        return location.longitude if location else "-"

    ## Geolocator: nome -> localização 

    geolocator = Nominatim(user_agent='student-application')
    
    # agregar endereço 
    data['helper'] = data['bairro'].map(str) + " " + data['cidade'].map(str) + " " + data['estado'].map(str) + " " + data['pais'].map(str)
    coluna_geolocate = data['helper'].apply(geolocator.geocode)
    data['latitude'] = coluna_geolocate.apply(get_latitude)
    data['longitude'] = coluna_geolocate.apply(get_longitude)
    data.to_csv('bairros_19_geocoded.csv')
    
if __name__ == '__main__':
    main()