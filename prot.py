def encode_protein(s):
	"""Given a string of RNA, produce the string of amino acids it encodes"""
	codon_map = {
		"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I",
		"GUC": "V", "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L",
		"AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A", "UCC": "S",
		"CCC": "P", "ACC": "T", "GCC": "A", "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
		"UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N",
		"GAU": "D", "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "UAA": "Stop", "CAA": "Q",
		"AAA": "K", "GAA": "E", "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C",
		"CGU": "R", "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
		"UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G", "UGG": "W", "CGG": "R", "AGG": "R",
		"GGG": "G"
	}

	protein = ""
	for i in range(0, len(s) - 3, 3):
		nucleotides = s[i:i+3]
		if nucleotides not in codon_map:
			print "Couldn't find match: " + nucleotides
			return "Fail"
		codon = codon_map[nucleotides]
		if codon == "Stop":
			return protein
		protein += codon
	return protein

print encode_protein("AUGGCGAUACAAUUUAUUAGCUACUUGAAGUCUGACAAACCCUCGGCGAAAGAGAGCGGGGGGCCCCUGGAAGGCACCGUAGGUGGACACCCCCCUAGCGAUGAAGUGUCGGAAACUCGUACUUCGUCACCCAUCUGUACGAAUCUCCACUGCGGCACCCGCUACCUCGCACCUCACCAGAUUUUCAACCACAGUAAUUAUUCUGCUUUCACUUGUCACGGUGUCUUUAUUAUCCGUUAUUGGCUUUAUGCUCCGUUAGAUCCCAUCUGUCAGAGGCAUCUGCUGGCUAUUCGGGCCAAACCAAGGGGGACACAUUGGCAAAGGCCAUCUCGUAAAAUGUUCGGCCCACGAAGACGGGGCAUGAAAGUUUCAAGUAAGCAGUCCGCAUUCAAGUCGCAUCCCACGCCUAUGCUCGUUUAUAUUAGUAGGCAGGCAGGUCGGGCCAUCAAAUUACUCAAGCUUAUUAUAUGGAUCAAAGCUUUUUUCCCUAGUUUGUCCGAGCGUAUACGACGUACCAGUCUUAAGCAAGAGAGGCGCCGUAGUGGGUACGCCGACAUUUCCCUGUCCCGGACAUCCAUUCGGCACCGCCUCUGCCCAAUCCGGUUCUCUCUGGGGAUAGGGUGGAACUGUACCCUUAGUAACAUGAAUCAUGGGGCAGCUGUCCUCAUCUUCGCGGGGAUACUUCGCAUACUUCUGCGAGACACCCUCGCCCUGCCAAGUGCUAGAUCCGUACUGAACGCGCUUAUGGACCCCCCGUUUCUACUAAACACGAUAGCUCCGAUACCCACUCACGCCUCAGACGGGCGCAGGCAUCCUGCGAGCUGGCGUGUACACCCCUGGGGGAAACUACAAUAUGUGUUGUCCACGAGUCCUCACACAAGAGUCGGUCAAAAAAAGACUCCCCGUAUGCAUCCGCACGGGAUGACCAGGAAUCCACUAAGCCUGCUCUCAAUUCUAUUUAGGCGUACUGGAUACACCCAGGAGGCUGAGGUUCUCCUUUGCGCGGACAGAGAACCCAUCUAUUGGGUCGCCGUCCAACCUCACUGGGAUUGGAUAAGGCUGUGGGGAUCGAAGCGAUUGCAGGUCCUGAUAGUUAAUCGAGACAGUUGGGGCCUAUGCGCUCAGGCCGACUUCGGGGUUUGCGUUUUUCAGUUGAUACGCUAUGGGACGGCCAUAGUAUGUAUGACGUCAGUAUGUCUUAAGUCACACGGUACGGGCACUGCCGUCUUUCUCUACGUCAUCCCACCAAUGGCCCUUCCUAUGUGCAGGCUAAAGUUGGGCCAAUGGGAGCCAGCGACUUUAAUCUCCCAAGGUUCUCUAGCACGUACUCCUCCAAAGAACCAACUGUCGAAGGGUCAGCCGACCUUAGUUCACGGUGAACGUGUAAGUUGGCGGACCCGGGCGCCGACGAAGACCCAGUGGCGUGCUUCUCUAAGCUGGCAAUCACAACGGCCCGCCCUCAUAACACUGGGACAUCUCGUGGAGUGUCUUUUGAUUGUCAUCUGGGGGGUACGGGGCGGCGCGUGUCAAAGGUUAUUACCGCUACCGCGUAACCACCUACGAGGAUGGGCAGUGCUUAGCAUGAUCCUGGUGGAGUCAGGCAUCGCGCCGGGGAUGAGAACGGCGGAGAUCUCGCGAAUAACAGAGACGCUCAUAAUACGAAAAAGUGCGCUUCUCUUGAGACCUGCAGAGAGAAGGGGGACUCUAGGGACCGCUUAUCUCCUCUCGGUGCAAAAUUUGCCACCCAUCCCAGUGAACAUGUGCACGGCCAGGGCAUGGAUCCCGGCGCAUGAGUUGGUCAGAGACACACGUCCAUCGCUACCGGACCACUCCUUCGCCGUCGGAUUAAACGUCUUUCCGGGUUCGGCGAUUCCCAUACAUCCUUGUCAUGGGAUUCGGGUUGGCCCAGGUAUCUGUCGUAGGUCGUGUAAAAUGGCUGGUCCGUGUUCAUGCAUGGGUUUUCUAUGCGUUUCGCUAAAGAAAGGGCGUAUGGGAGUGCCUUUCAGCUUGUUCACACGGAUCCUGCGAUCAUUUUAUCACGUCUGGUCGGCCCUAACGUACUUGACGUACCCCAUCCGCUACUCGCUUUUAUACGCACCUGAGCGUGACCUGAAUAGAAUCAUGUGUACCUUACUACAGACGUCAGAAUCUCUUACUGACGAGUCGGGGGGGAGUCGGACUCGCGCCAAGGUAACAUGCAUCGGACAUGCCCUUAAAUAUCCCACCCUCGAUGGCAGGACCGUAUAUGACAGAUUAACGCCUAGAAAGAUAGGCUUAGCUCAAAGCUAUACCUUUGACGUGCUCACGUUCCGCCGCAAGCCGCAAACAGUGCCAAUUCCGAAGUUUUCUCAACGCGCUUGGUGGGGGUUAUAUCCCGGCCUCAACUCAAAAUUACUUUUAGGCGCCUGUCCCGGCGCAAAACAAAAAAAGGAGAACCUUACCGGGGAUCCACCUCGAGGCAUACGCACGGUCCACGAUCCUUCUCUUCGACGGAAGCCAAGAAUGACUCUCUUUCCAUGUACCGCGCCAGCUAUGUGCACUUUUUCCGACCCAUUUGGAGACAUCCCCCUGUGCCUUCUAUCGUCACGCGAGCAUCGUCCGCAGUUAAGGUCGCGGACGGCGUUCUCGUACGCGGACACCCCUACCAUGACCUCUAGGCCCAACCUGAUAGGACUGGCUACAAUUCCACGUUAUAUUAAUUCUUGGAGCCCUGUCUAUGAUAGCGUCGCAUUUCGCAGGUCGGCGACCGAUAGUGCCCGCUGCUAUGAUAUGACGGAGCUUAAAAAUAGCGCUGAUGACUUAUCUCGAGGACGCGUGCCAGUAAUGACCACGAAACAUGCUGAUGUGAAUAUAUUCCCAGUCACAACUGCACGGGAUCCGAUAAGUUCUUCGCAUAGAGCAAUGGUACACAUACCGAUAUGCAAUGGAACUACAGGUACUGGCUUAUUCAUUACGGAGUUUACCCUCCAGAUACCCAACAUUACAGUUCAUCGGCUCCCAUCUCCCAGUAUUUCUUGCCGUAGUGCACUUACUCAGUCCACCCUAGAUUGUACUCUGGCAUUGUGCUCCCCGCCAGAUCUUUCAAUACCUCGGCAUAGCGAAACAACUAUGCUGCCGGCAGUGGACCCUCGGUUACUUGCUUCAGAGAGGCAGGCGGGCGUUGCGCCGGUGGCUUCUGCAUACGUGAGAUGGCCCGGGGGCCGGAUCGUGGGGUACACAUACUCCUGGACUGGCCUUUGUCUGAAGGCGGCGCGGACUUAUACGCAAGCUUUAAUUUUAUCGUGUGCUCACUGUGGACACAAAUGCGUUUUUCCGUUACCGGUGACACUUGUCCAAUCGUGCCGAACUAUGGCGAGAGUGGUUUAUUCCCUCACCAAGUUGCACCCUCCAAAACCAAGCAGAAUGUACUCACAAACCGACAGGAACACCGAGGAACUAUCCGAAUUGUCUCCUGGCGUCGGACGACCAAACACUAUUUCAGAUUGGACACGCGCCCCGCUCAUACCUAUGGAGAUCCAGACCCCACUCAAUUCGCUAGCCUGGAGCAGGAUUAUAUGGUUCAACCGUGCUUUAGGGACCGUUCCGCAGACUCUGGAAAUGCUGACACGUUACGAUUCUUUUAGGUUGACCAGAGUGGGUUUGUAUUAUCCCCAGAUGUCGGUAAGCAGACCGUUCAGAAUAAACGACGUUGGGAGGCUAGUUCCAAUCGGAUCCUACCCUCGCCCUAGCGAGCGUUGUGCUACUACUAAAGUUACUCCCGAUCUGCGGACUCAACCCUUAGCCAUCGUGUUACUACGGCGGACGUCAAGCAUGGUGUUCGUACGGGUAGACAGUGGCAGUCUUGCACUUAAGGAUCGGACGCUAGUCAAUCAAGGGUCGUUUACAGCUGAUCUUUUGCAAUGCCAAACACCCAUACAGAGAAAUUCCCCGAGCAAUCUCCAGGGCUUUCACAGUGAGAAGACGCGGAUGACAGUAACGGAAGAGUUCCGGGAGCUGUCUUCUUUGUCGGUCUUAGCGCCUGAAGACAACGCUGGGUCAAAGGGCCCCGCAUCCAUCCUCUACCUACGACGAUUUUCUAUUGAGUUGUUCAGCUUUUUAGGAGGAUUGAAUUUCUCGUCUAUUUGGAUAACGAUCGAUAAUAGUCAACACCUAGCUAGACAGCUUAGCCGGACGGUCACCAAAGAUCUAAAGUUUUAUUCCAAAAUAUCGAAAGAUUGCUCGGUCUUUCCGUUGUGGCGAACCUUAACGUCCUCUGUUGCAAUUAGCGCAUUGCAGAAGCCUAAUAUGCUUGAAAGGACGUUGGGAGACUAUCAGGACGCGAUUGGAGUUCAGUCACCCGAAAGCAGGCGAGCCCCUUGUACUGCCCCUUUGCGACAUCGUAUGUUGCCCCGACAUAACCAGUCAGGCCUUGCGGUAUAUUCCGAUCGGAGGCCAAGAUUGGUAUUUAUACCCCUAGGGCGGCGUAAUGAAGGCCGAUCCUUGGACGCAUGGCUCUUUGGAUGCUGGCUUCGAGAGAUGAACGUGGCAAUAACUUCAUCCCAUCUGAGCAGUCGCCGGAAUUGUCCGCAUCUCCGUCGUGAAGACUGGUUCUUCUCCUCCCAUGUCAGAGUAACCUCACUAGAGUUAACGGAAAGGUCGUCUUGCGAUGAAGUACCCACUCUGAUUAGAUUCCGAUCGUUGAUGGGGAAUGAUUUUGCCCUUGGCAUUGGCUACAAUUAUCAGACGUCCUCAUUGUAUGCAUGGUCGUUCGUGCCUGCCGCUGUCAUCCCGGUCAACCAAGAUGUAAGAGCGGGGAGGAUUUUUUCCGAAUGUACGACGUUGGAAAGUGCUCGUUACCGUGAGGAAAUCUACGUGACAAGUAAGGUGUUCAAGUGUCGUAAUCUUGCCUGCGCUAGCGGUUCAGCUAACGUAAAGCAAGGUGGGAGCCUGGCUGGCGUACGGCAGGUGAUCGUAUCGACCCAGCUAGCAACCAAAGUGGCCAUUACCAUUACCAGAGAACCCCUUUGCGCCACUCCUGUGAAUUACGCUGUAACAAUUGUAUACUCACCAAACCGAGCACAAAUCAGGGUUAGGUACCGCGACUGCAUGACAACUGAAUGCGUUAAGACACAGCAUUCGACUUGCGACCACCUGAUAAUACCUACGUUGAGGGCUCCGUACGCGUCUUGUACACGAGGUGCCUUGCCCGGAUCCUUCGGUAGCGGGAAUACGGCACUGAUAGUUUGUGUGUUCGCACGCGCACUCGUCCGGUAUGAAAAAGCUGCCACGAUCCAACAAUGGCAUCAAUCCCUGUACGUACGAAAGCUAGUGCUAAAUACCGUAGGAGGUAUCUUUGCCCACGCUGUAUCGGCGAGGUACGGUAUGACUCCAUGUAGACAGUCUGAUCUAGGUCGUCCCCGACAACCAAUUAGCGAAUUCUUCUAUCUGAAAUCCCUCGCGUCCGGGAAAGCCAUACGGCUAUUGACGUAUUGCCUUGGUCCCAAGGUGUACGUACUAGUUGCCCGCCUAAAGUCCCGUCGGUAUAAUAUAGAGGGGAGAUCCCGAUAUUUCACACGUCUCAACAGCUAUCCACCCGCGUGGUUGGGGAUUCUUCAGAUGAGAUUAGACAGUGAUGUGCUUACCGGACAGGCAGCGUUACAUAUUCAUAUCGCAUUAGCGACGAUCAUCAUCUAUGAGCCUCGCGCCACUUAUACGUCUCACAGUAAACAGUGCUAUUCCUUAGUGUUCCUACGUGUAAGCAGCCAUUUAGCACCUACGGCAUUGACAAACGUCAUAGGUACCGUGUGUACGAUAAGAGGCUCAAUUCCACCUGGCAGGAAAACGCAAAAGCUUCUUCUCUCAAAGACCGCCUAUUUUGGUGCCCGUCUAUACGUGUAUACAAUAUUGGGGAAUCAUUAUGGCAACAGGCAUGGAAUAGAUGGGCUGGCUGGCCGCCAUUUGGGGGGUCCUGUUGGAUACCUCUCAGCCACCUUGGGUAUGCAGCAGUGCCGUGCUUGCCGGCCUGCCCGCCAACCGGACCAUUUGGGUCUUGCCCCAAGGAGUAUUGUUAGCGCUACCAUGGGAGUUAAUAACAACCGUCCGAGUGUCAACCCAAUGCAGGGUGUGCUAUAUCCCUUCGGAGAGUGUUGCUUUCGGCCGAGGUGGAUUAGACUUUUGUUUAACUUGAUGCUUAUAGCUCGGUCCCUUAAAAGCGCUAAAACACGGGUGCACCGGGAACGUCAAUCGUGGCCGCGGGUUGGCGGAUUCCGCACACUGGGUAUGCAUAAACUAACCCAUAAAUCUUCGCUUCUUUUCUUGUGGCCAAAUGAUCCGUCUACGCUUUCAGCGGGGGGCAUCUGGUUGCUAUUGGCCAUGCGCCAUGCUAUAACCGCCUUAACUGUGCGUUCAAGUAGGGAAGGAGGUAAUCCUUCUAGUAUUUUAAGCACGGCACAAACACCACGAAGGAGAAAGAUAGUCCCCCUCUCGAAGAUAUAUCACGUAGAACAUAGUAUAAAAAGGCUAAGAUUGAUCAGACAGCCGGCCGGUCAAGUUACUGUGUCCAUACGUGAGGUACCGAUCAGUGGCGAAUGUCGGAGGAUCGAAGGACCACUACACCUCUGCUGGGGCCACCUGAGAGGCGAGAUGUUAUGCCACUUUCCUUGCUACAUACCUCGUCAGCUCGUUUUUCCACGUUUGUUCCCUCAAAGAAAGAGACUGCCCGAAAAUUUCCUGAGUGCAGAGUCUGUGCCCGCAUCACAAGGUUCGGCCUCUCAAGUUCCGCACGCCUCCGCGAAUCAUGCCCCCGGCGGAAGGGGGCAUUGGGCGCUCGCCUGCUCUCCGGCGAGUAGGCGAUUUUUGAUGAAGAGUAACAAACAUACCGUUCCAUGGAGAGCAUGGUUGACUGAUAGGAUCCGACCAUUAACAAAGCUGGAACCCGUACAGGUGAACCUCGUACGCAACAUUGCAGGACGGGCCUCACUUUUGCUUUAUCGUGUCACAGCGACGCAAUCAGUCUUUCAACCUUUUAUGGACACUCUUAAAGGGAGUGGUAAAAGAGCAUUGCUGUUUUCGAGUCGGUCUUCACGGGAUGCUUUCUGGAAACUAAACUCAGGGCGAUCUCCAUGGUGCAAGCGUAUGGUCCAAACGGUAUUAGAAGGGAAUAUCUCUUUGAGUCACGUGAGCUCUCAGCCACCCUUGGUUUCGGAUAACGAACAGGUACCGACUUUUGCCUCCACUCGAUUCCUCCAGAAACGAUACCCGCCCGUAUCAACAGGGCUCGUGGAGGGGCACGAAAUCCAAUACGGUUCUCAAGAUUGUCGUCGGGGUGGUUUCGAUGCGAUAACGAUCUGUAUUCUUUUGGCCACCGCAGCCGUGACAAGGGUGUUGAAGUCGACUGAGCCACAAUUGAAUUCCUGUCACCCCAUACCGAAUCCGUUUUGCGACUGGGGUCCGUCGAGGAUAUUGAAGUCCUGGUUCUUUGCACAUAAACUCGUGUUGGCAUUUCCAAAUGCGGUGCUCCGAGUAGAUGAUAGUGUUUCAUUUACACAGCCCGUUAUUGCGGUGUCUGGGAGCUCACCCUACAGCAGUGCACCUCAAAGAAGUUCAGCUCGUAGGCACUGCCUUUGCUCAUGGCUUUUAUACUGUAAUAAAUUUUGCAACUCGUCCCAAGUCCUAUCAAUGGAAAUUCAGAAAUUAAUUGGGGGAUGCUUUAACUCUGCCUCUAGCAGUGAGCUAUGGCCUGUGCUUCCAUGUAUGGAUUCUACUGACUUAGAACAUGACUCCCACACGACCCUGAUGUCUACACUAGGCCGAAGUUCGAAUAUACGUAAUGUGAACGCGGUAACUGUAAUAUGUCGGAUCGCAAGCCAAGCCACAAUCGGCCUGUGUGUGUUGUCAGUUGGCGCCGGUGUACAAGAAAACAGACGCUACAUGAGGAGACAUAUAGGUCGGGGAGCUCGUAGGAGUGUAGCAAAAAGAAUUCAGUCCUACGCACCAAAGCUCACUGUCACGUCUCUUCCAUUGGCUACGUCGUAUGAUUCCCGCUCGGUGCCCCCAGUCGAGUGUCAAGGUGGGAUAGUUAAAGUGCCCCGCGCUCAGGAGAAAGGUUUGACAUGCGACCGGUCUCGUGCCGUACCCGUACACUGCCAUAAUACGCUCGGCCAACUUUUAUGCCACAUCAACUACCAUAAUCUACCGAAGUCCCCAUCUCGGAUUUGUUUUCGUGUAACUCUCGUACAUUACAAAUCCCGAUUUCGGGCGCCUCCAACGUAUAAGCCUAGCGGAACAAAAGAGGCUUUGGGUGUUCGCAUGUUUCGUACCUAUUCACGGUGUCAUUCGCCAAAGAUUUGGGGCUUCGGCUCCCCGGGAUUUGCCAUACAUUAA")