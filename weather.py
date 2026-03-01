import random

def get_info():
    # Şehir listesi ve rastgele durumlar
    cities = ["İstanbul", "Ankara", "İzmir", "Denizli"]
    conditions = ["Güneşli ☀️", "Parçalı Bulutlu ⛅", "Yağmurlu 🌧️", "Rüzgarlı 💨"]
    
    city = random.choice(cities)
    status = random.choice(conditions)
    degree = random.randint(15, 30) # 15 ile 30 derece arası rastgele sıcaklık
    
    return f"{city} için hava durumu: {status} ve {degree}°C"

