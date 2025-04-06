# 🤖 Youthall Job Notifier Bot

Youthall web sitesinde yayımlanan yeni iş ilanlarını takip eder, daha önce paylaşılmayan ilanları MongoDB veritabanında kontrol eder ve yeni ilanları Telegram üzerinden bildiren bir Python botudur.

## 📌 Amaç

Yeni ilanları sürekli kontrol etmek yerine, bu bot sayesinde sadece yeni eklenen ilanlar Telegram üzerinden bildirilir. GitHub Actions kullanarak bu botu belirli aralıklarla çalıştırır ve yeni ilanları otomatik olarak kontrol eder. Böylece zaman kaybı ve tekrar eden kontrol işlemleri ortadan kaldırır.


## 🧰 Kullanılan Teknolojiler

- **Python** - Betik dili
- **BeautifulSoup** - HTML parse işlemleri
- **Requests** - Web'den veri çekme
- **MongoDB Atlas** - Veritabanı
- **Telegram Bot API** - Bildirim gönderimi
- **GitHub Actions** - Otomatik çalışma zamanlaması

## 🚀 Kurulum

### Telegram Bot Oluşturma

Telegram botu oluşturmak için aşağıdaki adımları izleyin:

1. **@BotFather ile sohbet başlatın:**
   - Telegram uygulamanızda **@BotFather** aratın ve sohbeti başlatın.

2. **Yeni Bot Oluşturun:**
   - **/newbot** komutunu yazın ve yönergeleri takip edin. Botunuz için bir isim ve kullanıcı adı seçmeniz istenecek.

3. **Token Alın:**
   - Bot oluşturulduktan sonra, **BotFather** size bir **API token** verecektir. Bu token'ı kaydedin, daha sonra `BOT_TOKEN` olarak kullanabilirsiniz.

4. **Chat ID'nizi Öğrenin:**
   - Chat ID'nizi öğrenmek için **@get_id_bot** adlı Telegram botunu kullanabilirsiniz.
   - **@get_id_bot** ile sohbet başlatın ve **/start** komutunu yazın.
   - Bot, size Telegram hesabınıza ait **Chat ID**'yi gönderecektir.

Bu adımları tamamladıktan sonra, Telegram botunuzu API token'ı ve chat ID'nizi kullanarak yapılandırabilirsiniz.

### 1. Gerekli paketleri yükle

```bash
pip install -r requirements.txt
```
### 2. Ortam değişkenlerini ayarla

```bash
MONGODB_URI=mongodb_connection_string
BOT_TOKEN=telegram_bot_token
CHAT_ID=telegram_chat_id
```
### 3. Botu çalıştır
```bash
python youthall_notifier.py
```