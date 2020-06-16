from models import Fiction, CompactDisc, VinylRecord, Nonfiction, Reference

catalog_seed = [
    Fiction(0, "Sirens Of Titan", "Kurt Vonnegut", 1959),
    Fiction(1, "The Heart Is a Lonely Hunter", "Carson McCullers", 1940),
    Fiction(2, "Things Fall Apart", "Chinua Achebe", 1958),
    CompactDisc(3, "In Utero", "Nirvana", 1993, 12),
    CompactDisc(4, "Siamese Dream", "Smashing Pumpkins", 1993, 12),
    VinylRecord(5, "Hunky Dory", "David Bowie", 1971, 11),
    VinylRecord(6, "3 Feet High and Rising", "De La Soul", 1989, 16),
    Nonfiction(7, "The Columbian Exchange", "Alfred Crosby", 1972),
    Nonfiction(8, "Imagined Communities", "Benedict Anderson", 1983),
    Nonfiction(9, "The Rise and Fall of the Plantation Complex", "Philip D. Curtin", 1998),
    Fiction(10, "Wandering", "Lu Xun", 1926),
    Reference(11, "The Oxford Dictionary of Word Histories", "Linguistics", 2002),
    Reference(12, "The Associated Press Style Guide 2019 Edition", "Journalism", 2019),
    Reference(13, "The Chicago Manual of Style, 17th Ed.", "Academic Publishing", 2017),
    Fiction(14, "Edges: 13 New Tales from the Borderlands of the Imagination", "Multiple Authors, ed. Ursula K. LeGuin", 1980),
    CompactDisc(15, "w h o k i l l", "tUnE-yArDs", 2011, 10),
    Nonfiction(16,"Black Lamb and Grey Falcon", "Rebecca West", 1941)
]