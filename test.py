my_list = [(40519703338693047098046551461490771877693972925937156430379281159200973865945, None), (51415526187165309223257705330680039425097166625607158775516718352801665442947, 98025279793103591817278333464241644374117654604560165491829684220734133806299), (74081216277933700831666362873884292484477686029261302989101722970889414584260, 46190838286468323486518277916624770995230518560480635961743438504412281312464), (87232867512800820149225834913766453011385964520743497948671152639417134153656, 37902687813451407171590838006256453159127491026539978658405087392569829986089), (88884070595172305137326465706021258325880335925625458099222754747713420900898, 3244963033710949589107910750652644972420408154684900723066781226121673657910), (61657872140099229389288501139160444557520431347927262366744797531544372220235, 63248533975343254938568295093715597911392247246186577963215615209673137217579), (90818992826722103056822498785079578254991301278765808008321174021341719804515, 48536876381144348264304422234202024488018488280628662821371182664081150663997), (37884512962717325989478589158672435020081076349246919356251696887303447419077, 89505016775626710852756529805476865557703846510446294422920634291311443829406), (91517649428097557648644209727151311818462908120864238705823097261965444379360, 85584059333745617441790466370692826278227819702407808425748711876667690871691)]
new_list = [tup for tup in my_list if tup[1] is not None]
print(new_list)