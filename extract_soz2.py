# The raw markdown from firecrawl_scrape response
# I need to extract the Altinci Soz section
import sys

# Read the actual response data - I'll embed it directly
raw_markdown = """# Beşinci Söz

﷽

اِنَّ اللّٰهَ مَعَ الَّذ۪ينَ اتَّقَوْا وَالَّذ۪ينَ هُمْ مُحْسِنُونَ

Namazkılmakvebüyükgünahlarıişlememek; nederecehakîkibirvazife‑i insaniyevenekadarfıtrî, münâsipbirnetice‑i hilkat-i beşeriyeolduğunugörmekistersen, şutemsîlîhikâyeciğebak, dinle:

Seferberliktebirtaburda, birimuallemvazife‑perver; diğeriacemînefis‑perverikiaskerberaberbulunuyordu. Vazife‑pervernefer, tâlimevecihadadikkat eder, erzâkvetâyinâtınıhiçdüşünmezdi. Çünküanlamışki; onubeslemekvecihâzâtınıvermek, hastaolsatedâvi etmek, hattâinde'l‑hâcelokmayıağzınakoymayakadardevletinvazifesidir. Veonunasılvazifesi, tâlimvecihaddır. Fakatbazıerzâkvecihâzâtişlerindeişler. Kazankaynatır, karavanayıyıkar, getirir.

Onasorulsa: “Neyapıyorsun?”

“Devletinangaryasınıçekiyorum.” der. Demiyor: “Nafakamiçinçalışıyorum.”

Diğerşikem‑perverveacemîneferise, tâlimeveharbedikkat etmezdi. “O, devletişidir. Banane!” derdi. Dâimnafakasınıdüşünüponunpeşindedolaşır, taburuterkeder, çarşıyagider, alışveriş ederdi.

Birgünmuallemarkadaşıonadedi:

“Birader, asılvazifentâlimvemuhârebedir. Senonuniçinburayagetirilmişsin. Pâdişahaîtimat et. Oseniaçbırakmaz. O, O’nunvazifesidir. Hemsenâcizvefakirsin, heryerdekendinibeslettiremezsin. Hemmücâhedeveseferberlikzamanıdır. Hemsana‘âsîdir’ der, cezaverirler. Evet, ikivazifepeşimizdegörünüyor. Biri; pâdişahınvazifesidir. Bazenbizonunangaryasınıçekerizki, bizibeslemektir. Diğeri; bizimvazifemizdir. Pâdişahbizeteshîlâtileyardım ederki, tâlimveharptir.”

50

Acabaoserserinefer, omücâhitmuallemekulakvermezse, nekadartehlikedekalır, anlarsın!

İşteeytenbelnefsim! Odalgalımeydân-ı harp, budağdağalıdünyahayatıdır. Otaburlarataksim edilenorduise, cemiyet-i beşeriyedir. Veotaburise, şuasrınCemâat‑i İslâmiye’sidir. Oikineferise; biri: Ferâiz‑i diniyesinibilenveişleyenvekebâiriterkvegünahlarıişlememekiçin, nefisveşeytanlamücâhede edenmüttakîMüslüman’dır. Diğeri: Rezzâk‑ı Hakîki’yiittiham etmekderecesindederd‑i maîşetedalıp, ferâiziterk edenvemaîşetyolundarastgelegünahlarıişleyenfâsık‑ı hâsirdir. Veotâlimvetâlimatise– baştanamaz– ibâdettir. Veoharpise, nefisvehevâ, cinveinsşeytanlarınakarşımücâhede edip, günahlardanveahlâk‑ı rezîleden, kalpverûhunuhelâket‑i ebediyedenkurtarmaktır. Veoikivazifeise; birisi: Hayatıveripbeslemektir. Diğeri: Hayatıverenevebesleyeneperestiş edipyalvarmaktır. O’natevekkül edipemniyet etmektir.

Evet, enparlakbirmûcize-i sanat-ı Samedâniyevebirhârika-i Hikmet-i Rabbâniyeolanhayatıkimvermiş, yapmışise, rızıklaohayatıbesleyenveidâme edendeO’dur. O’ndanbaşkaolmaz! Delilmiistersin? Enzayıf, enaptalhayvan, eniyibeslenir. (Meyvekurtlarıvebalıklargibi. ) Hemenâciz, ennâzikmahlûk, eniyirızkıoyer. (Çocuklarveyavrulargibi.)

Evet, vâsıta‑i rızk-ı helâl, iktidarveihtiyarileolmadığını; belki, aczvezaafileolduğunuanlamakiçinbalıklariletilkileri, yavrularilecanavarları, ağaçlarilehayvanlarımuvâzene etmekkâfîdir.

51

Demek, derd‑i maîşetiçinnamazınıterk eden, oneferebenzerki; tâlimivesiperinibırakıpçarşıdadilencilik eder. Fakat, namazınıkıldıktansonraCenâb‑ı Rezzâk-ı Kerîm’inmatbaha‑i rahmetindentâyinâtınıaramak, başkalarabâr olmamakiçinkendisibizzatgitmekgüzeldir, mertliktir; odahibiribâdettir. Hem, insanibâdetiçinhalk olunduğunu, fıtratıvecihâzât‑ı maneviyesigösteriyor. Zîra, hayat‑ı dünyeviyesinelâzımolanamelveiktidarcihetinde, enednâbirserçekuşunayetişmez. Fakat, hayat‑ı maneviye ve uhreviyesinelâzımolanilimveiftikâriletazarruveibâdetcihetindehayvanatınsultanıvekumandanıhükmündedir.

Demekeynefsim! Eğerhayat‑ı dünyeviyeyigaye-i maksatyapsanveonadâimçalışsan, enednâbirserçekuşununbirneferihükmünde olursun. Eğerhayat‑ı uhreviyeyigaye-i maksatyapsanveşuhayatıdahionavesilevemezraa etsenveonagöreçalışsan, ovakithayvanatınbüyükbirkumandanıhükmündeveşudünyadaCenâb‑ı Hakk’ınnâzlıveniyâzdârbirabdi, mükerremvemuhterembirmisâfiriolursun.

İştesanaikiyol. İstediğiniintihap edebilirsin. HidayetvetevfikiErhamürrâhimîn’deniste…

52

# AltıncıSöz

﷽

اِنَّ اللّٰهَ اشْتَرٰى مِنَ الْمُؤْمِن۪ينَ اَنْفُسَهُمْ وَاَمْوَالَهُمْ بِاَنَّ لَهُمُ الْجَنَّةَ

NefisvemalınıCenâb‑ı Hakk’asatmakveO’naabdolmakveaskerolmak; nekadarkârlıbirticâret, nekadarşereflibirrütbeolduğunuanlamakistersen, şutemsîlîhikâyeciğidinle:

Birzamanbirpâdişah, raiyetindenikiadama, her birisineemânetenbirerçiftlikverirki; içindefabrika, makine, at, silâhgibiher şeyvar. Fakatfırtınalıbirmuhârebezamanıolduğundan, hiçbirşeykararındakalmaz. Yamahvolurveyatebeddül edergider. Pâdişah, oikineferekemâl‑i merhametindenbiryâver‑i ekreminigönderdi. Gayetmerhametkârbirfermânileonlaradiyordu:

“Elinizdeolanemânetimibanasatınız. Tâsiziniçinmuhâfazaedeyim. Beyhûdezâyî olmasın. Hem, muhârebebittiktensonra, sizedahagüzelbirsûretteiâde edeceğim. Hem, güyâoemânetmalınızdır, pekbüyükbirfiatsizevereceğim. Hem, omakinevefabrikadakiâletler, benimnâmımlavebenimtezgâhımdaişlettirilecek. Hemfiyatı, hemücretleribirdenbineyükselecek. Bütünokârısizevereceğim. Hemdesizâcizvefakirsiniz. Okocaişlerinmasârifâtınıtedârik edemezsiniz. Bütünmasârifâtıvelevâzımatıbenderuhte ederim. Bütünvâridâtıvemenfaatisizevereceğim. Hemdeterhisâtzamanınakadarelinizdebırakacağım. İştebeşmertebekâriçindekâr!‥

Eğerbanasatmazsanız, zâtengörüyorsunuzki, hiçkimseelindekinimuhâfaza edemiyor. Herkesgibielinizdençıkacak. Hembeyhûdegidecek, hemoyüksekfiattanmahrum kalacaksınız. Hemonâzik, kıymettarâletler, mîzanlar; istîmâl edilecekşâhânemâdenlerveişlerbulmadığından, bütünbütünkıymetten düşecekler. Hemidarevemuhâfazazahmetivekülfetibaşınızakalacak. Hem, emânettehıyânetcezasınıgöreceksiniz. İştebeşderecehasâretiçindehasâret!‥

53

Hemdebanasatmakise, banaaskerolupbenimnâmımlatasarruf etmekdemektir. Âdibiresirvebaşıbozuğabedel, àlîbirpâdişahınhâs, serbestbiryâver‑i askeriolursunuz.”

Onlar, şuiltifatıvefermânıdinlediktensonra, oikiadamdanaklıbaşındaolanıdedi:

“Başüstüne, benmaaliftihârsatarım. Hembinteşekkür ederim.”

Diğerimağrûr, nefsifiravunlaşmış, hodbîn, ayyaş, güyâebedîoçiftliktekalacakgibi, dünyanınzelzelelerindenvedağdağalarındanhaberiyok. Dedi:

“Yok, yok!‥ Pâdişahkimdir? Benmülkümüsatmam, keyfimibozmam!‥”

Birazzamansonrabirinciadam, öylebirmertebeyeçıktıki, herkeshâlinegıpta ederdi. Pâdişahınlütfunamazhar olmuş, hâssarayındasaâdetleyaşıyor. Diğeri, öylebirhâlegiriftâr olmuşki; herkesonaacıyor, hem“Müstehak!” diyor. Çünkü; hatâsınınneticesiolarak, hemsaâdetivemülkügitmiş, hemcezaveazap çekiyor.

İşteeynefs‑i pür-heves! Şumisâlindürbünüilehakikatinyüzünebak. AmmaOPâdişahise; ezel ebed SultanıolanRabbin, Hàlık’ındır. Veoçiftlikler, makineler, âletler, mîzanlarise; senindâire‑i hayatıniçindekimâmelekinveomâmelekiniçindekicisim, rûhvekalbinveonlariçindekigözvedil, akılvehayâlgibizâhirîvebâtınîhâsselerindir. VeOYâver‑i Ekremise, Resûl‑i Kerîm’dir. Veofermân‑ı ahkemise, Kur'ân‑ı Hakîm’dirki; bahsindebulunduğumuzticâret‑i azîmeyi, şuâyetleilân ediyor:اِنَّ اللّٰهَ اشْتَرٰى مِنَ الْمُؤْمِن۪ينَ اَنْفُسَهُمْ وَاَمْوَالَهُمْ بِاَنَّ لَهُمُ الْجَنَّةَ

54

Veodalgalımuhârebemeydânıise, şufırtınalıdünyayüzüdürki; durmuyor, dönüyor, bozuluyorveherinsanınaklınaşufikriveriyor: “Mâdemher şeyelimizdençıkacak, fânîolupkaybolacak; acababâkîyetebdil edipibkâ etmekçaresiyokmu?” deyipdüşünürkenbirdensemâvîsadâ‑yı Kur'ânişitiliyor. Der: “Evet, var. Hembeşmertebekârlıbirsûrette, güzelverahatbirçaresivar.”

Suâl:Nedir?

Elcevap:Emânetisâhib‑i hakîkisinesatmak.

İşteosatışta, beşderecekâriçindekârvar.

Birinci Kâr:Fânîmalbekâ bulur. Çünkü: Kayyûm‑u BâkîolanZât‑ı Zülcelâl’everilenveO’nunyolundasarfedilenşuömr‑ü zâil, bâkîyeinkılâp eder. Bâkîmeyveler verir. Ovakitömürdakikaları; âdetatohumlar, çekirdeklerhükmündezâhirenfenâ bulur, çürür. Fakat, Âlem-i Bekâdasaâdetçiçekleriaçarlarvesünbüllenirler. VeÂlem‑i Berzah’taziyâdâr, mûnisbirermanzaraolurlar.

İkinci Kâr:Cennetgibibirfiatveriliyor.

Üçüncü Kâr:Herâzâvehâsselerinkıymeti, birdenbineçıkar.

55

Meselâ: Akılbirâlettir. EğerCenâb‑ı Hakk’asatmayıpbelkinefishesabınaçalıştırsan; öylemeş'ûmvemüz'icvemuaccizbirâlet olurki, geçmişzamanınâlâm‑ı hazînânesinivegelecekzamanınehvâl‑i muhavvifânesiniseninbubîçârebaşınayükletecekyümünsüzvemuzırbirâletderekesineiner. İştebununiçindirki; fâsıkadam, aklıniz'açvetâcizindenkurtulmakiçin, gâlibenyasarhoşluğaveyaeğlenceyekaçar. EğerMâlik‑i Hakîki’sinesatılsaveO’nunhesabınaçalıştırsan; akılöyletılsımlıbiranahtarolurki, şukâinâttaolannihâyetsizRahmethazineleriniveHikmetdefineleriniaçar. Vebununlasâhibini, saâdet‑i ebediyeyemüheyyâ edenbirmürşid‑i Rabbânîderecesineçıkar.

Meselâ: Göz, birhâssedirki, rûhbuâlemiopencereileseyreder. EğerCenâb‑ı Hakk’asatmayıpbelkinefishesabınaçalıştırsan; geçici, devamsızbazıgüzellikleri, manzaralarıseyrile, şehvetveheves‑i nefsâniyeyebirkavvâdderekesindebirhizmetkârolur. Eğergözü, gözünSâni'‑i Basîr’inesatsanveO’nunhesabınaveiznidâiresindeçalıştırsan; ozamanşugöz, şukitab‑ı kebîr-i kâinâtınbirmütâlaacısıveşuâlemdekimûcizât-ı sanat-ı Rabbâniye’ninbirseyircisiveşuküre‑i arzbahçesindekirahmetçiçeklerininmübârekbirarısıderecesineçıkar.

Meselâ: Dildekikuvve‑i zâikayı, Fâtır‑ı Hakîm’inesatmazsan, belkinefishesabına, midenâmınaçalıştırsan; ovakit, midenintavlasınavefabrikasınabirkapıcıderekesineiner, sukùt eder. EğerRezzâk‑ı Kerîm’esatsan; ozamandildekikuvve‑i zâika, Rahmet‑i İlâhiyehazinelerininbirnâzır‑ı mâhirivekudret‑i Samedâniye matbahlarınınbirmüfettiş‑i şâkirirütbesineçıkar.

İşteeyakıl! Dikkat et! Meş'ûmbirâletnerede, kâinâtanahtarınerede? Eygöz! Güzelbak! Âdibirkavvâdnerede, kütübhâne‑i İlâhî’ninmütefenninbirnâzırınerede? Veeydil! İyitat! Birtavlakapıcısıvebirfabrikayasakçısınerede, hazine‑i hàssa-i Rahmet nâzırınerede?‥

Vedahabunlargibibaşkaâletleriveâzâlarıkıyâs etsenanlarsınki; hakikatenmü'minCennet’elâyıkvekâfirCehennem’emuvâfıkbirmâhiyetkesbeder. Veonlarınher biriöylebirkıymetalmalarınınsebebi; mü'min, îmânıylaHàlık’ınınemânetini, O’nunnâmınaveiznidâiresindeistîmâl etmesidir. Vekâfir, hıyânet edipnefs‑i emmârehesabınaçalıştırmasıdır.

Dördüncü Kâr:İnsanzayıftır; belâlarıçok‥ fakirdir; ihtiyacıpekziyâde‥ âcizdir; hayatyüküpekağır… EğerKadîr‑i Zülcelâl’edayanıptevekkül etmezseveîtimat edipteslîm olmazsa, vicdânıdâimazapiçindekalır. Semeresizmeşakkatler, elemler, teessüfleronuboğar. Yasarhoşyacanavar eder.

56

Beşinci Kâr:Bütünoâzâveâletlerinibâdetivetesbihâtıveoyüksekücretleri, enmuhtaçolduğunbirzamanda, Cennetyemişlerisûretindesanaverileceğine, ehl‑i zevk ve keşfveehl-i ihtisâs ve müşâhedeittifak etmişler.

İştebubeşmertebekârlıticâretiyapmazsan, şukârlardanmahrumiyettenbaşka, beşderecehasâretiçindehasâretedüşeceksin.

Birinci Hasâret:Okadarsevdiğinmalveevlat; veperestiş ettiğinnefisvehevâ; vemeftûn olduğungençlikvehayatzâyî olupkaybolacak. Seninelindençıkacaklar. Fakat, günahlarını, elemlerinisanabırakıpboynunayükletecekler.

İkinci Hasâret:Emânettehıyânetcezasınıçekeceksin. Çünkü; enkıymettarâletleri, enkıymetsizşeylerdesarfedipnefsinezulmettin.

Üçüncü Hasâret:Bütünokıymettarcihâzât‑ı insaniyeyihayvanlıktançokaşağıbirderekeyedüşürüp, Hikmet‑i İlâhiye’yeiftiravezulmettin.

Dördüncü Hasâret:Aczvefakrınileberaber, opekağırhayatyükünü, zayıfbelineyükleyipzevâlvefirâksillesialtındadâimvâveylâ edeceksin.

Beşinci Hasâret:Hayat‑ı ebediyeyesâsâtınıvesaâdet‑i uhreviyelevâzımatınıtedârik etmekiçinverilenakıl, kalp, göz, dilgibigüzelhediye‑i Rahmâniye’yiCehennemkapılarınısanaaçacakçirkinbirsûreteçevirmektir.

Şimdisatmağabakacağız… Acabaokadarağırbirşeymidirki, çoklarısatmaktankaçıyorlar. Yok!‥ Kat'aveasla! Hiçöyleağırlığıyoktur. Zîrahelâldâiresigeniştir, keyfekâfî gelir. Haramagirmeyehiçlüzumyoktur. Ferâiz‑i İlâhiyeisehafiftir, azdır. Allah’aabdveaskerolmak, öylelezzetlibirşereftirkitârif edilmez. Vazifeise; yalnızbiraskergibiAllahnâmınaişlemeli, başlamalı‥ veAllahhesabıylavermelivealmalı‥ veiznivekanunudâiresindehareket etmeli, sükûnet bulmalı‥ Kusur etseistiğfar etmeli: “Yâ Rab! Kusurumuzuaffet. Bizi, kendinekulkabûl et. Emânetinikabzetmekzamanınakadar, biziemânetteemîn kıl. Âmîn!‥”demeliveO’nayalvarmalı…

57"""

# Find "AltıncıSöz" and extract from there to the end
idx_raw = raw_markdown.find("# AltıncıSöz")
idx_next = raw_markdown.find("# YedinciSöz")

if idx_raw >= 0 and idx_next >= 0:
    # Extract just the Altıncı Söz section
    altinci_text = raw_markdown[idx_raw:idx_next].strip()
    # Remove the heading
    lines = altinci_text.split('\n', 2)
    if len(lines) >= 3:
        content = lines[2].strip()
    else:
        content = altinci_text

    # The markdown from firecrawl has words concatenated (no spaces between them)
    # This is because the site renders with special formatting
    # Let me check what this looks like and just output it
    print(content)
else:
    print(f"AltıncıSöz at {idx_raw}, YedinciSöz at {idx_next}")
    sys.exit(1)
