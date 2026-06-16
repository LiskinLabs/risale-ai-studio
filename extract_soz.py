import re

text = r"""# Besinci Soz

Allah

innallaha maalladhinat taqaw walladhina hum muhsinun

Namaz kılmak ve buyuk gunahları islememek; ne derece hakiki bir vazife-i insaniye ve ne kadar fıtri, munasip bir netice-i hilkat-i beseriye oldugunu gormek istersen, su temsili hikayecige bak, dinle:

Seferberlikte bir taburda, biri muallem vazife-perver; digeri acemi nefis-perver iki asker beraber bulunuyordu. Vazife-perver nefer, talime ve cihada dikkat eder, erzak ve tayinatını hic dusunmezdi. Cunku anlamıs ki; onu beslemek ve cihazatını vermek, hasta olsa tedavi etmek, hatta inde'l-hace lokmayı agzına koymaya kadar devletin vazifesidir. Ve onun asıl vazifesi, talim ve cihaddır. Fakat bazı erzak ve cihazat islerinde isler. Kazan kaynatır, karavanayı yıkar, getirir.

Ona sorulsa: Ne yapıyorsun?

Devletin angaryasını cekiyorum. der. Demiyor: Nafakam icin calısıyorum.

Diger s ikem-perver ve acemi nefer ise, talime ve harbe dikkat etmezdi. O, devlet isidir. Bana ne! derdi. Daim nafakasını dusunup onun pesinde dolasır, taburu terkeder, carsıya gider, alısveris ederdi.

Bir gun muallem arkadası ona dedi:

Birader, asıl vazifen talim ve muharebedir. Sen onun icin buraya getirilm issin. Padisaha itimat et. O seni ac bırakmaz. O, O'nun vazifesidir. Hem sen aciz ve fakirsin, her yerde kendini beslettiremezsin. Hem mucahede ve seferberlik zamanıdır. Hem sana asidir der, ceza verirler. Evet, iki vazife pesimizde gorunuyor. Biri; padisahın vazifesidir. Bazen biz onun angaryasını cekeriz ki, bizi beslemektir. Digeri; bizim vazifemizdir. Padisah bize teshilat ile yardım eder ki, talim ve harptir.

Acaba o serseri nefer, o mucahit mualleme kulak vermezse, ne kadar tehlikede kalır, anlarsın!

Iste ey tenbel nefsim! O dalgalı meydan-ı harp, bu dagdagalı dunya hayatıdır. O taburlara taksim edilen ordu ise, cemiyet-i beseriyedir. Ve o tabur ise, su asrın Cemaat-i Islamiye'sidir. O iki nefer ise; biri: Feraiz-i diniyesini bilen ve isleyen vekebairi terk ve gunahları islememek icin, nefis ve seytanla mucahede eden muttaki Musluman'dır. Digeri: Rezzak-i Hakiki'yi ittiham etmek derecesinde derd-i maisete dalıp, feraizi terk eden ve maiset yolunda rastgele gunahları isleyen fasık-ı hasirdir. Ve o talim ve talimat ise – basta namaz – ibadettir. Ve o harp ise, nefis ve heva, cin ve ins seytanlarına karsı mucahede edip, gunahlardan ve ahlak-ı rezileden, kalp ve ruhunu helaket-i ebediyeden kurtarmaktır. Ve o iki vazife ise; birisi: Hayatı verip beslemektir. Digeri: Hayatı verene ve besleyene perestis edip yalvarmaktır. O'na tevekkul edip emniyet etmektir.

Evet, en parlak bir mucize-i sanat-ı Samedaniye ve bir harika-i Hikmet-i Rabbaniye olan hayatı kim vermis, yapmıs ise, rızıkla o hayatı besleyen ve idame eden de O'dur. O'ndan baska olmaz! Delil mi istersin? En zayıf, en aptal hayvan, en iyi beslenir. (Meyve kurtları ve balıklar gibi. ) Hem en aciz, en nazik mahluk, en iyi rızkı o yer. (Cocuklar ve yavrular gibi.)

Evet, vasıta-i rızk-ı helal, iktidar ve ihtiyar ile olmadıgını; belki, acz ve zaaf ile oldugunu anlamak icin balıklar ile tilkileri, yavrular ile canavarları, agaclar ile hayvanları muvazene etmek kafidir.

Demek, derd-i maiset icin namazını terk eden, o nefere benzer ki; talimi ve siperini bırakıp carsıda dilencilik eder. Fakat, namazını kıldıktan sonra Cenab-ı Rezzak-ı Kerim'in matbaha-i rahmetinden tayinatını aramak, baskalara bar olmamak icin kendisi bizzat gitmek guzeldir, mertliktir; o dahi bir ibadettir. Hem, insan ibadet icin halk olundugunu, fıtratı ve cihazat-ı maneviyesi gosteriyor. Zira, hayat-ı dunyeviyesine lazım olan amel ve iktidar cihetinde, en edna bir serce kusuna yetismez. Fakat, hayat-ı maneviye ve uhreviyesine lazım olan ilim ve iftıkar ile tazarru ve ibadet cihetinde hayvanatın sultanı ve kumandanı hukmundedir.

Demek ey nefsim! Eger hayat-ı dunyeviyeyi gaye-i maksat yapsan ve ona daim calıssan, en edna bir serce kusunun bir neferi hukmunde olursun. Eger hayat-ı uhreviyeyi gaye-i maksat yapsan ve su hayatı dahi ona vesile ve mezraa etsen ve ona gore calıssan, o vakit hayvanatın buyuk bir kumandanı hukmunde ve su dunyada Cenab-ı Hakk'ın nazlı ve niyazdar bir abdi, mukerrem ve muhterem bir misafiri olursun.

Iste sana iki yol. Istedigini intihap edebilirsin. Hidayet ve tevfiki Erhamurrahimin'den iste

Altıncı Soz

Allah

innallaha ishtara minal mu'minine anfusahum wa amwalahum bi anna lahumul jannah

Nefis ve malını Cenab-ı Hakk'a satmak ve O'na abd olmak ve asker olmak; ne kadar karlı bir ticaret, ne kadar serefli bir rutbe oldugunu anlamak istersen, su temsili hikayecigi dinle:

Bir zaman bir padisah, raiyetinden iki adama, her birisine emaneten birer ciftlik verir ki; icinde fabrika, makine, at, silah gibi her sey var. Fakat fırtınalı bir muharebe zamanı oldugundan, hicbir sey kararında kalmaz. Ya mahvolur veya tebeddul eder gider. Padisah, o iki nefere kemal-i merhametinden bir yaver-i ekremini gonderdi. Gayet merhametkar bir ferman ile onlara diyordu:

Elinizde olan emanetimi bana satınız. Ta sizin icin muhafaza edeyim. Beyhude zayi olmasın. Hem, muharebe bittikten sonra, size daha guzel bir surette iade edecegim. Hem, guya o emanet malınızdır, pek buyuk bir fiat size verecegim. Hem, o makine ve fabrikadaki aletler, benim namımla ve benim tezgahımda islettirilecek. Hem fiyatı, hem ucretleri birden bine yukselecek. Butun o karı size verecegim. Hem de siz aciz ve fakirsiniz. O koca islerin masarifatını tedarik edemezsiniz. Butun masarifatı ve levazımatı ben deruhte ederim. Butun varidatı ve menfaati size verecegim. Hem de terhisat zamanına kadar elinizde bırakacagım. Iste bes mertebe kar icinde kar!

Eger bana satmazsanız, zaten goruyorsunuz ki, hic kimse elindekini muhafaza edemiyor. Herkes gibi elinizden cıkacak. Hem beyhude gidecek, hem o yuksek fiattan mahrum kalacaksınız. Hem o nazik, kıymettar aletler, mizanlar; istimal edilecek sahanemadenler ve isler bulmadıgından, butun butun kıymetten dusecekler. Hem idare ve muhafaza zahmeti ve kulfeti basınıza kalacak. Hem, emanette hıyanet cezasını goreceksiniz. Iste bes derece hasaret icinde hasaret!

Hem de bana satmak ise, bana asker olup benim namımla tasarruf etmek demektir. Adi bir esir ve basıbozuga bedel, ali bir padisahın has, serbest bir yaver-i askeri olursunuz.

Onlar, su iltifatı ve fermanı dinledikten sonra, o iki adamdan aklı basında olanı dedi:

Bas ustune, ben maaliftihar satarım. Hem bin tesekkur ederim.

Digeri magrur, nefsi firavunlasmıs, hodbin, ayyaş, guya ebedi o ciftlikte kalacak gibi, dunyanın zelzelelerinden ve dagdagalarından haberi yok. Dedi:

Yok, yok! Padisah kimdir? Ben mulkumu satmam, keyfimi bozmam!

Biraz zaman sonra birinci adam, oyle bir mertebeye cıktı ki, herkes haline gıpta ederdi. Padisahın lutfuna mazhar olmus, has sarayında saadetle yasıyor. Digeri, oyle bir hale giriftar olmus ki; herkes ona acıyor, hem Mustehak! diyor. Cunku; hatasının neticesi olarak, hem saadeti ve mulku gitmis, hem ceza ve azap cekiyor.

Iste ey nefs-i pur-heves! Su misalin durbunu ile hakikatin yuzune bak. Amma O Padisah ise; ezel ebed Sultanı olan Rabbin, Halık'ındır. Ve o ciftlikler, makineler, aletler, mizanlar ise; senin daire-i hayatın icindeki mamelekin ve o mamelekin icindeki cisim, ruh ve kalbin ve onlar icindeki goz ve dil, akıl ve hayal gibi zahiri ve batıni hasselerindir. Ve O Yaver-i Ekrem ise, Resul-i Kerim'dir. Ve o ferman-ı ahkem ise, Kur'an-ı Hakim'dir ki; bahsinde bulundugumuz ticaret-i azimeyi, su ayetle ilan ediyor: innallaha ishtara minal mu'minine anfusahum wa amwalahum bi anna lahumul jannah

Ve o dalgalı muharebe meydanı ise, su fırtınalı dunya yuzudur ki; durmuyor, donuyor, bozuluyor ve her insanın aklına su fikri veriyor: Madem her sey elimizden cıkacak, fani olup kaybolacak; acaba bakiye tebdil edip ibka etmek caresi yok mu? deyip dusunurken birden semavi sada-yı Kur'an isitiliyor. Der: Evet, var. Hem bes mertebe karlı bir surette, guzel ve rahat bir caresi var.

Sual: Nedir?

Elcevap: Emaneti sahib-i hakikisine satmak.

Iste o satısta, bes derece kar icinde kar var.

Birinci Kar: Fani mal beka bulur. Cunku: Kayyum-u Baki olan Zat-ı Zulcelal'e verilen ve O'nun yolunda sarfedilen su omr-u zail, bakiye inkilap eder. Baki meyveler verir. O vakit omur dakikaları; adeta tohumlar, cekirdekler hukmunde zahiren fena bulur, curur. Fakat, Alem-i Bekada saadet cicekleri acarlar ve sunbullanir ler. Ve Alem-i Berzah'ta ziyadar, munis birer manzara olurlar.

Ikinci Kar: Cennet gibi bir fiat veriliyor.

Ucuncu Kar: Her aza ve hasselerin kıymeti, birden bine cıkar.

Mesela: Akıl bir alettir. Eger Cenab-ı Hakk'a satmayıp belki nefis hesabına calıstırsan; oyle mes'um ve muz'ic ve muacciz bir alet olur ki, gecmis zamanın alam-ı hazinanesini ve gelecek zamanın ehval-i muhavvifanesini senin bu bica re basına yukletecek yumunsuz ve muzır bir alet derekesine iner. Iste bunun icindir ki; fasık adam, aklın iz'ac ve tacizinden kurtulmak icin, galiben ya sarhosluga veya eglenceye kacar. Eger Malik-i Hakiki'sine satılsa ve O'nun hesabına calıstırsan; akıl oyle tılsımlı bir anahtar olur ki, su kainatta olan nihayetsiz Rahmet hazinelerini ve Hikmet definelerini acar. Ve bununla sahibini, saadet-i ebediyeye muhayya eden bir mursid-i Rabbani derecesine cıkar.

Mesela: Goz, bir hassedir ki, ruh bu alemi o pencere ile seyreder. Eger Cenab-ı Hakk'a satmayıp belki nefis hesabına calıstırsan; gecici, devamsız bazı guzellikleri, manzaraları seyrile, sehvet ve heves-i nefsaniyeye bir kavvad derekesinde bir hizmetkar olur. Eger gozu, gozun Sani'-i Basir'ine satsan ve O'nun hesabına ve izni dairesinde calıstırsan; o zaman su goz, su kitab-ı kebir-i kainatın bir mutalaacısı ve su alemdeki mucizat-ı sanat-ı Rabbaniye'nin bir seyircisi ve su kure-i arz bahcesindeki rahmet ciceklerinin mubarek bir arısı derecesine cıkar.

Mesela: Dildeki kuvve-i zaikayı, Fatır-ı Hakim'e satmazsan, belki nefis hesabına, mide namına calıstırsan; o vakit, midenin tavlasına ve fabrikasına bir kapıcı derekesine iner, sukut eder. Eger Rezzak-ı Kerim'e satsan; o zaman dildeki kuvve-i zaika, Rahmet-i Ilahiye hazinelerinin bir nazır-ı mahiri ve kudret-i Samedaniye matbahlarının bir mufettis-i sakiri rutbesine cıkar.

Iste ey akıl! Dikkat et! Mes'um bir alet nerede, kainat anahtarı nerede? Ey goz! Guzel bak! Adi bir kavvad nerede, kutuphane-i Ilahi'nin mutefernin bir nazırı nerede? Ve ey dil! Iyi tat! Bir tarla kapıcısı ve bir fabrika yasakcısı nerede, hazine-i hassa-i Rahmet nazırı nerede?

Ve daha bunlar gibi baska aletleri ve azaları kıyas etsen anlarsın ki; hakikaten mumin Cennet'e layık ve kafir Cehennem'e muvafık bir mahiyet kesbeder. Ve onların her biri oyle bir kıymet almalarının sebebi; mumin, imanıyla Halık'ının emanetini, O'nun namına ve izni dairesinde istimal etmesidir. Ve kafir, hıyanet edip nefs-i emmare hesabına calıstırmasıdır.

Dorduncu Kar: Insan zayıftır; belaları cok fakirdir; ihtiyacı pek ziyade acizdir; hayat yuku pek agırEger Kadir-i Zulcelal'e dayanıp tevekkul etmezse ve itimat edip teslim olmazsa, vicdanı daim azap icinde kalır. Semeresiz meşakkatler, elemler, teessufler onu bogar. Ya sarhos ya canavar eder.

Besinci Kar: Butun o aza ve aletlerini ibadeti ve tesbihatı ve o yuksek ucretleri, en muhtac oldugun bir zamanda, Cennet yemisleri suretinde sana verilecegine, ehl-i zevk ve kesf ve ehl-i ihtisas ve musahede ittifak etmisler.

Iste bu bes mertebe karlı ticareti yapmazsan, su karlardan mahrumiyetten baska, bes derece hasaret icinde hasarete duseceksin.

Birinci Hasaret: O kadar sevdig in mal ve evlat; ve perestis ettigin nefis ve heva; ve meftun oldugun genclik ve hayat zayi olup kaybolacak. Senin elinden cıkacaklar. Fakat, gunahlarını, elemlerini sana bırakıp boynuna yukletecekler.

Ikinci Hasaret: Emanette hıyanet cezasını cekeceksin. Cunku; en kıymettar aletleri, en kıymetsiz seylerde sarfedip nefsine zulmettin.

Ucuncu Hasaret: Butun o kıymettar cihazat-ı insaniyeyi hayvanlıktan cok asagı bir derekeye dusurup, Hikmet-i Ilahiye'ye iftira ve zulmettin.

Dorduncu Hasaret: Acz ve fakrın ile beraber, o pek agır hayat yukunu, zayıf beline yukleyip zeval ve firak sillesi altında daim vaveyla edeceksin.

Besinci Hasaret: Hayat-ı ebediyeye esasatını ve saadet-i uhreviye levazımatını tedarik etmek icin verilen akıl, kalp, goz, dil gibi guzel hediye-i Rahmaniye'yi Cehennem kapılarını sana acacak cirkin bir surete cevirmektir.

Simdi satmaga bakacagızAcaba o kadar agır bir sey midir ki, cokları satmaktan kacıyorlar. Yok! Kat'a ve asla! Hic oyle agırlıgı yoktur. Zira helal dairesi genistir, keyfekafi gelir. Harama girmeye hic luzum yoktur. Feraiz-i Ilahiye ise hafiftir, azdır. Allah'a abd ve asker olmak, oyle lezzetli bir sereftir ki tarif edilmez. Vazife ise; yalnız bir asker gibi Allah namına islemeli, baslamalı ve Allah hesabıyla vermeli ve almalı ve izni ve kanunu dairesinde hareket etmeli, sukunet bulmalıKusur etse istigfar etmeli: Ya Rab! Kusurumuzu affet. Bizi, kendine kul kabul et. Emanetini kabzetmek zamanına kadar, bizi emanette emin kıl. Amin!demeli ve O'na yalvarmalı
"""

# Extract Altinci Soz - from the heading to Yedinci Soz
start_marker = "Altinci Soz"
# Find the section
idx_start = text.find(start_marker)
if idx_start >= 0:
    # Skip past the heading line
    after_header = text.find('\n\n', idx_start)
    if after_header < 0:
        after_header = idx_start + len(start_marker)

    # Find end - look for the next Soz or end
    remaining = text[after_header:]

    # Print everything from Altinci Soz onward
    print(text[idx_start:].strip())
else:
    print("Altinci Soz not found")
