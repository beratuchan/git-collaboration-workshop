import random

def get_info():
    news_list = [
        "Son Dakika: NCPD, Watson bölgesinde siber-psiko alarmı verdi!",
        "Ekonomi: Arasaka hisseleri güne düşüşle başladı.",
        "Spor: Yeni sibernetik boks turnuvası bu akşam Pacifica'da.",
        "Magazin: Lizzy Wizzy'nin yeni albümü piyasaya sızdırıldı."
    ]
    secilen_haber = random.choice(news_list)
    return f"📰 Günün Haberi: {secilen_haber}"