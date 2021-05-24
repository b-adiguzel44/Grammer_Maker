# region Imported Modules/Packages

import random               # random modülünü projeye import ettim

# endregion

# region Classes


class Palindrom:
    '''Rastgele uzunlukta bir palindrom kelime üretir'''

    # __init__ function - Constructor/Initializer (Sınıftan bir nesne türettiğimizde çalışacak özel fonksiyonumuz)
    def __init__(self):
        # Kelime uzunluğu rastgele 0-50 arası olarak ayarladım
        leng = random.randint(0, 50)
        # Eğer uzunluk sıfır ise
        if leng == 0:
            self.word = 'ε'         # Kelimemizi epsilon karakteri yap
        else:
            # Uzunluk çift ise
            # 0 ve 1 lerden oluşan kelime oluşturuyorum. İlk kısmının yarısını alıyorum
            first = [str(random.randint(0, 1)) for s in range(leng // 2)]
            last = first[::-1]          # İlk oluşan kısmı ters çevirir, last nesnesine atar
            # Uzunluk çift ise
            if leng % 2 == 0:
                self.word = ''.join(first+last)     # Listeleri birleştiririz ve palindrom bir kelime elde etmiş oluruz
            # Uzunluk tek ise
            else:
                # Ortanca kısma rastgele 0-1 den oluşan bir sayı ekliyorum
                self.word = ''.join(first+[str(random.randint(0, 1))]+last)
        self.leng = leng               # İlgili nesnenin len attribute ını atıyorum
        # print('Kurucu fonksiyon çalıştı')

    def yazdir(self):
        '''Palindrom sınıfından türetilen nesnenin kelimesini ve uzunluğunu yazdırır'''
        return f'Kelime : {self.word}\nUzunluk: {self.leng}'

    @classmethod
    def is_pal(cls, str_):
        '''Bu string palindrome mu? (Tersten ve düzden yazılışı aynı mı?)'''
        if len(str_) <= 1:  # Base Case
            return True
        else:               # Recursive (Öz yinelemeli) case
            return str_[0] == str_[-1] and cls.is_pal(str_[1:-1])

    @classmethod
    def test(cls, word):
        '''Gelen string in palindrom olup olmadığını test edicektir. Kelime palindrom ise yazım yapılacaktır.'''

        try:
            assert type(word) == str
        except AssertionError:
            return 'Argümanın veri tipinin string olması beklenmektedir'

        # Gelen string argümanı, bir palindrom string değil ise
        if not cls.is_pal(word):
            return 'Girilen kelime, palindrom bir kelime değildir.'
        else:

            letter = '#'                                    # Çıktıda göstereceğim harf
            p_word = ''                                     # Çıktıda gözükecek string
            i = 0                                           # Kelimeyi indis bölmesi yaparken kullanıyoruz

            # Kelimenin uzunluğunu kontrol ediyoruz (ÇİFT İSE BURASI)
            if len(word) % 2 == 0:

                half_word_list = word[0:((len(word) // 2)+1)]  # Kelimenin yarısını aldık
                # (+1 ekliyoruz ki tam kısmı alsın = 101101 --> 101)

                while True:

                    # Oluşacak kelimenin uzunluğu, gelen kelimenin uzunluğundan büyük ise yazdırma işlemi biter
                    if len(p_word) > len(word):
                        # print(word)
                        return word
                    else:

                        # Son kısmdaki slicing kısmı string i ters çevirir.
                        p_word = half_word_list[:i + 1] + letter + half_word_list[:i + 1][::-1]

                        # Oluşan kelimeyi yazdırdık
                        print(p_word)

                    i += 1  # İndis sayımızı arttırıyoruz
            # (TEK İSE BURASI)
            else:

                half_word_list = word[0:len(word)//2]               # Kelimenin yarısını aldın

                while True:

                    if len(p_word) == len(word):            # Uzunlukları aynı olduğunda
                        # print(word)
                        return word                         # İşlem bitmiştir
                    else:
                        # Son kısmdaki slicing kısmı string i ters çevirir.
                        p_word = half_word_list[:i+1] + letter + half_word_list[:i+1][::-1]
                        print(p_word)           # Oluşan kelimeyi yazdırdık

                    i += 1                                  # İndis sayımızı arttırıyoruz

    @classmethod
    def uzunluk(cls, kelime1, kelime2):
        '''Girilen iki kelimenin aynı uzunlukta olup olmadığını kontrol eder'''
        try:
            # Gelen iki argümanın string bir veri olduğunu iddia ediyoruz.
            assert type(kelime1) and type(kelime2) == str

            # Argüman olarak gelen kelimelerin palindrom olması beklenmektedir.
            if not cls.is_pal(kelime1) or not cls.is_pal(kelime2):
                return 'Argüman olarak gelen kelimelerin palindrom olması gerekmektedir.'

            if len(kelime1) > len(kelime2):
                return 'İlk kelimenin uzunluğu, ikinci kelimenin uzunluğundan büyüktür'
            elif len(kelime1) < len(kelime2):
                return 'İkinci kelimenin uzunluğu, ilk kelimenin uzunluğundan büyüktür'
            else:
                return 'Girilen iki kelimenin uzunluğu birbirine eşittir'
        except AssertionError:
            return 'Argüman veri tipleri hatalı. String tipinde veri/veriler bekleniyor.'


class UnlemliPalindrom(Palindrom):
    '''Palindrom sınıfından türettiğimiz bir Child Class'tır'''
    # __init__ function - Constructor/Initializer (Sınıftan bir nesne türettiğimizde çalışacak özel fonksiyonumuz)
    def __init__(self):
        # _(single underscore): Python da özel bir değişkendir. Derleyicide yapılan en son durumları kaydeder.
        # Genelde ilgilenmek istenenmeyen veriler atılır veya geçici bir değişken niyetinde kullanılabilir.

        super().__init__()                      # Base/Parent Class ın init i çalıştı
        if self.leng != 0:       # Uzunluk sıfır değil ise
            _ = (' '.join(self.word)).split(' ')    # Kelimeyi list şekline çeviriyoruz
            # print(_)
            _[0], _[-1] = '!', '!'                  # Kelimenin başına ve sonuna ünlem işareti koyuyoruz
            self.word = ''.join(_)                  # Tekrardan string e çeviriyoruz
        # print('Child class çalıştı')

# endregion

# region Functions


def line(x='', y='-', z=29):
    # x = başlık, y = çizgi karakteri, z = adet
    print(x, str(y * z), sep='\n')


def class_code_show(code='Kod yok'):
    '''İlgili class ın metod ve Attributelerinin yazıp altında çıktısını gösterir
ÖRNEK  ÇIKTI :
class.attirbute_name Ya da class.method_name(args)
-----------------------------
(İlgili Attribute'in veya Method'un çıktısı)
'''
    try:
        assert type(code) == str       # code argümanın bir string ifade olması gerektiğini belirtiyoruz(iddia ediyoruz)
        line(f'\n{code}')              # gelen code değişkenini başlık olarak yazdırıp altına çizgi ekler
        exec(f"print({code})")         # string bir ifadeyi koda döktürüp çalıştırır
    except AssertionError:  # String ifade değilse
        return 'code argümanı bir string ifade olmalıdır'


# endregion

# region Main Program
# Eğer bu modül/script direkt olarak çalıştırılır ise if komutu bloğu çalışacaktır

if __name__ == '__main__':

    p_word1 = Palindrom()            # p_word1 isimli, Palindrom sınıfında nesne türettik
    p_word2 = Palindrom()            # p_word2 isimli bir nesneyi Palindrom sınıfından türettik
    p_word3 = UnlemliPalindrom()     # p_word3 isimli bir nesneyi UnlemliPalindrom sınıfından türettik

    # line('\nword 1 nesnesi')
    # print(p_word1.yazdir())          # p_word1 in durumunu görmek için yazdırdık
    class_code_show('p_word1.yazdir()')

    # line('\nword 2 nesnesi')
    # print(p_word2.yazdir())          # p_word2 in durumunu görmek için yazdırdık
    class_code_show('p_word2.yazdir()')

    # line('\nword 3 nesnesi')
    # print(p_word3.yazdir())          # p_word3 in durumunu görmek için yazdırdık
    class_code_show('p_word3.yazdir()')

    # test(string) metodu işlemleri
    # ------------------------------------------

    # print(Palindrom.test(p_word3.word))
    class_code_show('Palindrom.test(p_word3.word)')

    # print(Palindrom.test('AHMETEMA'))
    class_code_show("Palindrom.test('AHMETEMA')")

    # print(Palindrom.test(p_word1.word))
    class_code_show('Palindrom.test(p_word1.word)')

    # uzunluk(kelime1, kelime2) metodu işlemleri
    # ------------------------------------------
    line('\nuzunluk() metodu işlemleri', '*')

    # print(Palindrom.uzunluk('2312', 'AsA'))
    class_code_show("Palindrom.uzunluk('2312', 'AsA')")

    # print(Palindrom.uzunluk(p_word1.word, p_word2.word))      # uzunluk() metodu, class method dur
    class_code_show('Palindrom.uzunluk(p_word1.word, p_word2.word)')

    # print(Palindrom.uzunluk(p_word2.word, p_word2.word))
    class_code_show('Palindrom.uzunluk(p_word2.word, p_word2.word)')

    # print(word_2.__dir__())
    # print(dir(Palindrom))

# endregion
