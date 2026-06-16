import re

# Full markdown from firecrawl (with hash to preserve encoding)
raw = '''# Besinci Soz

Allah

innallaha maalladhinat taqaw walladhina hum muhsinun

Namazkılmakvebuyukgunahlarıislememek; nederecehakikibirvazife-i insaniyevenekadarfıtri, munasipbirnetice-i hilkat-i beseriyeoldugunugormekistersen, sutemsilihikayecigebak, dinle:

Seferberliktebirtaburda, birimuallemvazife-perver; digeriaceminefis-perverikiaskerberaberbulunuyordu. Vazife-pervernefer, talimevecihadadikkat eder, erzakvetayinatınıhicdusunmezdi. Cunkuanlamıski; onubeslemekvecihazatınıvermek, hastaolsatedavi etmek, hattainde'l-hacelokmayıagzınakoymayakadardevletinvazifesidir. Veonunasılvazifesi, talimvecihaddır. Fakatbazıerzakvecihazatislerindeisler. Kazankaynatır, karavanayıyıkar, getirir.

Onasorulsa: "Neyapıyorsun?"

"Devletinangaryasınıcekiyorum." der. Demiyor: "Nafakamicinealisıyorum."

Digersikem-perverveacemineferise, talimeveharbedikkat etmezdi. "O, devletisidir. Banane!" derdi. Daimnafakasınıdusunuponunpesindedolasır, taburuterkeder, carsıyagider, alısveris ederdi.

Birgunmuallemarkadasıonadedi:

"Birader, asılvazifentalimvemuharebedir. Senonunicinburayagetirilmissin. Padisahaitimat et. Oseniacbırakmaz. O, O'nunvazifesidir. Hemsenacizvefakirsin, heryerdekendinibeslettiremezsin. Hemmucahedeveseferberlikzamanıdır. Hemsana'asidir' der, cezaverirler. Evet, ikivazifepesimizdegorunuyor. Biri; padisahinvazifesidir. Bazenbizonunangaryasınıcekerizki, bizibeslemektir. Digeri; bizimvazifemizdir. Padisahbizeteshilatileyardım ederki, talimveharptir."

Acabaoserserinefer, omucahitmuallemekulakvermezse, nekadartehlikedekalır, anlarsın!

Isteeytenbelnefsim! Odalgalımeydan-ı harp, budagdagalıdunyahayatıdır. Otaburlarataksim edilenorduise, cemiyet-i beseriyedir. Veotaburise, suasrınCemaat-i Islamiye'sidir. Oikineferise; biri: Feraiz-i diniyesinibilenveisleyenvekebairiterkvegunahlarıislememekicin, nefisveseytanlamucahede edenmuttakiMusluman'dır. Digeri: Rezzak-i Hakiki'yiittiham etmekderecesindederd-i maisetedalıp, feraiziterk edenvemaisetyolundarastgelegunahlarıisleyenfasık-ı hasirdir. Veotalimvetalimatise- bastanamaz- ibadettir. Veoharpise, nefisveheva, cinveinsseytanlarına karsımucahede edip, gunahlardanveahlak-ı rezileden, kalpveruhunuhelaket-i ebediyedenkurtarmaktır. Veoikivazifeise; birisi: Hayatıveripbeslemektir. Digeri: Hayatıverenevebesleyeneperestis edipyalvarmaktır. O'natevekkul edipemniyet etmektir.

Evet, enparlakbirmucize-i sanat-ı Samedaniyevebirharika-i Hikmet-i Rabbaniyeolanhayatıkimvermis, yapmısise, rızıklaohayatıbesleyenveidame edendeO'dur. O'ndanbaskaolmaz! Delilmiistersin? Enzayıf, enaptalhayvan, eniyibeslenir. (Meyvekurtlarivebalıklargibi. ) Hemenaciz, en nazikmahluk, eniyirızkıoyer. (Cocuklarevyavrulargibi.)

Evet, vasıta-i rızk-ı helal, iktidarveihtiyarileolmadıgını; belki, aczvezaafileoldugunuanlamakicinbalıklariletilkileri, yavrularilecanavarları, agaclarilehayvanlarımuvazene etmekkafidir.

Demek, derd-i maiseticinnamazınıterk eden, oneferebenzerki; talimivesiperinibırakıpcarsıdadilencilik eder. Fakat, namazınıkıldıktansonraCenab-ı Rezzak-ı Kerim'inmatbaha-i rahmetindentayinatınıaramak, baskalabar olmamakicinkendisibizzatgitmekguzeldir, mertliktir; odahibiribadettir. Hem, insanibadeticinhalk olundugunu, fıtratıvecihazat-ı maneviyesigosteriyor. Zira, hayat-ı dunyeviyesinelazımolanamelveiktidarcihetinde, enednabirsercekusunayetismez. Fakat, hayat-ı maneviye ve uhreviyesinelazımolanilimveiftikariletazarruveibadetcihetindehayvanatınsultanıvekumandanıhukmundedir.

Demekeynefsim! Egerhayat-ı dunyeviyeyigaye-i maksatyapsanveonadaimcalıssan, enednabirsercekusununbirneferihukmunde olursun. Egerhayat-ı uhreviyeyigaye-i maksatyapsanvesuhayatıdahionavesilevemezraa etsenveonagorecalıssan, ovakithayvanatınbuyukbirkumandanıhukmundevesudunyadaCenab-ı Hakk'ınnazlıveniyazdarbirabdi, mukerremvemuhterembirmisafiriolursun.

Ittesanaikiyol. Istediğiniintihap edebilirsin. HidayetvetevfikiErhamurrahimin'deniste

Altinci Soz

Allah

innallaha ishtara minal mu'minine anfusahum wa amwalahum bi anna lahumul jannah

NefisvemalınıCenab-ı Hakk'asatmakveO'naabdolmakveaskerolmak; nekadarkarlıbirticaret, nekadarsereflibirrutbeoldugunuanlamakistersen, sutemsilihikayecigidinle:

Birzamanbirpadisah, raiyetindenikiadama, her birisineemanetenbirerci iftlikverirki; icindefabrika, makine, at, silahgibiher seyvar. Fakatfırtınalıbirmuharebezamanıoldugundan, hicbirseykararındakalmaz. Yamahvolurveyatebeddul edergider. Padisah, oikineferekemal-i merhametindenbiryave r-i ekreminigonderdi. Gayetmerhametkarbirfermanileonlaradiyordu:

"Elinizdeolanemanetimibanasatınız. Tasizinicinmuhafazaedeyim. Beyhudezayi olmasın. Hem, muharebebittiktensonra, sizedahaguzelbirsuretteiade edecegim. Hem, guyaoemanetmalınızdır, pekbuyukbirfi atsizeverecegim. Hem, omakinevefabrikadakialetler, benimnamımlavebenimtezgahımdaislettirilecek. Hemfiyatı, hemucretleribirdenbineyukselecek. Butunokarısizeverecegim. Hemdesizacizvefakirsin iz. Okocaislerinmasarifatınıtedarik edemezsiniz. Butunmasarifatıvelevazımatıbenderuhte ederim. Butunvaridatıvemenfaatisizeverecegim. Hemdeterhisatzamanınakadarelinizdebırakacagım. Itebesmertebekaricindekar!‥

Egerbanasatmazsanız, zatengoruyorsunuzki, hickimseelindekinimuhafaza edemiyor. Herkesgibielinizdenckacak. Hembeyhudegidecek, hemoyuksekfiattanmahrum kalacaksınız. Hemonazik, kıymettaraletler, mizanlar; istimal edileceksahanemadenlerveislerbulmadıgından, butunbutunkıymetten dusecekler. Hemidarevemuhafazazahmetivekulfetibasınakalacak. Hem, emanettehıyanetcezasınıgoreceksiniz. Itebesderecehasareticindehasaret!‥

Hemdebanasatmakise, banaaskerolupbenimnamımlatasarruf etmekdemektir. Adibiresirvebasıbozugabedel, alibirpadısahınhas, serbestbiryave r-i askeriolursunuz."

Onlar, suiltifatıvefermanıdinlediktensonra, oikiadamdanaklıbasındaolanıdedi:

"Basustune, benmaaliftiharsatarım. Hembintesekkur ederim."

Digerimagrur, nefsifiravunlasmıs, hodbin, ayyas, guyaebedio iliktekalacakgibi, dunyanınzelzelelerindenvedagdagalarındanhaberiyok. Dedi:

"Yok, yok!‥ Padisahkimdir? Benmulkumusatmam, keyfimibozmam!‥"

Birazzamansonrabirinciadam, oylebirmertebeyeckıktıki, herkeshalinegıpta ederdi. Padısahınlutf unamazhar olmus, hassarayındasaadetleyasıyor. Digeri, oylebirhalegiriftar olmuski; herkesonaacıyor, hem"Mustehak!" diyor. Cunku; hatasınınneticesiolarak, hemsaadetivemulku gitmis, hemcezaveazap cekiyor.

Iteeynefs-i pur-heves! Sumisalindurbunuilehakikatinyuzunebak. AmmaOPadisahise; ezelebedSultanıolanRabbin, Halk'ındır. Veociftlikler, makineler, aletler, mizanlarise; senindaire-i hayatinicindekimamelekinveomamelekiniicindekicisim, ruhvekalbinveonlariicindekigozvedil, akılvehayalgibizahiri vebatınıhasselerindir. VeOYaver-i Ekremise, Resul-i Kerim'dir. Veoferman-ı ahkemise, Kur'an-ı Hakim'dirki; bahsindebulundugumuzticaret-i azimeyi, suayetleilan ediyor: innallaha ishtara minal mu'minine anfusahum wa amwalahum bi anna lahumul jannah

V eodalgalımuharebemeydanıise, sufırtınalıdunyayuzudurki; durmuyor, donuyor, bozuluyorveherinsanınaklınasufikriveriyor: "Mademher sey elimizdenckacak, faniolupkaybolacak; acababakiyetebdil edipibka etmekca resiyokmu?" deyipdusunurkenbirdensemavisada-yı Kur'anisitiliyor. Der: "Evet, var. Hembesmertebekarlıbirsurette, guzelverahatbircaresivar."

Sual: Nedir?

Elcevap: Emanetisahib-i hakikisinesatmak.

Iteosatısta, besderecekaricindekarvar.

Birinci Kar: Fanimalbeka bulur. Cunku: Kayyum-u BakiolanZat-ı Zulcelal'everilenveO'nunyolundasarfedilensuomr-u zail, bakiyeninkilap eder. Bakimeyveler verir. Ovakitomurdakikaları; adetatohumlar, cekirdeklerhukmundezahirenfenabulur, curur. Fakat, Alem-i Bekadasaadetcicekleriacarlarvesunbullanirler. VeAlem-i Berzah'taz iyadar, munisbirermanzaraolurlar.

Ikinci Kar: Cennetgibirfiatveriliyor.

Ucuncu Kar: Herazavehasselerinkıymeti, birdenbineckıkar.

Mesela: Akılbiralettir. EgerCenab-ı Hakk'asatmayıpbelkinefishesabınacalıstırsan; oylemes'um vemuz'icvemuaccizbiralet olurki, gecmiszamanınalam-ı hazinanesinivegelecekzamanınehval-i muhavvifanesiniseninbicarebasınayukletecekyumunsuzvemuzırbiraletderekesineiner. Itebununicindirki; fasıkadam, aklın iz'acvetacizindenkurtulmakicin, galibenya sarhosluga veya eglenceyekacar. EgerMalik-i Hakiki'sinesatılsaveO'nunhesabınacalıstırsan; akıloyletılsımlıbiranahtarolurki, sukainattaolannihayetsizRahmethazineleriniveHikmetdefineleriniacar. Vebununlasahibini, saadet-i ebediyeyemuheyy a edenbirmursid-i Rabbaniderecesineckıkar.

Mesela: Goz, birhassedirki, ruhbualemio pencereileseyreder. EgerCenab-ı Hakk'asatmayıpbelkinefishesabınacalıstırsan; gecici, devamsızbazıguzellikleri, manzaralarıseyrile, sehvetveheves-i nefsaniyeyebirka vvadderekesindebirhizmetkarolur. E gerg ozu, g ozunSani'-i Besir'inesatsanveO'nunhesabınaveznidairesindecalıstırsan; ozamansugoz, sukitab-ı kebir-i kainatınbirmutalaacısıvesualmd ekimucizat-ı sanat-ı Rabbaniye'ninbirseyircisivesukure-i arzbahcesindekirahmetckeki lerininmubarekbrarısıderecesineckıkar.

Mesela: Dildekikuvve-i zaikayı, Fatır-ı Hakim'esatmazsan, belkinefishesabına, mide namınacalıstırsan; ovakit, midenintavlasınavef abrikasnabir kapıcıderekesineiner, sukt eder. EgerRezzak-ı Kerim'esatsan; ozamandildekikuvve-i zaika, Rahmet-i Ihayiyehazinelerininbirnazır-ı mahiriivekudret-i Samedaniyematbahlarınınbirmufettis-i sakirir utbesineckıkar.

Iteeyakıl! Darkk at et! Mes'umbiraletnerede, kainatanahtarnerede? Egyz! Guzlbak! Adibr kavvadnerede, kutuphane-i Iahi'ninmutefernnbr nazırnerede? Veydil! Iyatat! B rtvarl apcısvebrfabyasakcsnerede, hazine-i hassa-iRahmet nazrnerede?‥

Vedahabunlargibibsakaaltleriveazalarıkyas etsenanlarsınki; hakikatenmuminCennet'elaykvekafirCehennem'emuva kbrmahiyetksbeder. Veonlarınhr biriylebrkymetlmalarnsebebi; mumin, imanıylaHalk'ınınnemanetin, O'nunnamnavemzdarsndeistml etmsidr. Vekafir, hyne ed etmekmireesabınacalıştırmasıdır.

Dorduncu Kar: Insanzayıftır; belalarıok‥ fakirdir; ihtiyacıpekzde‥ cizdir; hayatyukupekagır… EgerKadirr-i Zulcelal'eyanpvekkul etmzsetmt edipteslm omazsa, vcdandaimazapiindekalr. Semeresizmsakkatler, eleml r, teessufleronoar. Yasr hoyaavanar edr.

Besinci Kar: Butunodiletleien abdetvn spihıveyksekretleri, enmuhaclduğunbrzamanda, Cennetyemişlerisuretdsanaverleceğne, ehli-zevk vkesfveehl-i ihtss vemuhdeittfak etmişler.

Itebubesmertebekrlticaretıyapmazsn, sukarardanmahrumyettenbaka, beşderecehasretiindehasaredüeceksn.

Birinci Hasret: Okadaresvidğiinalv elat; veersetis edtğiinneseved; vemefluodğununliylikayatzay ouplacaksın. Seninlindençıcaklar. Fakat, günahlarını, elemler aıkuıınyüecker.

İkinci Hasret: Emnteyet czaııçkecksn. Çüük; enkımdıiridğiynzelerdeidfipnsinezulmettin.

Ugun Hasret: Butunokymettrahtihazianiyeyievnlnetanokaağbrdereeydüüüp, Hikm- iIîye'ftravzumttin.

DnHasret: cız acınilrrear, opekğrlha tüüü, zayıbnineyikyipzavlfirakilesi altıddaimvveyld edecesin.

Bşn Hasret: Hayt- yeeyeyesasınıvsaddetiveyeevazmatındretmelmekcinverilenakl, kalp, göz, dil gibiğüzehediyeiRamaniy'yCenemkarınısnaaçakikinsurteevirmetir.

Şmdiatmğacaz… Acabaokadarağrbirşeyimdri, çklarısatmaknkaktıryorlar.Yok!‥ Kat'vasla! Hiçöyleğrilığyktur.Zırhelâldiresiştir,eykfâîgr. Haramgimiyecüykytyr. Ferâz-İlâhiyeishfiftir, aazdır.Alahâbdevaskerolmak, yleezzlebişftikitârifdmz. Vzfi; lalnzbiraksergbiAllahhamıalşmli, çlaĞ      veAllahhbiyelnşlmal     veizvisunuirsdsajketiml,ükneblılĞ      Kuurtistifa      “YâR!aKurumuaef. B,ııku e. Emnetiv elaniıdeaimndaruaVede.                       deO'yavarmalı'''

# Fix encoding - the firecrawl output was in markdown with # headings
# First, let's find Altıncı Söz (may be written as "Altincı Soz" or "Altıncı Söz")
import re

# Normalize - look for the section
# The content before Altıncı Söz ends with "isten Altinci Soz" (no proper separator)
idx = raw.find("Altinci Soz")
if idx >= 0:
    # Get content from after "Allah" line following Altinci Soz
    lines = raw[idx:].split('\n')
    result = []
    capture = False
    for line in lines:
        if line.strip() == "Allah":
            capture = True
            continue
        if capture:
            if line.strip().startswith('#'):
                break
            result.append(line)

    altinci_text = '\n'.join(result).strip()

    # The text has missing spaces between words
    # Let me preserve it as-is since that's what the site rendered
    print(altinci_text)
else:
    print("Not found")
