<h1>RSA Şifreleme Programı</h1>

Bu program, Python dilinde RSA (Rivest-Shamir-Adleman) şifreleme algoritmasını kullanarak metinleri şifrelemek ve çözmek için bir araç sağlar.

<h2>Kurulum</h2>
Programın çalıştırılabilmesi için Python 3 ve math modülünün yüklü olması gerekmektedir. İlgili modülü yüklemek için aşağıdaki komutu kullanabilirsiniz:

<code>pip install math</code>

<h2>Kullanım</h2>
Programı çalıştırmak için aşağıdaki adımları izleyin:

Terminali açın ve programın kaynak kodunu içeren dizine gidin.
python rsa.py komutunu kullanarak programı başlatın.
Program çalıştırıldığında, kullanıcıdan p ve q olarak iki asal sayı girmesi istenir. Bu sayılar, RSA algoritması için gerekli anahtar çiftini oluşturmak için kullanılır.

Daha sonra, kullanıcıdan şifrelenmek istenen mesajı girmesi istenir. Girilen metin, oluşturulan anahtar çifti kullanılarak şifrelenir ve şifreli mesaj ekrana yazdırılır.

Aynı anahtar çifti kullanılarak şifreli mesaj çözülür ve orijinal mesaj ekrana yazdırılır.
