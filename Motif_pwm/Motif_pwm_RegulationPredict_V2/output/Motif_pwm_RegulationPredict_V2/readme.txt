pos+-:	后缀代表可能调节的基因的方向，s为正向，c代表反向。
pos：	cpxR结合位点在基因组上的位置（第一个碱基，无论方向），c代表cpxR结合位点为反向。
score：	cpxR结合位点按照pssw方式的打分
seq：	cpxR结合位点的序列
regulate：	该位点可能调控的基因，判定标准：基因上游200bp或基因的前100bp“碰到”了结合位点。在此情况下，如果调控多顺反子调控只给出第一个基因；其它基因独立判定。
regulation_site: 负数代表距离基因上游，正数代表在基因上的位置，数字以最靠近基因的结合位点边界开始算。
ref_seq locus_tag: 可能调节的基因在refseq注释信息中的locus_tag，即转录组测序中所用的基因标识。可利用此列将转录组测序结果进行数据拼接（excel可完成）。