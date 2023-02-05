# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image dom = "dom.png"
image pole = "pole.png"
image somsiad = "somsiad.png"
image somsiad_one = "somsiad close.png"
image somsiad_two = "somsiad very close.png"
image marchew = "marchew.png"
image anime_gurl = "anime gurl.png"
image chad = "chad.png"
image grzybek = "grzybek.png"
image krowa = "krowa.png"
image young = "young milczeq.png"
image ufo = "UFO.png"
image kosmita = "sweety.png"
image kosmici = "kosmici.png"
image krzak = "krzak.png"
image uwu = "uwu_theme.png"
image melon = "melon.png"
image musk = "musk.png"
image coin = "coin.png"
image las = "las.png"
image dogee = "doge.png"
image kamien_onee = "kamien one.png"
image kamien_twoo = "kamien two.png"
image kamien_threee = "kamien three.png"
image kamieniee = "kamienie.png"
image party = "party.png"
image yong_milq = "yong milq.png"
image shop = "shop.png"
image korzen = "korzen.png"
image breaker = "break.png"
image andrzej = "andrzej.png"


define narrator = Character("Narrator")
define somsiad = Character("Somsiad")
define melon = Character("Melon Mózk")
define mariolka = Character("Mariolka")
define anime = Character("Anime Gurl")
define krowa = Character("Muuucia")
define kosmita_one = Character("Kosmita 1")
define kosmita_two = Character("Kosmita 2")
define doge = Character("Dodż")
define kamien_one = Character("Kamień Kac")
define kamien_two = Character("Kamień Kub")
define kamien_three = Character("Kamień Dam")
define kamienie = Character("Kamienie")
define yong_milq = Character("Yong MilQ")
define chad = Character("???")
define andrzej = Character("Andrzej")




# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music ["audio/the-beat-of-root.mp3"] loop
    scene dom with dissolve


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    narrator "Dawno dawno temu za siedmioma kucami, żył sobie spokojny chłop."
    narrator "Nie był on w żaden sposób nadzwyczajny."
    narrator "Nie był bogaty, ale mógł żyć tak jak zawsze chciał."
    narrator "Miał swój dom, szczęśliwą rodzinę."
    narrator "Czy mógłby chcieć czegoś więcej?"
    narrator "Już niedługo na tym świecie pojawi się jego pierworodny syn."
    narrator "Od razu wiedzieli jak go będą chcieli nazwać."
    narrator "Andrzej."
    narrator "W rodzinie Somsiada imię to nosiło za sobą wielką historię."
    narrator "Historię pełną szczęścia, radości, ale również cierpienia."
    narrator "I tak oto rozpoczął się kolejny spokojny dzień w rodzinie Korzennych."

    mariolka "Heeeeej kochanieee, przyniesiesz mi prosze mleko ze strychu?"
    mariolka "Byłam pewna, że je wczoraj otwierałam i wkładałam do lodówki, ale nie moge go teraz nigdzie znaleźć."

    narrator "Somsiad wiedział najlepiej, że nie należy podważać autorytetu małżonki przed jej poranna kawą  i ruszył na strych."
    narrator "Nie kwestionował już nawet dlaczego akurat tam postanowiła je trzymać."
    narrator "Najwidoczniej to tylko kolejny zwyczaj Korzennych."

    show somsiad
    somsiad "..."
    hide somsiad

    narrator "Dziwne."
    narrator "Na strychu nie było nawet żadnego śladu po mleku."
    narrator "Pierwszy raz w historii Korzennych ich “Ultimate plan żywieniowy” zawiódł."
    narrator "Somsiad wiedział, że ktoś musiał maczać w jego mleku palce."
    show somsiad
    narrator "Somsiad"
    hide somsiad

    show somsiad_one
    narrator "był"
    hide somsiad_one

    show somsiad_two
    narrator "zły."
    hide somsiad_two
    narrator "Nie chcąc jednak niepokoić małżonki, szybko wyskoczył przez okno i ruszył do ich krowy."
    narrator "Nie wiedział on jednak, że to dopiero początek niezapomnianej przygody."
    narrator "Otóż każdy wie, że"
    narrator "Tak jak i świat z korzenia sie zaczął, tak i on w korzeń kiedyś urośnie."

    ###
    scene uwu with dissolve
    show anime_gurl
    play sound "audio/breaking_news.mov" volume 1
    anime "Błeajking nuwus! "
    anime "Wszłemdzie tjmńłicio znikła melko. Pobłiskie medłja sugełują zakup kluwuw. "
    anime "Nje wiadomo jeście dłaciego sie tak dźłieje, aćkolwiek pojawłiają sie pziecieki o pławdopodobnym atakłu telłołystyćnym na wapń u najmłodsich. >.<"
    anime "See nyaaaa~~~~"
    anime "✌️ 😗 ✌️"
    ###

    scene pole with dissolve
    narrator "Somsiad jak prawdziwy farmer, miał swoją krowę - Muuucie."
    show krowa
    krowa "Muuuusisz mi teraz przeszkadzać?"
    krowa "Mooogłes przyjść wcześniej co nie?"
    krowa "Muuuam teraz spanko..."
    krowa "Muuusisz przyjść później 😠"

    narrator "Krowa Muuucia nie była najlepsza krową w okolicy, ale zawsze to była jego krowa."
    narrator "I nagle niczym grom z jasnego nieba pojawiło się..."
    narrator "ufo."
    hide krowa

    show kosmici with dissolve

    kosmita_one "Joł joł joł"
    kosmita_two "*beatboksuje*"
    kosmita_one "Słuchaj stary, bo jest sprawa"
    kosmita_one "Moze lekko niefosforawa"
    kosmita_one "Twoja krowa"
    kosmita_one "to moja krowa"
    kosmita_one "Naura"
    hide kosmici

    narrator "No nie."
    narrator "Najgorzej."
    narrator "Somsiad już nie miał krowy."
    narrator "Wiedział jednak co musi zrobić. Niczym strzała zerwał się do pobliskiego korzenia."
    show krzak
    narrator "Otóż każdy wie, że kto korzenia pyta ten nie zakorzenia."
    narrator "Chwycił za pobliski krzak. Po chwili walki udało mu się go wyciągnąć."
    hide krzak

    show melon
    melon "MMHMASSASD MTFNFHHRBDV MSDSFSF."
    melon "…"
    melon "DFSGDFGHGH"
    melon "sdkfsdjfsdjh"
    hide melon

    narrator "Melon Mózk ewidentnie jest yyyy"
    narrator "można by rzec "
    narrator "zaskoczony" 
    narrator "nagłym wyrwaniem z jego oglądania upadającego stoka." 
    narrator "He he, został"
    narrator "wykorzeniony ze swojego stanowiska. "
    narrator "W każdym bądź razie, jestem przekonany, że Melon Mózk jest w stanie porozumiewać się po ludzku."
    narrator "Prawda Melon?."

    show musk
    melon "Tak jest! Prosze wielki narratorze nie rób mi krzywdy." 

    somsiad "…"

    narrator "Somsiad szybko zapomniał o tym jakimś dziwnym rozbiciu 4 ściany i wrócił do rozmowy z Melonem Mózkiem." 

    melon "Witam." 
    melon "Jeśli chcesz dowiedzieć się, jak złożyć domowe ogrzewanie atomowe, pociągnij za liść numer jeden."
    melon "Jeśli chcesz złożyć uwagę na temat wybuchających pestek naszej firmy, pociągnij za liść numer dwa.."
    melon "Jeśli chcesz dowiedzieć się ..."

    narrator "Somsiad bardzo niemiło przerwał gadanie Melona Mózka, mimo że ten EWIDENTNIE jeszcze nie skończył, i od razu po tych słowach pociągnął go za liść numer trzy." 
    narrator "To skąd wiedział, który to jest pozostaje swoją własną zagadką, na która nawet ja nie znam odpowiedzi."

    melon "Wybrałeś liść numer trzy."
    melon "Niestety na ten moment nie mamy wolnych operatorów z tej dziedziny, prosze czekać"
    hide musk

    somsiad "…"
    show somsiad
    somsiad "…"
    hide somsiad
    show somsiad_one
    somsiad "…"
    hide somsiad_one
    show somsiad_two
    somsiad "…"
    hide somsiad_two

    show musk
    melon "Dziękuje za cierpliwość z tej strony Melon Móżkk. Czego Pan pragnie dowiedzieć się na temat porwanych krów?"
    hide musk

    show somsiad_two
    somsiad "…"
    hide somsiad_two

    show musk
    melon "Rozumiem,"
    melon "niestety nie jesteśmy w stanie Panu teraz pomóc, jako że tym zajmuje się Dodz."
    melon "Proszę podać mu tę monetę, a ten spełni Pana życzenie."
    melon "Dziękuje za skorzystanie z naszych usług, do widzenia."

    narrator "Somsiad zobaczył jak na jego oczach Melon Mózk zmienił się w korzenna monetę, zbudowana z UWAGA UWAGA korzeni. Ah tak, jak to stare przysłowie mówi:"
    hide musk
    show coin
    narrator "Kto komu korzeń ten temu moneta, a moneta robi backflip."
    hide coin

    ###
    scene uwu with dissolve
    show anime_gurl
    anime "Błeajking nuwus!" 
    anime "Ośtłatńio nja śieci njesamowłitom popułałność zdiobiwia nowy wykłonawcła Yung Milq wypłomowany płzeź ańiominiowy ześpiuł U. F. O. łówniesz znłany jako unidentified fliing object! Ich njowy wpłólny kawłałek “Młumłisie muwuwu” podłbija sociał midia"
    anime "See nyaaaa~~~~"
    anime "✌️ 😗 ✌️"
    hide anime
    ###

    scene las with dissolve
    narrator "Tak oto somsiad wybrał się na podróż przez lasu Skowrytu. Pokonując niezliczone przeszkody dotarł do Dodż’a."
    narrator "Było to wręcz mityczne stworzenie od lat mieszkające w najgłośniejszej części lasu Skowrytu."
    narrator "Dźwięk tam zawsze jest powyżej 100db."
    
    somsiad "…"

    show dogee
    doge "HENLO FREND"
    doge "COM TAM"
    doge "MIŁOM MIM CIEM WIMDZIEĆ"
    doge "CZEGOM POTRZEBUJESZ" 


    hide dogee
    show somsiad_one
    somsiad "…"
    hide somsiad_one

    show dogee
    doge "AAA ROZUMIEM"
    doge "ALE KAŻDYM MUSI ZAPŁACIĆ ZANIM ZOSTANIE ZAKORZENIONY"

    hide dogee
    show somsiad_one
    somsiad "…"
    hide somsiad_one

    show dogee
    doge "DZIEMKUJE" 
    doge "CZEGO SOBIE ŻYCZYSZ"
 
    hide dogee
    show somsiad_one
    narrator "Somsiad powiedział ... Święty Spokój"
    hide somsiad_one

    show dogee
    doge "…"

    hide dogee
    show somsiad_one
    somsiad "…"
    hide somsiad_one

    show dogee
    doge "…"

    hide dogee
    show somsiad_one
    somsiad "…"
    hide somsiad_one

    show dogee
    doge "…"
    doge "CHODZIŁO CI MOZE O:"
    doge "KAMIEŃ?"
    hide dogee

    show kamien_onee
    kamien_one "🐛"
    hide kamien_onee

    show somsiad_one
    somsiad "…"
    hide somsiad_one

    show dogee
    doge "JAKIEM JEST TWOJE DRUGIE ŻYCZENIE?"
    hide dogee

    show somsiad_one
    narrator "Somsiad powiedział ... Chciałbym w końcu rozumieć co oni mówią w Błeajking nuwus!"
    hide somsiad_one

    show dogee
    doge "…"

    hide dogee
    show somsiad_one
    somsiad "…"
    hide somsiad_one

    show dogee
    doge "…"

    hide dogee
    show somsiad_one
    somsiad "…"
    hide somsiad_one

    show dogee
    doge "…"
    doge "CHODZIŁO CI MOZE O:"
    doge "KAMIEŃ?"
    hide dogee

    show kamien_twoo
    kamien_two "Rozłożyło mnie przeziębienie 😢😢"
    hide kamien_twoo

    show dogee
    doge "JAKIEM JEST TWOJE TRZECIE ŻYCZENIE?"
    hide dogee

    show somsiad
    narrator "Somsiad powiedział ... Chciałbym zobaczyć jak mój Syn dorasta"
    hide somsiad

    show dogee
    doge "…"

    hide dogee
    show somsiad_one
    somsiad "…"
    hide somsiad_one

    show dogee
    doge "…"

    hide dogee
    show somsiad_one
    somsiad "…"
    hide somsiad_one

    show dogee
    doge "…"
    doge "CHODZIŁO CI MOZE O:"
    doge "KAMIEŃ?"
    hide dogee

    show kamien_threee
    kamien_three "Ze względów prywatnych nie mogę dalej uczestniczyć w tej rozmowie"
    hide kamien_threee

    show dogee
    doge "DOBRA, DZIEMKUJE ZA TWÓJ BIZNES, A TERAZ WYBACZ, ALE ZA CHWILE ROPOCZYNA SIĘ KONCERT YUNG MILQ."
    hide dogee

    hide dogee
    show somsiad_one
    somsiad "…"
    hide somsiad_one

    show kamieniee
    kamienie "👥 👟 ⏮️ 👆"

    
    narrator "Somsiad nie zwlekając ani chwili dłużej, mając odwieczne marzenie o straceniu słuchu jak Dodż, ruszył z nimi na koncert."
    narrator "Z jakiegoś powodu, Yung Milq wydawało mu sie bardzo bliskie, ale to było zmartwienie na inna porę."
    hide kamieniee

    ###
    scene uwu with dissolve
    show anime_gurl
    anime "Błeajking nuwus!" 
    anime "Jus dźłiś w lasie Skowłituwu rusia płmieła niowej płity Yung Milku! Łazem z ńią wiśtąpią nja ścieńje U. F. O. !!!!"
    anime "Jak źwikle wiśtempy w lasie Skowłitu wśtięp jeśt źia diarmo, ałe ołganiźiatoły nje odpjowiadiają źia wśielkom utlate śluchuwu."
    anime "See nyaaaa~~~~"
    anime "✌️ 😗 ✌️"
    hide anime_gurl
    ###

    scene party with dissolve
    show yong_milq
    yong_milq "Muuuiło mi was tu wszystkich widzieć!"
    yong_milq "Muuuszze wam podziękować, za tak dobry odzew mojej skromnej osoby."
    yong_milq "Moooże być tak, że ogłuchnięcie, ale jak była mooowa wcześniej, my nie jesteśmy za nic odpowiedzialni."
    yong_milq "Moooge się z wami podzielić moją historią, otóż wcześniej byłam zwykłą krową, żyłam sobie i nic nikomu nie robiłam, a ten wstrętny Somsiad nawet nie dawał mi spać."
    yong_milq "Moooje rapy nie były wtedy docenione, ale to już tylko przeszłość."
    yong_milq "Mooo…"
    hide yong_milq

    show somsiad
    somsiad "…"
    hide somsiad

    narrator "Somsiad ponownie pokazując swoje niesamowite poziomy empatii, przerwał komuś wypowiedź, wtrącając swoje trzy grosze. "
    narrator "Co gorsza,"
    narrator "tym razem jeszcze się odwrócił i odszedł."
    narrator "Wiedział, że potrzebuje chwili przerwy i w sumie, "
    narrator "zjadł by coś."
    narrator "Somsiad uznał, że pójdzie do pobliskiej Ropuchy™℠®©."

    scene shop with dissolve
    
    somsiad "…"

    narrator "Kiedy już Somsiad zbliżał się do Ropuchy™℠®© zobaczył podejrzaną postać wychodzącą stamtąd z ..."
    narrator "chwila"
    narrator "czy Somsiad dobrze widzi?"
    narrator "ON WYNOSI WŁAŚNIE CAŁE MLEKO Z TEGO SKLEPU."
    show chad
    narrator "TAK"
    narrator "BYC"
    narrator "NIE-E"
    narrator "MOZE."
    narrator "Tak oto Somsiad ruszył w pogoń za tajemniczą postacią."

    chad "Wiedziałem, że w końcu po mnie przybędziesz."
    chad "W końcu Twoja historia była mi już dawno znana."

    somsiad "…"

    narrator "Somsiad wytłumaczył mu, że nawet nie wie kim jest ???."

    chad "Nic nie zmieni znajomość mojego imienia. Możesz mnie nazywać jak tylko chcesz, ale wiedz że nic nie możesz zrobić."
    chad "korzeń"
    chad "już"
    chad "urósł." 
    chad "W tym momencie, hah"
    chad "co ja mogę powiedzieć oprócz"
    chad "przegrałeś."

    narrator "Somsiad mając dość narzekania ??? rzuca w niego ziemniakiem, który akurat trzymał w swojej kieszeni."
    narrator "Przez to ??? upuścił jedno z wielu mlek, które ma ze sobą, rozlewając je."

    chad "NIEEEE"
    chad "CO TY NAROBIŁEŚ"
    hide chad

    narrator "Nagle z ziemi dookoła ??? zaczęły wyrastać korzenie. Somsiad mając łeb na karku spytał się czemu tak się dzieje."
    show korzen

    show chad
    chad "Korzenie to jest podstawa, korzenie to wszystko. Dzięki nim całe uniwersum może istnieć. Historia była w nich od dawna zapisana, a Ty ją tak bezmyślnie zepsułeś."
    chad "Ja chciałem wszystko naprawić."
    chad "Ja"
    scene breaker with dissolve
    chad "Ja po prostu chciałem mieć ojca!"
    chad "Nigdy nie wróciłeś do mnie!"
    chad "Specjalnie dla Ciebie zniszczyłem czasoprzestrzeń, żeby móc zapobiec temu dniu."
    chad "Teraz kiedy jednak Ciebie spotkałem, wiem już jedno."
    chad "Cieszę się, że nigdy wcześniej cię nie spotkałem."

    narrator "W czasie monologu, jak na to wychodzi Andrzeja, korzenie powoli rozrywały czasoprzestrzeń dookoła niego, żeby móc się go pozbyć."

    somsiad "…"

    narrator "Gdy Andrzej już prawie całkowicie został wypchnięty, Somsiad rzucił się na niego i razem przelecieli przez portal"

    ###
    scene uwu with dissolve
    show anime_gurl
    anime "Błeajking nuwus!"
    anime "Mińjeło juś 19 latć odkiąt ośtatni łaz widźiano Somsiada."
    anime "Njektuzi mówią, ze śpędźia on cijaś w lesie Skowłitu, jakoś sie ośtatńji raź bił tam widźjany."
    anime "Ja włiem jedńiak lepiej i źdaję sobię śprawę, źie ten od djawnia nje istnieje w tiej łeczywiśtości!"
    anime "Otjóś Kłołenni od djawien dawńa mają pewńia tradycje, ale cio ja wiam będie opjowiadjać, lepiej ziobaćie śjami!"
    anime "See nyaaaa~~~~"
    anime "✌️ 😗 ✌️"
    hide anime_gurl
    ###

    scene dom with dissolve
    mariolka "Andrzej, obudź się! Twoi znajomi niedługo będą!"

    show andrzej
    andrzej "..." 

    narrator "Andrzej próbował z całych sił odpowiedzieć swojej mamie na jej zawołanie, lecz nie mógł z siebie wydobyć żadnego dźwięku."

    andrzej "..."

    narrator "Andrzej w panice zaczął rozglądać się dookoła, zupełnie niepotrzebnie, przecież jestem tylko zwykłym narratorem"

    andrzej "..."

    narrator "Jak to zawsze jest w rodzinie Korzennych pierworodny syn w momencie swoich 19 urodzin łączy się ze swoim ojcem i ten zostaje nowym narratorem."
    narrator "Nie martw się synu, mimo że tego nie wiesz, bo w teorii tego nie przeżyłeś, swoimi czynami w przyszłości zaburzyłeś czasoprzestrzeń."
    narrator "Przez 19 lat krążyłem w nicości, ale przeczekałem je specjalnie dla Ciebie."
    narrator "Andrzej nie marnował już więcej czasu na rozmyślaniem nad ojcem, którego nigdy nie poznał i poszedł się szykować do swojego wyjazdu."
    narrator "W końcu dzisiaj wyjeżdżał na Podstawy Jądrowej Autonomii Tworzyw Katastrofialnych"
    narrator "inaczej też zwany"
    narrator "PJATK"
    hide andrzej

    ###
    scene uwu with dissolve
    show anime_gurl
    anime "Błeajking nuwus!"
    anime "I tjak otio przedśtawia się hiśtiołia Kłołennich"
    anime "Mjam nadźjeje sie wjam sie podjobało"
    anime "Djo zobjaczenja kolejnym łaziem"
    anime "See nyaaaa~~~~"
    anime "✌️ 😗 ✌️ "
    hide anime_gurl
    ###

    # This ends the game.

    return
