import pygame
from pet import Tamagotchi

# Inicjalizacja i ustawienia
pygame.display.init()
pygame.font.init()
SZEROKOSC, WYSOKOSC = 400, 450
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Tamagotchi")
zegar = pygame.time.Clock()

# Kolory
KOLOR_TLA = (200, 200, 200) # jasnoszary
KOLOR_CZARNY = (0, 0, 0)
KOLOR_BIALY = (255, 255, 255)
KOLOR_ZIELONY = (0, 255, 0)
KOLOR_ZOLTY = (255, 255, 0)
KOLOR_CZERWONY = (255, 0, 0)

# Czcionka
CZCIONKA = pygame.font.SysFont("Comic Sans", 20)

# Funkcje pomocnicze
def okresl_kolor(poziom):
    if poziom > 70:
        return KOLOR_ZIELONY
    
    if 30 <= poziom <= 70:
        return KOLOR_ZOLTY
    
    return KOLOR_CZERWONY


# Inicjalizacja Tamagotchi
tamagotchi = Tamagotchi()

# Główna pętla gry
koniec_gry = False
while koniec_gry != True:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE: # klawisz Escape
                koniec_gry = True
        elif zdarzenie.type == pygame.QUIT: # przycisk zamykający okno X
            koniec_gry = True
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN:
            if przycisk_nakarm.collidepoint(zdarzenie.pos):
                tamagotchi.nakarm()
            elif przycisk_pobaw.collidepoint(zdarzenie.pos):
                tamagotchi.pobaw_sie()
            
    tamagotchi.aktualizuj()
    
    ekran.fill(KOLOR_TLA)
    
    # Interfejs
    ## szczęście - pasek i napis
    kolor_szczescie = okresl_kolor(tamagotchi.poziom_szczescia)
    pygame.draw.rect(ekran, kolor_szczescie,
        pygame.Rect(50, 50, tamagotchi.poziom_szczescia * 2, 20))
    tekst_szczescie = CZCIONKA.render("Szczęście", True, KOLOR_CZARNY)
    ekran.blit(tekst_szczescie, (50, 20))

    ## głód - pasek i napis
    kolor_glod = okresl_kolor(tamagotchi.poziom_glodu)
    pygame.draw.rect(ekran, kolor_glod,
        pygame.Rect(50, 100, tamagotchi.poziom_glodu * 2, 20))
    tekst_glod = CZCIONKA.render("Głód", True, KOLOR_CZARNY)
    ekran.blit(tekst_glod, (50, 70))
    
    ## przyciski Nakarm i Pobaw się
    przycisk_nakarm = pygame.Rect(225, 300, 150, 50)
    przycisk_pobaw = pygame.Rect(25, 300, 150, 50)
    pygame.draw.rect(ekran, KOLOR_BIALY, przycisk_nakarm, 3)
    pygame.draw.rect(ekran, KOLOR_BIALY, przycisk_pobaw, 3)
    
    ### teskt przycisków
    tekst_nakarm = CZCIONKA.render("Nakarm", True, KOLOR_CZARNY)
    tekst_pobaw = CZCIONKA.render("Pobaw się", True, KOLOR_CZARNY)

    tekst_szer_nakarm, tekst_wys_nakarm = tekst_nakarm.get_size()
    tekst_szer_pobaw, tekst_wys_pobaw = tekst_pobaw.get_size()

    ekran.blit(tekst_nakarm, (przycisk_nakarm.x + (przycisk_nakarm.width - tekst_szer_nakarm) // 2, przycisk_nakarm.y + (przycisk_nakarm.height - tekst_wys_nakarm) // 2))
    ekran.blit(tekst_pobaw, (przycisk_pobaw.x + (przycisk_pobaw.width - tekst_szer_pobaw) // 2, przycisk_pobaw.y + (przycisk_pobaw.height - tekst_wys_pobaw) // 2))


    pygame.display.flip()
    zegar.tick(30)
    
pygame.quit()