# Pertanyaan Terbuka: Kritik dan Masalah Proyek

Dokumen ini menampung pertanyaan untuk penyelidikan dan revisi proyek. Pertanyaan bukan temuan atau klaim bahwa suatu kegagalan telah terbukti. Jawaban yang kelak ditambahkan perlu menunjuk bukti, versi, konteks penggunaan, dan kondisi yang dapat mengubah kesimpulannya.

## Potret repo yang diperiksa

Snapshot lokal pada `2026-10-11`, commit `0800d3a`:

| Paket | Versi pada `plugin.json` | File dalam folder |
| --- | ---: | ---: |
| Reasoning Method Controller | 0.6.1 | 491 |
| Coursecraft Lab | 0.4.1 | 23 |
| AntiSlop | 0.3.1 | 24 |
| Reasoning Consortium Controller | 0.2.0 | 88 |
| Visual Pipeline | 1.0.1 | 93 |

Jumlah file dihitung dari folder hasil ekstraksi, termasuk teks, kode, gambar, PDF, tes, dan konfigurasi. Versi berasal dari metadata lokal paket; tabel ini bukan pemeriksaan apakah versi tersebut masih terbaru di upstream. ZIP sumber tetap di mesin lokal dan dikecualikan dari commit baru. Riwayat Git sebelumnya masih memuat commit yang pernah menyimpan ZIP.

## 1. Tujuan dan batas masalah

- Masalah pengguna seperti apa yang ingin dibantu proyek ini: interpretasi maksud, pembentukan masalah, ideasi, evaluasi solusi, atau lebih dari satu tahap itu?
- Bagaimana proyek membedakan kegagalan model dari masalah pada prompt, konteks, antarmuka, sumber, atau ekspektasi pengguna?
- Apa batas klaim yang dapat dibuat repo ini tentang “bias” atau “penalaran” model tanpa akses ke proses internal model?
- Kondisi apa yang akan menunjukkan bahwa pendekatan proyek tidak membantu pengguna merumuskan atau menyelesaikan masalah?
- Apakah seluruh paket saat ini diperlukan untuk tujuan inti, dan bukti apa yang menentukan bahwa sebuah paket termasuk inti atau hanya berdekatan?

## 2. Interpretasi, ideasi, dan pembentukan masalah

- Bagaimana sistem mengetahui kapan harus meminta klarifikasi dan kapan sebaiknya mengajukan beberapa tafsir yang dapat dibandingkan?
- Bagaimana ia membedakan ideasi awal, definisi masalah, kendala, hipotesis, dan keputusan yang sudah disetujui pengguna?
- Bagaimana pengguna dapat mengoreksi interpretasi model dengan biaya rendah sebelum interpretasi itu menjadi dasar rekomendasi atau tindakan?
- Seberapa sering model mengganti masalah pengguna dengan masalah yang lebih mudah dijawab, dan bagaimana kejadian itu akan dicatat?
- Bukti apa yang dapat membedakan klarifikasi yang membantu dari pertanyaan tambahan yang hanya memperlambat pekerjaan?

## 3. Reasoning Method Controller

- Dalam jenis tugas apa tahapan, pemeriksaan bukti, dan perbaikan ketergantungan paling meningkatkan hasil; dalam tugas apa justru menambah beban?
- Apakah pemeriksaan terhadap pesaing, contoh negatif, dan kondisi yang dapat membalik kesimpulan berhasil menemukan kesalahan yang lolos dari jawaban awal?
- Bagaimana pengguna dapat melihat asal-usul klaim dan asumsi tanpa menerima penjelasan panjang yang tidak dapat diverifikasi?
- Apakah konsep “perbaiki ketergantungan paling awal yang gagal” menghasilkan koreksi yang lebih tepat daripada memperbaiki jawaban akhir saja?
- Kegagalan apa yang masih terjadi ketika model mengikuti prosedur yang tertulis dengan benar tetapi salah memahami domain atau tujuan manusia?

## 4. Coursecraft Lab dan interaksi belajar

- Apakah bentuk visual atau interaktif membantu pengguna mendeteksi perbedaan antara maksudnya dan tafsir model? Pada tugas dan pengguna yang mana?
- Performa apa yang menunjukkan pemahaman mandiri, bukan sekadar keberhasilan meniru contoh?
- Bagaimana materi memberi dukungan bagi pengguna yang memakai teknologi bantu atau lebih nyaman dengan penjelasan teks?
- Bagaimana Coursecraft membedakan sumber bidang, metode pengajaran, contoh latihan, dan hasil buatan model?
- Apakah latihan transfer mengungkap pemahaman yang bertahan saat konteks atau alat berubah?

## 5. AntiSlop dan guardrail

