classDiagram
    Monopoli -- "2..8" Pelaaja
    Monopoli -- "2" Noppa
    Monopoli -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Pelaaja -- "1" Pelinappula
    Ruutu "1"-- Pelinappula
    class Ruutu {
      SeuraavaRuutu
    }
