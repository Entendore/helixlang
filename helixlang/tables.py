CODON_ORDER = [
    "UUU","UUC","UUA","UUG","UCU","UCC","UCA","UCG",
    "UAU","UAC","UAA","UAG","UGU","UGC","UGA","UGG",
    "CUU","CUC","CUA","CUG","CCU","CCC","CCA","CCG",
    "CAU","CAC","CAA","CAG","CGU","CGC","CGA","CGG",
    "AUU","AUC","AUA","AUG","ACU","ACC","ACA","ACG",
    "AAU","AAC","AAA","AAG","AGU","AGC","AGA","AGG",
    "GUU","GUC","GUA","GUG","GCU","GCC","GCA","GCG",
    "GAU","GAC","GAA","GAG","GGU","GGC","GGA","GGG",
]

NCBI_TABLES = {
    1:  {"name":"Standard",
         "aa":"FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
         "starts":"---M------**--*----M---------------M----------------------------"},
    4:  {"name":"Mold/Protozoan/Coelenterate Mitochondrial; Mycoplasma/Spiroplasma",
         "aa":"FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
         "starts":"--MM------**-------M------------MMMM---------------M------------"},
    11: {"name":"Bacterial, Archaeal, Plant Plastid",
         "aa":"FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
         "starts":"---M------**--*--------------MMMM---------------M------------"},
}
