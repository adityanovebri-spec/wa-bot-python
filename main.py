# =====================================================================
# WA-BotStudio: WhatsApp Chatbot Otomatis (FastAPI + Twilio Sandbox)
# =====================================================================

import os
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Response, status
from twilio.twiml.messaging_response import MessagingResponse

load_dotenv()

app = FastAPI(title="WhatsApp Bot Twilio")

@app.get("/")
def home():
    return {"status": "online", "message": "Bot WhatsApp aktif!"}

@app.post("/webhook")
async def whatsapp_webhook(
    Body: str = Form(default=""),
    From: str = Form(default=""),
    ProfileName: str = Form(default="Pelanggan")
):
    user_msg = Body.strip().lower()
    print(f"[PESAN MASUK] Dari: {ProfileName} ({From}) | Isi: {Body}")

    # 1. Menu Salam
    if ("halo" in user_msg or "hai" in user_msg or "menu" in user_msg or "start" in user_msg):
        reply_text = """Halo! 👋 Selamat datang di layanan otomatis kami.

Ketik angka pilihan menu di bawah ini untuk informasi cepat:
1️⃣ *Daftar Produk & Harga*
2️⃣ *Jam Operasional & Alamat*
3️⃣ *Cara Pemesanan & Pembayaran*
4️⃣ *Hubungi Customer Service (CS)*

Ketik *menu* kapan saja untuk kembali ke pilihan ini."""

    # 2. Menu 1: Produk & Harga
    elif ("1" in user_msg or "produk" in user_msg or "harga" in user_msg or "paket" in user_msg):
        reply_text = """📦 *DAFTAR PRODUK & HARGA TERBARU*

1. *Paket Basic*: Rp 50.000 (Konsultasi awal + E-Book)
2. *Paket Pro*: Rp 150.000 (Akses sistem + Template Bot)
3. *Paket Enterprise*: Rp 450.000 (Custom Setup + Pendampingan 1-on-1)

Ketik *3* untuk cara order, atau ketik *menu* untuk kembali."""

    # 3. Menu 2: Jam Operasional & Alamat
    elif ("2" in user_msg or "jam" in user_msg or "buka" in user_msg or "alamat" in user_msg or "lokasi" in user_msg):
        reply_text = """🏢 *INFORMASI OPERASIONAL & LOKASI*

⏰ *Jam Buka*:
- Senin - Jumat: 08.30 - 17.00 WIB
- Sabtu: 09.00 - 14.00 WIB
- Minggu & Libur Nasional: Tutup

📍 *Alamat*: Jl. Sudirman Technopark No. 12, Jakarta Selatan.
Ketik *menu* untuk kembali."""

    # 4. Menu 3: Pembayaran & Rekening BCA Anda
    elif ("3" in user_msg or "order" in user_msg or "pesan" in user_msg or "bayar" in user_msg or "rekening" in user_msg or "transfer" in user_msg):
        reply_text = """💳 *CARA PEMESANAN & PEMBAYARAN*

1. Pilih paket yang Anda inginkan (Ketik *1* untuk melihat paket).
2. Lakukan transfer ke salah satu rekening resmi:
   - BCA: *4125-1500-48* a/n Muhammad Novebri Aditya
3. Kirimkan bukti transfer ke WhatsApp ini beserta nama dan email Anda.
4. Tim kami akan segera mengaktifkan akun Anda dalam waktu maksimal 15 menit.

Ketik *menu* untuk kembali."""

    # 5. Menu 4: Hubungi CS
    elif ("4" in user_msg or "cs" in user_msg or "admin" in user_msg or "operator" in user_msg):
        reply_text = """👨‍💼 *HUBUNGI CUSTOMER SERVICE KAMI*

Pesan Anda telah kami tandai untuk dialihkan ke Tim Customer Service.
Mohon tunggu sejenak, tim kami akan membalas chat ini secara langsung."""

    # 6. Fallback (Jika kata kunci tidak cocok)
    else:
        reply_text = """Maaf, kata kunci tersebut belum kami kenali. 🤖

Silakan pilih angka:
- Ketik *1* untuk Produk & Harga
- Ketik *2* untuk Jam & Alamat
- Ketik *3* untuk Cara Pesan & Rekening
- Ketik *4* untuk Bicara dengan Admin
- Ketik *menu* untuk membuka menu utama"""

    # Respon XML untuk WhatsApp Twilio
    twiml_resp = MessagingResponse()
    twiml_resp.message(reply_text)

    return Response(content=str(twiml_resp), media_type="application/xml", status_code=status.HTTP_200_OK)