- Jenis kegagalan keluaran mana yang paling sering terjadi pada penggunaan nyata, dan mana yang paling merugikan pengguna?
- Seberapa baik aturan eksplisit mendeteksi kegagalan itu tanpa menandai variasi bahasa atau gaya yang sebenarnya berguna?
- Bagaimana corpus regresi memperoleh contoh yang berizin, representatif, dan cukup beragam tanpa mengumpulkan percakapan pribadi berlebihan?
- Bagaimana tingkat salah-positif dan salah-negatif diukur untuk tiap pemeriksaan?
- Apa yang terjadi ketika guardrail bertentangan dengan kebutuhan domain, bahasa, atau instruksi pengguna yang sah?

## 6. Reasoning Consortium Controller

- Masalah mana yang benar-benar mendapat manfaat dari analisis terpisah, dan kapan beberapa worker hanya mengulang asumsi atau kesalahan yang sama?
- Bagaimana independensi tiap worker diuji, bukan hanya dinyatakan dalam desain tugas?
- Kriteria apa yang membuat sebuah hasil layak digabung, dipertahankan sebagai konflik, atau dibuka kembali setelah bukti baru?
- Dalam penggunaan nyata, apakah biaya konteks, waktu, dan kompleksitas orkestrasi sebanding dengan peningkatan kualitas keputusan?
- Bukti runtime apa yang diperlukan sebelum mengklaim eksekusi paralel atau isolasi antar-worker?

## 7. Visual Pipeline sebagai paket berdekatan

- Hubungan apa yang dapat dibuktikan antara pipeline visual dan tujuan utama repo tentang interpretasi serta pemecahan masalah manusia–AI?
- Apakah paket ini berfungsi sebagai contoh interaksi visual yang dapat dipindahkan ke domain lain, atau tetap merupakan alur kerja kreatif khusus?
- Konsep dan artefak mana yang dapat dibagikan lintas paket tanpa menyamakan kebutuhan visual dengan bukti reasoning?
- Apakah repo sebaiknya mempertahankan paket ini sebagai eksperimen berdekatan, memindahkannya ke repo lain, atau menjelaskan keterkaitannya dengan lebih spesifik?

## 8. Data, evaluasi, dan pembaruan

- Unit analisis apa yang paling berguna: giliran percakapan, perubahan pemahaman pengguna, keputusan, artefak akhir, atau proses perbaikannya?
- Dataset seperti apa yang dapat menguji interpretasi, ideasi, dan problem-solving tanpa menyamakan kefasihan dengan kebenaran?
- Bagaimana anotator menyepakati maksud pengguna ketika permintaan memang ambigu atau berubah selama interaksi?
- Apa pembanding yang adil: jawaban satu model, beberapa model, pengguna tanpa bantuan, atau alur kerja alternatif?
- Bagaimana perubahan versi model dan paket dicatat agar hasil lama tidak dianggap berlaku untuk versi baru?
- Metrik apa yang dapat dipakai bersama, dan bagian mana yang harus tetap dinilai melalui penjelasan atau artefak manusia?

## 9. Privasi, lisensi, dan distribusi

- Materi mana di setiap paket yang berasal dari pihak ketiga, percakapan, atau konteks personal, dan izin apa yang berlaku untuk distribusi publik?
- Apa proses yang akan digunakan untuk memeriksa lisensi pada PDF, kode vendored, atribusi, dan contoh percakapan sebelum rilis?
- Informasi apa yang perlu disunting atau dikeluarkan sebelum versi publik baru dibuat?
- Apakah ZIP lama dalam riwayat Git memuat materi yang perlu dihapus dari riwayat, dan bagaimana dampak penulisan ulang riwayat terhadap salinan atau fork yang sudah ada?
- Bagaimana pengguna dapat melaporkan materi sensitif atau masalah hak cipta dan meminta koreksi?

## 10. Struktur dan tata kelola repo

- Apakah folder paket hasil ekstraksi sebaiknya tetap disalin ke repo ini atau dirujuk sebagai repositori upstream dengan versi dan checksum?
- Bagaimana repo membedakan salinan upstream, modifikasi lokal, dan materi tambahan agar perubahan asal dapat ditelusuri?
- Kapan perubahan paket harus dibuat sebagai commit lokal, kapan sebagai fork, dan kapan sebagai kontribusi upstream?
- Siapa yang memutuskan bahwa paket atau eksperimen baru sesuai dengan tujuan repo?
- Bagaimana rilis, changelog, dan keputusan penting akan dicatat tanpa membuat dokumen administratif menggantikan bukti penggunaan?

## Cara menutup pertanyaan

Untuk setiap pertanyaan yang diteliti, catat: jawaban sementara, bukti dan versinya, konteks yang diperiksa, penjelasan alternatif, batas kesimpulan, serta temuan apa yang akan mengubah jawaban. Biarkan pertanyaan tetap terbuka bila bukti belum cukup.
