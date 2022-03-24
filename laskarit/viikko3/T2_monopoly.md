classDiagram
    Monopoli -- "2..8" Pelaaja
    Monopoli -- "2" Noppa
    Monopoli -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Pelaaja -- "1" Pelinappula
    Pelaaja "0..1" -- "*" Katu
    Pelaaja : rahamaara
    
    Kortti -- Yhteismaa
    Kortti -- Sattuma
    Kortti : teeJotain()

    Ruutu <|-- Katu
    Katu : nimi

    Talo "0..4" -- "1" Katu   
    Hotelli "0..1" -- "1" Katu
    Ruutu "1"-- Pelinappula

    Ruutu : seuraavaRuutu
    Ruutu : teeJotain()

    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- Sattuma
    Ruutu <|-- Yhteismaa
    Ruutu <|-- Asema
    Ruutu <|-- Laitos
    Aloitusruutu <|-- Monopoli
    Vankila <|-- Monopoli