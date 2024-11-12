import requests
import pandas as pd

# Dictionary for translating weather descriptions from English to Indonesian
deskripsi_cuaca_id = {
    'clear sky': 'cerah',
    'few clouds': 'berawan',
    'overcast clouds': 'mendung',
    'moderate rain': 'hujan sedang',
    'light rain': 'hujan ringan',
    'shower rain': 'hujan gerimis',
    'rain': 'hujan',
    'thunderstorm': 'badai petir',
    'snow': 'salju',
    'mist': 'kabut'
}

def ambil_data_cuaca(kota, api_key):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={kota}&appid={api_key}&units=metric'  # Add units=metric
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Error {response.status_code}: {response.text}')
        return None

def analisis_cuaca(data):
    if data is None:
        return None
    
    forecast_list = data.get('list', [])
    dates = []
    temperatures = []
    humidities = []
    weather_descriptions = []

    for item in forecast_list:
        date = item['dt_txt'].split(' ')[0]
        dates.append(date)
        temperatures.append(item['main']['temp'])  # Temp in Celsius due to units=metric
        humidities.append(item['main']['humidity'])
        desc = item['weather'][0]['description']
        weather_descriptions.append(deskripsi_cuaca_id.get(desc, desc))

    df = pd.DataFrame({
        'Tanggal': dates,
        'Temperatur (°C)': temperatures,
        'Kelembapan (%)': humidities,
        'Deskripsi Cuaca': weather_descriptions
    })

    # Daily aggregation
    df_daily = df.groupby('Tanggal').agg({
        'Temperatur (°C)': 'mean',
        'Kelembapan (%)': 'mean',
        'Deskripsi Cuaca': lambda x: x.mode()[0]  # Most common weather description
    }).reset_index()

    df_daily.index = df_daily.index + 1  # Start index at 1
    return df_daily

def main():
    kota = input('Masukkan nama kota: ')
    api_key = '001664eaec451b2c1b961a609c2de8ee'  # Replace with your API key

    data = ambil_data_cuaca(kota, api_key)
    df = analisis_cuaca(data)

    if df is not None:
        print("Hasil Analisis Cuaca:")
        print(df.head())
        
if __name__== '__main__':
    main()